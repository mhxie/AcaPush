from django.test import TestCase
from newspush.models import Academy, News, Notice, NewsComment, StudentInfo
from django.core.exceptions import ValidationError

class AcademyModelTest(TestCase):
    def test_no_duplicate_Academy(self):
        pass
    def test_can_save_and_retriving_Academy(self):
        first_academy = Academy(code='cs')
        first_academy.name = 'Computer Science'
        first_academy.save()

        second_academy = Academy(code='se')
        second_academy.name = 'Software Engineering'
        second_academy.save()

        saved_academy = Academy.objects.all()
        self.assertEqual(saved_academy.count(), 2)

        first_saved_academy = saved_academy[0]
        second_saved_academy = saved_academy[1]
        self.assertEqual(first_saved_academy.name, 'Computer Science')
        self.assertEqual(second_saved_academy.name, 'Software Engineering')

class NewsModelTest(TestCase):
    def test_can_save_and_retriving_news(self):
        academy_ = Academy(code='cs')
        academy_.name = 'Computer Science'
        academy_.save()

        news_ = News.objects.create(academy=academy_)
        # first_news = News()
        # first_news.AcademyCode = Academy_
        # # news_.AcademyID = Academy_
        # # first_news = News(AcademyID = Academy)
        # first_news.save()
        #
        # second_news = News()
        # second_news.AcademyCode = Academy_
        # second_news.save()
        #
        # saved_news = News.objects.all()
        # self.assertEqual(saved_news.count(), 2)
        #
        # first_saved_news = saved_news[0]
        # second_saved_news = saved_news[1]
class CommentModelTest(TestCase):
    def test_can_save_and_retriving_comments(self):
        academy_ = Academy.objects.create(code='cs')
        news_ = News.objects.create(academy=academy_)
        student_info_ = StudentInfo.objects.create(studentID='0000000000000')
        comment_ = NewsComment.objects.create(news=news_, studentInfo=student_info_)
        self.assertEqual(NewsComment.objects.count(), 1)
