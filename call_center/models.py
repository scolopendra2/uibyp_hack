import django.core
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Category(models.Model):
    name = models.TextField('название', max_length=70, null=False, unique=True)

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    login = models.TextField('имя сотрудника', max_length=50, null=False)
    categories = models.ManyToManyField(
        Category, related_name='workers_categories'
    )
    username = models.TextField(null=True, unique=False)

    password = models.TextField(
        'пароль',
        validators=[
            django.core.validators.MinLengthValidator(
                limit_value=8,
                message='Пароль должен содержать не менее 8 символов.',
            ),
            django.core.validators.RegexValidator(
                regex='[A-Z]',
                message='Пароль должен содержать хотя бы 1 заглавную букву.',
            ),
        ],
    )

    groups = models.ManyToManyField(Group, related_name='workers')
    user_permissions = models.ManyToManyField(
        Permission, related_name='workers'
    )

    class Meta:
        verbose_name = 'сотрудника'
        verbose_name_plural = 'сотрудники'

    def __str__(self):
        return self.login


class Question(models.Model):
    question = models.TextField('вопрос', max_length=150, null=False)
    answer = models.TextField('ответ', max_length=250)
    id_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='question'
    )
    id_worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name='question'
    )
    id_user = models.TextField(null=True)
    status = models.BooleanField(
        'статус вопроса',
        default=False,
        help_text='Текущий статус вопроса',
    )
    important = models.IntegerField(
        'важность вопроса',
        validators=[
            django.core.validators.MinValueValidator(1),
            django.core.validators.MaxValueValidator(3),
        ],
    )
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-important', ]
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def get_id_for_question(self, category_name):
        workers = (
            Worker.objects.filter(categories__name=category_name)
            .only('id')
            .all()
        )
        min_tasks = workers.first()
        for worker in workers:
            questions = (
                Question.objects.filter(id_worker=worker.id, status=False)
                .only('id')
                .all()
            )
            questions_min = (
                Question.objects.filter(id_worker=min_tasks.id, status=False)
                .only('id')
                .all()
            )
            if len(questions_min) > len(questions):
                min_tasks = worker
        return min_tasks

    def __str__(self):
        return self.question


class Mark(models.Model):
    id_question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='mark'
    )
    mark = models.IntegerField(
        'оценка',
        validators=[
            django.core.validators.MinValueValidator(1),
            django.core.validators.MaxValueValidator(5),
        ],
    )

    class Meta:
        verbose_name = 'оценку'
        verbose_name_plural = 'оценки'

    def __str__(self):
        return self.id_question.question[:15]
