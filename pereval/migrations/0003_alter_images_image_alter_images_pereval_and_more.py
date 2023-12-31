# Generated by Django 4.2.8 on 2023-12-15 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0002_alter_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='images',
            name='pereval',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pereval.perevals'),
        ),
        migrations.DeleteModel(
            name='PerevalImages',
        ),
    ]
