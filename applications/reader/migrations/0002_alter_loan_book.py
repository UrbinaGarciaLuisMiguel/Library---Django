# Generated by Django 4.1.4 on 2023-01-10 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_category'),
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_loan', to='book.book'),
        ),
    ]
