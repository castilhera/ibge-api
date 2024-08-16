from requests import get, post

class _APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint:str, params:dict[str,str]=None):
        """Use a HTTP Client to GET data.
        """
        response = get(f"{self.base_url}{endpoint}",
                       params=params,
                       timeout=5)
        response.raise_for_status()
        return response.json()
