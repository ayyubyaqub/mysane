# Generated by Django 4.0.5 on 2022-09-07 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_alter_user_career_is_currently_working'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_socialmedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plateform', models.CharField(max_length=255)),
                ('link', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socialmedia', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
