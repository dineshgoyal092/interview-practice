# Generated by Django 3.2.5 on 2021-07-11 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0002_auto_20210710_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
