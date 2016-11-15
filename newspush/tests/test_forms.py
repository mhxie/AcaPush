from django.test import TestCase
from newspush.forms import (
    EMPTY_INPUT_ERROR, TOO_LONG_ERROR, TOO_SHORT_ERROR,
    CommentForm, LoginForm
)
from newspush.models import Academy, News, NewsComment, StudentInfo
from unittest import skip
from django.core.exceptions import ValidationError
from copy import deepcopy

class CommentFormTest(TestCase):
    def test_form_validation_for_blank_items(self):
        student_ = StudentInfo.objects.create(studentID='2014141466666')
        form = CommentForm(data={'content': '',
                                 'ip': '127.0.0.1'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], [EMPTY_INPUT_ERROR])

    def test_form_save_handles_saving_to_a_news(self):
        academy_ = Academy.objects.create()
        news_ = News.objects.create(academy=academy_)
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

class LoginFormTest(TestCase):
    valid_form = LoginForm(data={
        'scu_id': '2014141466666',
        'password': '666666',
        'name': 'normal name',
        'nickname': 'abnormal name',
    })
    def test_valid_form_can_pass_validation(self):
        valid_form = LoginFormTest.valid_form
        self.assertTrue(valid_form.is_valid())

    def test_form_validation_for_strange_id(self):
        invalid_form = deepcopy(LoginFormTest.valid_form)
        invalid_form.data['scu_id'] = '123'
        self.assertFalse(invalid_form.is_valid())
        self.assertEqual(invalid_form.errors['scu_id'], [TOO_SHORT_ERROR])

    def test_form_validation_for_no_password(self):
        invalid_form = deepcopy(LoginFormTest.valid_form)
        invalid_form.data['password'] = None
        self.assertFalse(invalid_form.is_valid())
        self.assertEqual(invalid_form.errors['password'], [EMPTY_INPUT_ERROR])

    def test_form_validation_for_too_long_name(self):
        invalid_form = deepcopy(LoginFormTest.valid_form)
        invalid_form.data['name'] = '012345678901234567890'
        self.assertFalse(invalid_form.is_valid())
        self.assertEqual(invalid_form.errors['name'], [TOO_LONG_ERROR])

    def test_form_validation_for_too_long_nickname(self):
        invalid_form = deepcopy(LoginFormTest.valid_form)
        invalid_form.data['nickname'] = '012345678901234567890'
        self.assertFalse(invalid_form.is_valid())
        self.assertEqual(invalid_form.errors['nickname'], [TOO_LONG_ERROR])
