# Generated by Django 3.2.2 on 2021-05-11 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0002_auto_20210511_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='deposit',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='term',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True),
        ),
    ]
