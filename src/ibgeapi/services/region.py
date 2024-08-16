from ibgeapi.models.region import Region
from ibgeapi.services.location import LocationService

class RegionService(LocationService):

    def __init__(self) -> None:
        super().__init__("/regioes")

    def parse(self, response) -> Region:
        return Region(
            id=response["id"],
            name=response["nome"],
            acronym=response["sigla"]
        )
