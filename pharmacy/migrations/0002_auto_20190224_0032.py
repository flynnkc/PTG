# Generated by Django 2.1.7 on 2019-02-24 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disburse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Receive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='drug',
            name='location',
        ),
        migrations.AddField(
            model_name='drug',
            name='location',
            field=models.ManyToManyField(to='pharmacy.Location'),
        ),
    ]