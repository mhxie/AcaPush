from django.test import TestCase
from newspush.models import Academic, News, Notice, NewsComment, StudentInfo
from django.core.exceptions import ValidationError

class AcademicModelTest(TestCase):
    def test_no_duplicate_academic(self):
        pass
    def test_can_save_and_retriving_academic(self):
        first_academic = Academic(code='cs')
        first_academic.name = 'Computer Science'
        first_academic.save()

        second_academic = Academic(code='se')
        second_academic.name = 'Software Engineering'
        second_academic.save()

        saved_academic = Academic.objects.all()
        self.assertEqual(saved_academic.count(), 2)

        first_saved_academic = saved_academic[0]
        second_saved_academic = saved_academic[1]
        self.assertEqual(first_saved_academic.name, 'Computer Science')
        self.assertEqual(second_saved_academic.name, 'Software Engineering')

class NewsModelTest(TestCase):
    def test_can_save_and_retriving_news(self):
        academic_ = Academic(code='cs')
        academic_.name = 'Computer Science'
        academic_.save()

        news_ = News.objects.create(academic=academic_)
        # first_news = News()
        # first_news.academicCode = academic_
        # # news_.academicID = academic_
        # # first_news = News(academicID = academic)
        # first_news.save()
        #
        # second_news = News()
        # second_news.academicCode = academic_
        # second_news.save()
        #
        # saved_news = News.objects.all()
        # self.assertEqual(saved_news.count(), 2)
        #
        # first_saved_news = saved_news[0]
        # second_saved_news = saved_news[1]
class CommentModelTest(TestCase):
    def test_can_save_and_retriving_comments(self):
        academic_ = Academic.objects.create(code='cs')
        news_ = News.objects.create(academic=academic_)
        student_info_ = StudentInfo.objects.create(studentID='0000000000000')
        comment_ = NewsComment.objects.create(news=news_, studentInfo=student_info_)
        self.assertEqual(NewsComment.objects.count(), 1)
