# Generated by Django 3.2.6 on 2021-11-21 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0011_alter_post_datecreated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='author',
            name='authorRating',
            field=models.SmallIntegerField(default=0, verbose_name='рейтинг'),
        ),
        migrations.AlterField(
            model_name='author',
            name='authorUsername',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='логин'),
        ),
        migrations.AlterField(
            model_name='author',
            name='avatar',
            field=models.ImageField(upload_to='static/img', verbose_name='аватар'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='some name', max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='subscribers', through='news.CatSub', to=settings.AUTH_USER_MODEL, verbose_name='subscribers'),
        ),
        migrations.AlterField(
            model_name='catsub',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.category', verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='catsub',
            name='subscriber',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='читатель'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentPost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post', verbose_name='корр пост'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='логин'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.SmallIntegerField(default=0, verbose_name='рейтинг'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='news.author', verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categoryType',
            field=models.CharField(choices=[('NWS', 'Новость'), ('ART', 'Статья'), ('RVW', 'Обзор')], default='ART', max_length=3, verbose_name='тип'),
        ),
        migrations.AlterField(
            model_name='post',
            name='dateCreated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='post',
            name='isUpdated',
            field=models.BooleanField(default=False, verbose_name='изменён'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postCategory',
            field=models.ManyToManyField(through='news.PostCategory', to='news.Category', verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.SmallIntegerField(default=0, verbose_name='рейтинг'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default='', verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128, verbose_name='заголовок'),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='categoryThrough',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category', verbose_name='корр_категория'),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='postThrough',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post', verbose_name='корр_пост'),
        ),
    ]
