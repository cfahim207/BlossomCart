# Generated by Django 5.0.6 on 2024-08-28 05:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coustomer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coustomer',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.CreateModel(
            name='Deposite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('coustomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coustomer.coustomer')),
            ],
        ),
    ]
