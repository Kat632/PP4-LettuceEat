# Generated by Django 3.2 on 2022-04-17 14:59

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_post_comment_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=django_summernote.fields.SummernoteTextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='method',
            field=django_summernote.fields.SummernoteTextField(),
        ),
    ]
