# Generated by Django 4.2.7 on 2023-12-29 10:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('3bacb497-9c92-4a58-ba77-70fd6efa0f0d'), editable=False, primary_key=True, serialize=False),
        ),
    ]
