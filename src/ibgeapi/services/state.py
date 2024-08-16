from ibgeapi.models.state import State
from ibgeapi.services.location import LocationService

class StateService(LocationService):

    def __init__(self) -> None:
        super().__init__("/estados")

    def parse(self, response) -> State:
        return State(
            id=response["id"],
            name=response["nome"],
            acronym=response["sigla"]
        )
