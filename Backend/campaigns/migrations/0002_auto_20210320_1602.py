# Generated by Django 3.0.5 on 2021-03-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='backers',
            field=models.CharField(blank=True, default='0', max_length=100),
        ),
    ]
