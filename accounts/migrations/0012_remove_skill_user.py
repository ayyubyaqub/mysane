# Generated by Django 4.0.5 on 2022-08-30 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_rename_professional_details_professional_detail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='user',
        ),
    ]