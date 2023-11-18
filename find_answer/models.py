from django.db import models


class Questions(models.Model):
    question = models.TextField('вопрос', max_length=70, null=False)
    answer = models.TextField('ответ', null=False)

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.question[:15]
