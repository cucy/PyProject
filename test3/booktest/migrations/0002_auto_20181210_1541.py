# Generated by Django 2.1.3 on 2018-12-10 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='booktest/')),
            ],
        ),
        migrations.AlterField(
            model_name='areainfo',
            name='atitle',
            field=models.CharField(max_length=30, verbose_name='城市'),
        ),
        migrations.AlterModelTable(
            name='areainfo',
            table='AreaInfo',
        ),
    ]