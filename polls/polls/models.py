from django.db import models

# Question
# pk, 질문내용, 등록일
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.question_text


# Choice
# pk, 선택 문항, 투표수, Question 관계
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text

