# Generated by Django 2.1.2 on 2018-10-18 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20181018_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='api.Tweet'),
        ),
    ]
