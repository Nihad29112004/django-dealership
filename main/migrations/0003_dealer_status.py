# Generated by Django 5.2.3 on 2025-06-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_dealer'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='status',
            field=models.CharField(choices=[('active', 'Aktif'), ('inactive', 'Pasif')], default='active', max_length=20),
        ),
    ]
