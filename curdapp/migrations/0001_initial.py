# Generated by Django 3.0.4 on 2020-03-25 11:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.AutoField(auto_created=True, serialize=False, verbose_name='name')),
                ('email', models.AutoField(auto_created=True, serialize=False, verbose_name='email')),
                ('contact', models.AutoField(auto_created=True, serialize=False, verbose_name='contact')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
