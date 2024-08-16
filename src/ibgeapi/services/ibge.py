from abc import ABC
from ibgeapi._api_client import _APIClient

class IGBEService(ABC):

    def __init__(self) -> None:
        self.client = _APIClient(
            base_url="https://servicodados.ibge.gov.br/api/v1"
        )
