# Generated by Django 4.2 on 2023-05-22 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_rename_color01_home_card_color01_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img_01', models.CharField(blank=True, max_length=50)),
                ('img_02', models.CharField(blank=True, max_length=50)),
                ('img_03', models.CharField(blank=True, max_length=50)),
                ('img_04', models.CharField(blank=True, max_length=50)),
                ('img_05', models.CharField(blank=True, max_length=50)),
                ('img_06', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Slides de Imagem',
            },
        ),
    ]