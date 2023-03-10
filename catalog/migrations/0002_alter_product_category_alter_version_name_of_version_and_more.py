# Generated by Django 4.1.6 on 2023-02-12 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(max_length=29, null=True, on_delete=models.SET('None'), to='catalog.category'),
        ),
        migrations.AlterField(
            model_name='version',
            name='name_of_version',
            field=models.CharField(max_length=250, verbose_name='Название версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='version',
            field=models.CharField(max_length=250, verbose_name='Номер версии'),
        ),
    ]
