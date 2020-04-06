from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from extra_views import ModelFormSetView
from zgw_consumers.models import Service

from openzaak.components.autorisaties.admin_views import get_form_data

from .forms import (
    ExternalServiceForm,
    InternalServiceForm,
    NLXConfigForm,
    get_nlx_choices,
)
from .models import InternalService, NLXConfig
from .utils import AdminRequiredMixin


class ConfigDetailView(AdminRequiredMixin, TemplateView):
    template_name = "config/config_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        nlx = NLXConfig.get_solo()
        context["nlx"] = nlx

        internal_services = InternalService.objects.order_by("api_type").all()
        context["internal_services"] = internal_services

        external_services = Service.objects.order_by("api_type", "api_root").all()
        context["external_services"] = external_services

        return context


class NLXConfigView(AdminRequiredMixin, UpdateView):
    model = NLXConfig
    form_class = NLXConfigForm
    template_name = "config/config_nlx.html"
    success_url = reverse_lazy("config-internal")

    def get_object(self, queryset=None):
        nlx = NLXConfig.get_solo()
        return nlx


class InternalConfigView(AdminRequiredMixin, ModelFormSetView):
    model = InternalService
    queryset = InternalService.objects.order_by("api_type")
    form_class = InternalServiceForm
    factory_kwargs = {"extra": 0}
    template_name = "config/config_internal.html"
    success_url = reverse_lazy("config-external")


class ExternalConfigView(AdminRequiredMixin, ModelFormSetView):
    model = Service
    queryset = Service.objects.order_by("api_type", "api_root")
    form_class = ExternalServiceForm
    factory_kwargs = {"extra": 0}
    template_name = "config/config_external.html"
    success_url = reverse_lazy("config-detail")

    def get_context_data(self, **kwargs):
        formset = kwargs.pop("formset", self.get_formset())
        kwargs["formset"] = formset

        context = super().get_context_data(**kwargs)
        context.update(
            {
                "formdata": [get_form_data(form) for form in formset],
                "nlx_choices": get_nlx_choices(),
            }
        )

        return context
