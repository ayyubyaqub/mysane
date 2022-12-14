# Generated by Django 4.0.5 on 2022-08-31 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_user_dob_user_leadership'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_volunteership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volunteer_title', models.CharField(blank=True, max_length=255, null=True)),
                ('volunteer_desc', models.TextField()),
                ('volunteer_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteership', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
