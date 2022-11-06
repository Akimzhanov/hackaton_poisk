# Generated by Django 4.1.3 on 2022-11-05 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_remove_category_id_category_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lost',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='lost',
            name='category',
            field=models.CharField(choices=[('documents', 'Документ'), ('keys', 'Ключи'), ('technique', 'Техника'), ('wallets', 'Кошельки'), ('amimals', 'Животные'), ('decorations', 'Украшения'), ('bags', 'Сумки'), ('other', 'Другое')], default=False, max_length=100),
        ),
    ]
