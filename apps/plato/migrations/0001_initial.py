# Generated by Django 3.0.4 on 2020-03-17 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ingredientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='', max_length=50)),
                ('tipo', models.CharField(default='', max_length=50)),
                ('precio', models.CharField(default='', max_length=20)),
            ],
        ),
    ]