from abc import abstractmethod
from collections import defaultdict
from ibgeapi.services.ibge import IGBEService

class LocationService(IGBEService):

    @abstractmethod
    def parse(self, response):
        pass

    def get(self, loc_id:int):
        response = self.client.get(f"{self.endpoint}/{loc_id}", 
                                   params=self._filters)
        
        if isinstance(response, list):
            response = response[0]

        return self.parse(response) \
            if response else None

    def get_all(self, orderBy:str="nome"):
        self._filters["orderBy"] = orderBy
        response = self.client.get(self.endpoint, 
                                   params=self._filters)
        return [self.parse(location) for location in response] \
            if response else []

    def __init__(self, endpoint: str) -> None:
        super().__init__()
        self._filters = defaultdict(str)
        self.endpoint = f"/localidades{endpoint}"
