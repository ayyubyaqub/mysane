# Generated by Django 4.0.5 on 2022-08-30 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_skill_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='skill', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
