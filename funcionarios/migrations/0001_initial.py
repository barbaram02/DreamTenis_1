# Generated by Django 4.2.4 on 2023-09-05 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tema', models.CharField(max_length=30)),
                ('foto', models.ImageField(upload_to='')),
                ('conteudo', models.TextField(blank=True, null=True)),
            ],
        ),
    ]