# Generated by Django 5.2.3 on 2025-07-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
