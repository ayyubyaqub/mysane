# Generated by Django 4.0.5 on 2022-09-09 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_college_detail_delete_professional_basic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_fellowship',
            name='organisation_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user_volunteership',
            name='organisation_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='user_preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefered_job_type', models.CharField(blank=True, max_length=255, null=True)),
                ('prefered_job_location', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preference', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification_name', models.CharField(blank=True, max_length=255, null=True)),
                ('certification_completion_id', models.CharField(blank=True, max_length=255, null=True)),
                ('certification_url', models.TextField(blank=True, null=True)),
                ('issue_date', models.CharField(blank=True, max_length=255, null=True)),
                ('expiry_date', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certification', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
