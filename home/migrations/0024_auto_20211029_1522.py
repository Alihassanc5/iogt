# Generated by Django 3.1.13 on 2021-10-29 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20211029_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iogtflatmenuitem',
            name='background_color',
            field=models.CharField(blank=True, help_text='The background color of the flat menu item on Desktop + Mobile', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='iogtflatmenuitem',
            name='font_color',
            field=models.CharField(blank=True, help_text='The font color of the flat menu item on Desktop + Mobile', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='themesettings',
            name='navbar_background_color',
            field=models.CharField(blank=True, default='#0094F4', help_text='The background color of the navbar as a HEX code', max_length=8, null=True),
        ),

    ]
