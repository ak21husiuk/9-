# Generated by Django 4.2 on 2023-05-16 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_alter_article_options_alter_article_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Стаття', 'verbose_name_plural': 'Статті'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='description',
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(help_text='Максимум 250 символів', max_length=250, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='articleimage',
            name='title',
            field=models.CharField(blank=True, help_text='Максимум 250 символів', max_length=250, verbose_name='Заголовок'),
        ),
    ]
