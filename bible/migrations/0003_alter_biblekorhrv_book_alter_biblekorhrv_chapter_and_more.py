# Generated by Django 4.0.3 on 2022-03-29 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0002_alter_biblekorhrv_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biblekorhrv',
            name='book',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='biblekorhrv',
            name='chapter',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='biblekorhrv',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='biblekorhrv',
            name='verse',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
