from django.test import TestCase

# Create your tests here.
class WikiTestCase(TestCase):

    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """

        #1. create test data

        #2. make a get request 

        #3. check the response returns what we want
        self.assertEqual(True, True)


class QuestionViewTests(TestCase):
    def test_show_question_creation_form(self):
        #1. 
        User = User.objects.create_user(username='jim', password='password')
        self.client.login(username='jim', password='password')

        #2.
        response = self.client.get('polls/create')

        #3. 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response, 'New Poll')

        #4. check if data in database

    def test_submit_question_creation_form(self):
        pass
