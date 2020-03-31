import uuid
from datetime import date
from typing import Dict, Union

from django.conf import settings
from django.utils import timezone

from vng_api_common.tests import get_operation_url as _get_operation_url

JsonValue = Union[str, None, int, float]


def get_operation_url(operation, **kwargs):
    return _get_operation_url(
        operation, spec_path=settings.SPEC_URL["documenten"], **kwargs
    )


def get_eio_response(url: str, **overrides) -> Dict[str, JsonValue]:
    eio_type = (
        f"https://external.catalogus.nl/api/v1/informatieobjecttypen/{uuid.uuid4()}"
    )
    eio = {
        "url": url,
        "identificatie": "DOCUMENT-00001",
        "bronorganisatie": "272618196",
        "creatiedatum": date.today().isoformat(),
        "titel": "some titel",
        "auteur": "some auteur",
        "status": "",
        "formaat": "some formaat",
        "taal": "nld",
        "beginRegistratie": timezone.now().isoformat().replace("+00:00", "Z"),
        "versie": 1,
        "bestandsnaam": "",
        "inhoud": f"{url}/download?versie=1",
        "bestandsomvang": 100,
        "link": "",
        "beschrijving": "",
        "ontvangstdatum": None,
        "verzenddatum": None,
        "ondertekening": {"soort": "", "datum": None},
        "indicatieGebruiksrecht": None,
        "vertrouwelijkheidaanduiding": "openbaar",
        "integriteit": {"algoritme": "", "waarde": "", "datum": None},
        "informatieobjecttype": eio_type,
        "locked": False,
    }
    eio.update(**overrides)
    return eio


def get_oio_response(
    io_url: str, object_url: str, object_type: str = "zaak"
) -> Dict[str, JsonValue]:
    start = io_url.split("enkelvoudiginformatieobjecten")[0]
    url = f"{start}objectinformatieobjecten"
    oio = {
        "url": url,
        "informatieobject": io_url,
        "object": object_url,
        "objectType": object_type,
    }
    return oio


def get_informatieobjecttype_response(
    catalogus: str, informatieobjecttype: str
) -> dict:
    return {
        "url": informatieobjecttype,
        "catalogus": catalogus,
        "omschrijving": "some desc",
        "vertrouwelijkheidaanduiding": "openbaar",
        "beginGeldigheid": "2019-11-18",
        "concept": False,
    }


def get_catalogus_response(catalogus: str, informatieobjecttype: str) -> dict:
    return {
        "url": catalogus,
        "domein": "PUB",
        "contactpersoonBeheerTelefoonnummer": "0612345678",
        "rsin": "517439943",
        "contactpersoonBeheerNaam": "Jan met de Pet",
        "contactpersoonBeheerEmailadres": "jan@petten.nl",
        "informatieobjecttypen": [informatieobjecttype],
        "zaaktypen": [],
        "besluittypen": [],
    }
