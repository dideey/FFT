# Generated by Django 5.1.2 on 2024-10-28 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_user_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
