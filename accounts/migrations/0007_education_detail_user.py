# Generated by Django 4.0.5 on 2022-08-12 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_education_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='education_detail',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='education_details', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
