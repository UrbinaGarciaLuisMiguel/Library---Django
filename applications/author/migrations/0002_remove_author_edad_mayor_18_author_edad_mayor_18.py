# Generated by Django 4.1.1 on 2023-01-21 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='author',
            constraint=models.CheckConstraint(check=models.Q(('age__gte', 18)), name='edad_mayor_18'),
        ),
    ]