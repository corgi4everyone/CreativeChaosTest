# Generated by Django 3.2.7 on 2021-09-10 08:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0003_alter_catagory_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
