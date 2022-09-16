import unittest
from Day22 import AnonymousSurvey

# question = 'Cola or pepsi?'
# my_question = AnonymousSurvey(question)
# my_question.show_question()
# while True:
#     response = input('I drink ')
#     if response == 'q':
#         break
#     my_question.store_responses(response)

# print('\n\n')
# my_question.show_results()


class TestAnonymousSurvey(unittest.TestCase):
    """This is to test class AnonymousSurvey"""
    def test_store_single_question(self):
        """test one question will be stored"""
        question = 'Cola or pepsi:'
        my_question = AnonymousSurvey(question)
        my_question.store_responses('Pepsi')
        self.assertIn('Pepsi', my_question.responses)




class Employee:
    """This is to store empolyee info and raise the salary"""
    def __init__(self, first_name, last_name, salary=2000):
        """format the info"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self):
        """raise the salary for 5000 dollars"""
        self.salary += 5000


class TestEmployee(unittest.TestCase):
    """This is to test Employee class"""
    def test_default_salary(self):
        employ1 = Employee('Katono', 'Wong')
        self.assertEqual(2000, employ1.salary)
    def test_raise_salary(self):
        employ1 = Employee('Katono', 'Wong')
        employ1.give_raise()
if __name__ == '__main__':
    unittest.main()