# Generated by Django 3.1.5 on 2022-10-22 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20221022_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='web',
            field=models.URLField(blank=True, verbose_name='Website Address'),
        ),
    ]
