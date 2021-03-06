from django import forms
from django.test import TestCase

from openzaak.components.zaken.admin import ZaakForm


class TestZaakForm(TestCase):
    def test_zaak_form_clean_does_not_throw_exception_if_zaaktype_is_given(self):
        form = ZaakForm()
        form.cleaned_data = {
            "_zaaktype": 1,
        }
        try:
            form.clean()
        except forms.ValidationError:
            self.fail("Exception was raised in clean function when it should not have")

    def test_zaak_form_clean_does_not_throw_exception_if_zaaktype_url_is_given(self):
        form = ZaakForm()
        form.cleaned_data = {
            "_zaaktype_url": "https://testserver",
        }
        try:
            form.clean()
        except forms.ValidationError:
            self.fail("Exception was raised in clean function when it should not have")

    def test_zaak_form_clean_throws_exception_if_zaaktype_and_zaaktype_url_are_not_given(
        self,
    ):
        form = ZaakForm()
        form.cleaned_data = {}
        with self.assertRaises(forms.ValidationError):
            form.clean()
