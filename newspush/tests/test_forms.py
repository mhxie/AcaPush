from django.test import TestCase
from newspush.forms import (
    EMPTY_COMMENT_ERROR, CommentForm
)
from newspush.models import Academic, News, NewsComment, StudentInfo
from unittest import skip
from django.core.exceptions import ValidationError

class CommentFormTest(TestCase):
    def test_form_validation_for_blank_items(self):
        student_ = StudentInfo.objects.create(studentID='2014141466666')
        form = CommentForm(data={'content': '',
                                 'studentID': '2014141466666',
                                 'ip': '127.0.0.1'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], [EMPTY_COMMENT_ERROR])

    def test_form_save_handles_saving_to_a_news(self):
        academic_ = Academic.objects.create(code='cs')
        news_ = News.objects.create(academic=academic_)
        student_ = StudentInfo.objects.create(studentID='2014141466666')
        form = CommentForm(data={'content': 'This is a comment',
                                 'ip': '127.0.0.1'})

        self.assertTrue(form.is_valid())
        new_comment = form.save(for_news=news_, for_stu_info=student_)
        self.assertEqual(new_comment, NewsComment.objects.first())
        self.assertEqual(new_comment.content, 'This is a comment')
        self.assertEqual(new_comment.ip, '127.0.0.1')
        self.assertEqual(new_comment.news, news_)
        self.assertEqual(new_comment.studentInfo, student_)
