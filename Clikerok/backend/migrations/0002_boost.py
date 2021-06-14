# Generated by Django 3.2.3 on 2021-06-14 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=10)),
                ('mainCycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.maincycle')),
            ],
        ),
    ]
