# Generated by Django 3.2 on 2022-08-20 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0004_auto_20220819_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='exame',
            field=models.BooleanField(default=False, verbose_name='Exame?'),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='ingles',
            field=models.BooleanField(default=False, verbose_name='Ingles?'),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='nivel_ingles',
            field=models.CharField(blank=True, max_length=30, verbose_name='Nível de Inglês'),
        ),
    ]
