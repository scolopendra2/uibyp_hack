# Generated by Django 4.2.7 on 2023-11-19 08:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('call_center', '0008_alter_question_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(max_length=250, verbose_name='ответ'),
        ),
    ]
