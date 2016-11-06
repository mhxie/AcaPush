from django.test import TestCase
from newspush.models import college, news, notice, newsComment, studentInfo
from django.core.exceptions import ValidationError

class CollegeModelTest(TestCase):
    def test_no_duplicate_college(self):
        pass
    def test_can_save_and_retriving_college(self):
        first_college = college()
        first_college.name = 'Computer Science'
        first_college.save()

        second_college = college()
        second_college.name = 'Software Engineering'
        second_college.save()

        saved_college = college.objects.all()
        self.assertEqual(saved_college.count(), 2)

        first_saved_college = saved_college[0]
        second_saved_college = saved_college[1]
        self.assertEqual(first_saved_college.name, 'Computer Science')
        self.assertEqual(second_saved_college.name, 'Software Engineering')

class NewsModelTest(TestCase):
    def test_no_duplicate_news_id(self):
        pass
