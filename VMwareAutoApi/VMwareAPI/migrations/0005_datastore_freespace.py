# Generated by Django 2.1.5 on 2019-02-28 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VMwareAPI', '0004_datastore'),
    ]

    operations = [
        migrations.AddField(
            model_name='datastore',
            name='freespace',
            field=models.IntegerField(null=True),
        ),
    ]
