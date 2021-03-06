from django.urls import reverse

from django_webtest import WebTest

from ..api.schema import info


class CatalogiSchemaTests(WebTest):
    def test_schema_page_title(self):
        response = self.app.get(reverse("schema-redoc-catalogi", kwargs={"version": 1}))
        self.assertEqual(response.html.find("title").text, info.title)
