# Generated by Django 3.1.3 on 2020-11-11 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
                ('telephone', models.CharField(max_length=200, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
