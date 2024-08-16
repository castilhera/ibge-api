from ibgeapi.models.municipality import Municipality
from ibgeapi.services.location import LocationService

class MunicipalityService(LocationService):

    def __init__(self) -> None:
        super().__init__("/municipios")

    def parse(self, response) -> Municipality:
        return Municipality(
            id=response["id"],
            name=response["nome"]
        )
