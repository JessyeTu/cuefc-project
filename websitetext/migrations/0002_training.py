# Generated by Django 2.2.12 on 2020-07-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitetext', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Training', models.TextField()),
                ('Beginners', models.TextField()),
            ],
        ),
    ]
