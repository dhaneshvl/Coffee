# Generated by Django 3.1.5 on 2021-03-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Address', models.CharField(max_length=100)),
                ('Phone', models.IntegerField(max_length=10)),
            ],
        ),
    ]