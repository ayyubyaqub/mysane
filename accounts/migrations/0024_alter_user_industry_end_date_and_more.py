# Generated by Django 4.0.5 on 2022-09-08 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_user_industry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_industry',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_industry',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
