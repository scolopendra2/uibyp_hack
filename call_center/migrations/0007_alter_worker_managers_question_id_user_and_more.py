# Generated by Django 4.2.7 on 2023-11-18 23:38

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('homepage', '0001_initial'),
        ('call_center', '0006_alter_worker_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='worker',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='id_user',
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='question',
                to='homepage.user',
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='important',
            field=models.IntegerField(
                default=1993,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(3),
                ],
                verbose_name='важность вопроса',
            ),
            preserve_default=False,
        ),
    ]
