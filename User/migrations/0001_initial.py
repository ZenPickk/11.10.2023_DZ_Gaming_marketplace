# Generated by Django 4.2.5 on 2023-10-10 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usermame', models.TextField()),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('email', models.TextField()),
                ('pasword', models.TextField()),
            ],
        ),
    ]