from ibgeapi.models.country import Country
from ibgeapi.services.location import LocationService

class CountryService(LocationService):

    def __init__(self) -> None:
        super().__init__("/paises")
        self._prefix = "pais-"
        self._filters["view"] = "nivelado"

    def parse(self, response) -> Country:
        return Country(
            id=response[f"{self._prefix}M49"],
            iso_alpha2=response[f"{self._prefix}ISO-ALPHA-2"],
            iso_alpha3=response[f"{self._prefix}ISO-ALPHA-3"],
            name=response[f"{self._prefix}nome"]
        )
