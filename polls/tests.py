import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Question, Choice
from django.urls import reverse


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class ChoicesIndexViewTest(TestCase):
    def question_no_choices(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available.')
        self.assertQuerySetEqual(response.context['latest_question_list'], [])

    def question_with_choices(self):
        question = create_question(question_text='Past question.', days=-5)
        question.choice_set.create(choice_text='Very good!')
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(response.context['latest_question_list'], [question], )


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        # If no questions exist, an appropriate message is displayed
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available.')
        self.assertQuerySetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        # Question with a pub_date in the past are displayed on the index page.
        question = create_question(question_text='Past question.', days=-30)
        question.choice_set.create(choice_text='Not much', votes=0)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(response.context['latest_question_list'], [question], )

    def test_future_question(self):
        # Question with a pub_date in the future aren't displayed on the index page.
        create_question(question_text='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available')
        self.assertQuerySetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        question = create_question(question_text='Past question.', days=-30)
        question.choice_set.create(choice_text='So nice', votes=0)
        create_question(question_text='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(response.context['latest_question_list'], [question], )

    def test_two_past_questions(self):
        # The questions index page may display multiple questions.
        question1 = create_question(question_text='Past question 1.', days=-30)
        question1.choice_set.create(choice_text='Very good', votes=0)
        question2 = create_question(question_text='Past question 2.', days=-5)
        question2.choice_set.create(choice_text='Very goood!', votes=0)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(response.context['latest_question_list'], [question1, question2], ordered=False)


class ChoicesDetailViewTests(TestCase):
    def question_no_choices(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available.')
        self.assertQuerySetEqual(response.context['latest_question_list'], [])

    def question_with_choices(self):
        question = create_question(question_text='Past question.', days=-5)
        question.choice_set.create(choice_text='Very good!')
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(response.context['latest_question_list'], [question], )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        # The detail view of a question with a pub_date in the future returns a 404 not found.
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        # The detail view of a question with pub_date in the past displays the question's text.
        past_question = create_question(question_text='Past Question.', days=-5)
        past_question.choice_set.create(choice_text='Nice, nice', votes=0)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class ChoicesResultsViewTests(TestCase):
    def question_no_choices(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available.')
        self.assertQuerySetEqual(response.context['latest_question_list'], [])

    def question_with_choices(self):
        question = create_question(question_text='Past question.', days=-5)
        question.choice_set.create(choice_text='Very good!')
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(response.context['latest_question_list'], [question], )


class QuestionResultsViewTests(TestCase):
    def test_future_question(self):
        # This function has to return a page 404
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:results', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        # This function tests past questions, they have to be displayed and published
        past_question = create_question(question_text='Past question', days=-5)
        past_question.choice_set.create(choice_text='Wow, very nice', votes=0)
        url = reverse('polls:results', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        # was_published_recently returns False for questions whose pub_date is in the future.

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() + datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
