# Generated by Django 4.0.5 on 2022-09-08 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_rename_end_date_user_career_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='College_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(blank=True, max_length=100, null=True)),
                ('degree', models.CharField(blank=True, max_length=100, null=True)),
                ('university', models.CharField(blank=True, max_length=100, null=True)),
                ('stream', models.CharField(blank=True, max_length=100, null=True)),
                ('From', models.DateField(blank=True, null=True)),
                ('to', models.DateField(blank=True, null=True)),
                ('grades', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='college_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='professional_basic',
        ),
    ]