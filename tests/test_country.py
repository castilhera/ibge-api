import unittest
from ibgeapi import CountryService

class TestCountry(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.service = CountryService()

    def test_get_all_should_return_193(self):
        countries = self.service.get_all()
        self.assertEqual(len(countries), 193)

    def test_get_76_should_return_brasil(self):
        country = self.service.get(76)
        expected_iso_alpha3 = "BRA"
        self.assertEqual(country.iso_alpha3,
                         expected_iso_alpha3,
                         f"Returned {country.iso_alpha3}. \
                            Should return '{expected_iso_alpha3}'.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
