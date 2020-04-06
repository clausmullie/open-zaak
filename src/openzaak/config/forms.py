import socket
from typing import List, Tuple
from urllib.parse import urlparse

from django.forms import ChoiceField, ModelForm, ValidationError
from django.utils.translation import ugettext_lazy as _

from zgw_consumers.models import Service

from openzaak.nlx.api import get_services

from .models import InternalService, NLXConfig


class NLXConfigForm(ModelForm):
    class Meta:
        model = NLXConfig
        fields = ("directory", "outway")

    def clean_outway(self):
        outway = self.cleaned_data["outway"]

        if not outway:
            return outway

        # try to tcp connect to the port
        parsed = urlparse(outway)
        with socket.socket() as s:
            s.settimeout(2)  # 2 seconds
            try:
                s.connect((parsed.hostname, parsed.port))
            except ConnectionRefusedError:
                raise ValidationError(
                    _("Connection refused. Please, provide a correct address")
                )

        return outway


class InternalServiceForm(ModelForm):
    class Meta:
        model = InternalService
        fields = ("enabled", "nlx")


def get_nlx_choices() -> List[Tuple[str, str]]:
    choices = [("", "---No NLX---")]
    nlx_outway = NLXConfig.get_solo().outway
    if not nlx_outway:
        return choices

    services = get_services()
    for service in services:
        url = f"{nlx_outway}{service['organization_name']}/{service['service_name']}"
        label = f"{service['organization_name']}: {service['service_name']}"
        choices.append((url, label))
    return choices


class ExternalServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = (
            "api_root",
            "api_type",
            "label",
            "auth_type",
            "nlx",
            "client_id",
            "secret",
            "header_key",
            "header_value",
        )
