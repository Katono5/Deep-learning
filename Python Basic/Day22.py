import unittest


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        formatted_name = f'{first_name} {middle_name} {last_name}'
    else:
        formatted_name = f'{first_name} {last_name}'
    return formatted_name


class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        """Is that okay to collect a full name"""
        formatted_name = get_formatted_name('James', 'Bond')
        self.assertEqual(formatted_name, 'James Bond')

    def test_first_last_middle_name(self):
        """Is that okay to collect a full name"""
        formatted_name = get_formatted_name('James', 'Bond', 'Mad')
        self.assertEqual(formatted_name, 'James Mad Bond')


# if __name__ == '__main__':
#     unittest.main()


def get_formatted_city(city, country):
    formatted_city = f'{city},{country}'
    return formatted_city


class CityTestCase(unittest.TestCase):
    def test_cityname(self):
        """This is to store shit to collect a full describtion"""
        formatted_city = get_formatted_city('Santiago', 'Chile')
        self.assertEqual(formatted_city, 'Santiago,Chile')


def get_full_name(city, country, population=''):
    fullname = f'{city},{country} - {population}'
    return fullname


class CityTestCase(unittest.TestCase):
    def test_cityname(self):
        """This is to store shit to collect a full describtion"""
        formatted_city = get_full_name('Santiago', 'Chile')
        self.assertEqual(formatted_city, 'Santiago,Chile - ')


if __name__ == '__main__':
    unittest.main()

# Here's two things
# one is that any function waiting to be tested should be named begin with 'test_'
# the other is that the main could only be used once and that's the end of the unittest

"""
assertEqual(a, b)  核实 a == b
assertNotEqual(a, b) 核实 a != b
assertTrue(x)  核实x为True
assertFalse(x) 核实x为Flase
assertIn(item, list) 核实item在list中
assertNotIn(Item, list) 核实item不在list中
"""


class AnonymousSurvey:
    """collect answers from anonymous surveies"""

    def __init__(self, question):
        """Collect a question,and be ready for the answer"""
        self.question = question
        self.responses = []

    def show_question(self):
        """show the questions in the survey"""
        print(self.question)

    def store_responses(self, new_responses):
        self.responses.append(new_responses)

    def show_results(self):
        """show all the answers we collected previously"""
        print("Survey results:")
        for response in self.responses:
            print(f'- {response}')
