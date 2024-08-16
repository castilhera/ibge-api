import unittest
from ibgeapi import StateService

class TestState(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.service = StateService()

    def test_get_all_should_return_27(self):
        states = self.service.get_all()
        self.assertEqual(len(states), 27)

    def test_get_35_should_return_sp(self):
        state = self.service.get(35)
        expected_acronym = "SP"
        self.assertEqual(state.acronym,
                         expected_acronym,
                         f"Returned {state.acronym}. \
                            Should return '{expected_acronym}'.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
