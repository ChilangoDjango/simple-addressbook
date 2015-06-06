# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Direccion', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name=b'Correo', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Apellidos', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.IntegerField(verbose_name=b'Numero'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='type_number',
            field=models.IntegerField(verbose_name=b'Tipo', choices=[(1, b'Movil'), (2, b'Casa'), (3, b'Trabajo'), (4, b'Fax')]),
        ),
        migrations.AlterField(
            model_name='group',
            name='contact',
            field=models.ManyToManyField(to='contacts.Contact', verbose_name=b'Contactos'),
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.CharField(max_length=255, verbose_name=b'Descripcion'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'Nombre'),
        ),
    ]
