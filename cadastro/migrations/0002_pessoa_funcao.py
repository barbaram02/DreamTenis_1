# Generated by Django 4.2.4 on 2023-09-05 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='funcao',
            field=models.TextField(default=5, max_length=50),
            preserve_default=False,
        ),
    ]
