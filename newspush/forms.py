from django import forms
from newspush.models import NewsComment, StudentInfo
from django.core.exceptions import ValidationError


EMPTY_INPUT_ERROR = "You can't have an empty item"
TOO_LONG_ERROR = "Too long!!!"
TOO_SHORT_ERROR = "Too short!!!"

class CommentForm(forms.models.ModelForm):
    class Meta:
        model = NewsComment
        fields = ('content', 'ip',)

        error_messages = {
            'content': {'required': EMPTY_INPUT_ERROR}
        }

    def save(self, for_news, for_stu_info):
        self.instance.news = for_news
        self.instance.studentInfo = for_stu_info
        return super().save()

class LoginForm(forms.Form):
    scu_id = forms.CharField(max_length=13, min_length=13,
                             error_messages={
                                'max_length': TOO_LONG_ERROR,
                                'min_length': TOO_SHORT_ERROR,
                            })
    password = forms.CharField(error_messages={'required': EMPTY_INPUT_ERROR})
    name = forms.CharField(required=False, max_length=20,
                           error_messages={'max_length': TOO_LONG_ERROR})
    nickname = forms.CharField(required=False, max_length=20,
                               error_messages={'max_length': TOO_LONG_ERROR})
