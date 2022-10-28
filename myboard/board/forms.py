from django import forms

from .models import Answer, Comment, Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']


# AnsworForm - fields : content
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']


# CommentForm - fields : content
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']