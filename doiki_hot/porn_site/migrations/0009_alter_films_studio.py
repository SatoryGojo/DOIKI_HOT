# Generated by Django 5.0.6 on 2024-08-12 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porn_site', '0008_alter_films_studio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='studio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='studio', to='porn_site.studio'),
        ),
    ]
