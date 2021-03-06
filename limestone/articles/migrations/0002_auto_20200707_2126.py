# Generated by Django 3.0.8 on 2020-07-07 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_at', 'updated_at']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comment', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.TextField(max_length=250),
        ),
    ]
