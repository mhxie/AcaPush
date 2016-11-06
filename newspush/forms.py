from django import forms
from newspush.models import NewsComment
from django.core.exceptions import ValidationError


EMPTY_COMMENT_ERROR = "You can't have an empty comment item"

class CommentForm(forms.models.ModelForm):
    class Meta:
        model = NewsComment
        fields = ('content', 'ip',)

        error_messages = {
            'content': {'required': EMPTY_COMMENT_ERROR}
        }

    def save(self, for_news, for_stu_info):
        self.instance.news = for_news
        self.instance.studentInfo = for_stu_info
        return super().save()
