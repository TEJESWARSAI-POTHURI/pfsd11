
from django.test import TestCase
from django.urls import reverse
from .models import Question, Choice

class QuizTests(TestCase):
    def setUp(self):
        self.question = Question.objects.create(text='What is 2 + 2?')
        self.correct_choice = Choice.objects.create(question=self.question, text='4', is_correct=True)
        self.wrong_choice = Choice.objects.create(question=self.question, text='5', is_correct=False)

    def test_quiz_view(self):
        response = self.client.get(reverse('quiz'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.question.text)

    def test_result_view_correct_answer(self):
        data = {str(self.question.id): str(self.correct_choice.id)}
        response = self.client.post(reverse('result'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your score is: 1')

    def test_result_view_wrong_answer(self):
        data = {str(self.question.id): str(self.wrong_choice.id)}
        response = self.client.post(reverse('result'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your score is: 0')
