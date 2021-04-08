# Generated by Django 3.0.2 on 2021-04-08 06:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fields', models.CharField(max_length=50, verbose_name='分野')),
            ],
        ),
        migrations.AlterModelOptions(
            name='subjectmodel',
            options={'verbose_name': '科目カテゴリー'},
        ),
        migrations.AlterModelOptions(
            name='todomodel',
            options={'verbose_name': '医薬品データベース', 'verbose_name_plural': '医薬品データベース'},
        ),
        migrations.AddField(
            model_name='todomodel',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='最終更新日'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todomodel',
            name='relation',
            field=models.ManyToManyField(blank=True, null=True, related_name='_todomodel_relation_+', to='todo.TodoModel', verbose_name='関連分野'),
        ),
        migrations.AddField(
            model_name='todomodel',
            name='field',
            field=models.ManyToManyField(to='todo.Field', verbose_name='分野'),
        ),
    ]
