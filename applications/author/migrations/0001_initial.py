# Generated by Django 4.1.4 on 2022-12-20 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surnames', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
    ]
