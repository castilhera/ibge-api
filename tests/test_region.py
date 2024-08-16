import unittest
from ibgeapi import RegionService

class TestRegion(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.service = RegionService()

    def test_get_all_should_return_5(self):
        regions = self.service.get_all()
        self.assertEqual(len(regions), 5)

    def test_get_3_should_return_sudeste(self):
        region = self.service.get(3)
        expected_name = "Sudeste"
        self.assertEqual(region.name,
                         expected_name,
                         f"Returned {region.name}. \
                            Should return '{expected_name}'.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
