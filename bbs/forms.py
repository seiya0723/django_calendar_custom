from django import forms
from .models import Topic

from django.core.validators import MinValueValidator, MaxValueValidator

class TopicForm(forms.ModelForm):
    class Meta:
        model   = Topic
        fields  = ["comment"]


# 年月検索用バリデーションフォーム
class YearMonthForm(forms.Form):
    year    = forms.IntegerField()
    month   = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])


