# Generated by Django 3.2.6 on 2021-11-21 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20211121_1528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'автор', 'verbose_name_plural': 'автор'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='catsub',
            options={'verbose_name': 'подписка', 'verbose_name_plural': 'подписки'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'комментарий', 'verbose_name_plural': 'комментарии'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'пост', 'verbose_name_plural': 'посты'},
        ),
        migrations.AlterModelOptions(
            name='postcategory',
            options={'verbose_name': 'категория поста', 'verbose_name_plural': 'категории постов'},
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(help_text='категория', max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(help_text='категория', max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentPost_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.post', verbose_name='корр_пост'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentPost_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.post', verbose_name='корр_пост'),
        ),
        migrations.AddField(
            model_name='comment',
            name='text_en',
            field=models.TextField(null=True, verbose_name='текст'),
        ),
        migrations.AddField(
            model_name='comment',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='текст'),
        ),
        migrations.AddField(
            model_name='post',
            name='text_en',
            field=models.TextField(default='', null=True, verbose_name='текст'),
        ),
        migrations.AddField(
            model_name='post',
            name='text_ru',
            field=models.TextField(default='', null=True, verbose_name='текст'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=128, null=True, verbose_name='заголовок'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='заголовок'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='категория', max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentPost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post', verbose_name='корр_пост'),
        ),
    ]