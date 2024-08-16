import unittest
from ibgeapi import MunicipalityService

class TestMunicipality(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.service = MunicipalityService()

    def test_get_3304557_should_return_rio_de_janeiro(self):
        municipality = self.service.get(3304557)
        expected_name = "Rio de Janeiro"
        self.assertEqual(municipality.name,
                         expected_name,
                         f"Returned {municipality.name}. \
                            Should return '{expected_name}'.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
