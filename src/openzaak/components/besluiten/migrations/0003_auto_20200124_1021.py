# Generated by Django 2.2.9 on 2020-01-24 10:21

from django.db import migrations
import django_loose_fk.fields


class Migration(migrations.Migration):

    dependencies = [
        ("besluiten", "0002_auto_20200124_1005"),
    ]

    operations = [
        migrations.AddField(
            model_name="besluit",
            name="besluittype",
            field=django_loose_fk.fields.FkOrURLField(
                blank=False,
                fk_field="_besluittype",
                null=False,
                url_field="_besluittype_url",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="besluit",
            name="zaak",
            field=django_loose_fk.fields.FkOrURLField(
                blank=True, fk_field="_zaak", null=True, url_field="_zaak_url"
            ),
        ),
        migrations.AddField(
            model_name="besluitinformatieobject",
            name="informatieobject",
            field=django_loose_fk.fields.FkOrURLField(
                blank=False,
                fk_field="_informatieobject",
                null=False,
                url_field="_informatieobject_url",
            ),
            preserve_default=False,
        ),
    ]