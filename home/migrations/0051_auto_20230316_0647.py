# Generated by Django 3.1.14 on 2023-03-16 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_auto_20230213_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='global_matomo_site_id',
            field=models.IntegerField(blank=True, help_text='Global Matomo Site ID to be used to view analytics on this site only', null=True, verbose_name='Global Matomo Site ID'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='local_matomo_site_id',
            field=models.IntegerField(blank=True, help_text='Local Matomo Site ID to be used to view analytics on this site only', null=True, verbose_name='Local Matomo Site ID'),
        ),
        migrations.AlterField(
            model_name='manifestsettings',
            name='language',
            field=models.CharField(choices=[('ar', 'Arabic'), ('bn', 'Bengali'), ('ny', 'Chichewa'), ('prs', 'Dari'), ('en', 'English'), ('fr', 'French'), ('hi', 'Hindi'), ('id', 'Indonesian'), ('kaa', 'Karakalpak'), ('km', 'Khmer'), ('rw', 'Kinyarwanda'), ('rn', 'Kirundi'), ('ku', 'Kurdish'), ('mg', 'Malagasy'), ('ne', 'Nepali'), ('nr', 'Ndebele'), ('ps', 'Pashto'), ('pt', 'Portuguese'), ('qu', 'Quechua'), ('ru', 'Russian'), ('sn', 'Shona'), ('si', 'Sinhala'), ('es', 'Spanish'), ('sw', 'Swahili'), ('tg', 'Tajik'), ('ta', 'Tamil'), ('ti', 'Tigrinya'), ('tr', 'Turkish'), ('uk', 'Ukraine'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('zu', 'Zulu'), ('xy', 'Testing')], default='en', help_text='Choose language', max_length=3, verbose_name='Language'),
        ),
    ]
