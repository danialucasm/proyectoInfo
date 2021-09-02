# Generated by Django 2.2.5 on 2021-08-29 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_juego', '0005_auto_20210828_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elegirrespuesta',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='preguntasrespondidas',
            name='correcta',
            field=models.BooleanField(default=True, verbose_name='¿Es esta la respuesta correcta?'),
        ),
        migrations.AlterField(
            model_name='preguntasrespondidas',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='triviausuario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]