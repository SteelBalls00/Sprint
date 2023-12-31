# Generated by Django 4.2.7 on 2023-12-18 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0004_alter_images_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevals',
            name='status',
            field=models.CharField(choices=[('new', 'Создано'), ('pending', 'Взято в работу'), ('accepted', 'Успешно'), ('rejected', 'Отклонено')], default='new', max_length=10, verbose_name='Статус заявки'),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=128),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.IntegerField(verbose_name='Телефон'),
        ),
    ]
