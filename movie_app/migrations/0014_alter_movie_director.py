# Generated by Django 4.0.3 on 2022-03-28 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0013_alter_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_app.director'),
        ),
    ]
