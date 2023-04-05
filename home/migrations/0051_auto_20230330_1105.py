# Generated by Django 3.1.14 on 2023-03-30 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_auto_20230213_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manifestsettings',
            name='language',
            field=models.CharField(choices=[('ar', 'Arabic'), ('bn', 'Bengali'), ('ny', 'Chichewa'), ('prs', 'Dari'), ('en', 'English'), ('fa', 'Farsi'), ('fr', 'French'), ('hi', 'Hindi'), ('id', 'Indonesian'), ('kaa', 'Karakalpak'), ('km', 'Khmer'), ('rw', 'Kinyarwanda'), ('rn', 'Kirundi'), ('ku', 'Kurdish'), ('mg', 'Malagasy'), ('ne', 'Nepali'), ('nr', 'Ndebele'), ('ps', 'Pashto'), ('pt', 'Portuguese'), ('qu', 'Quechua'), ('ru', 'Russian'), ('sn', 'Shona'), ('si', 'Sinhala'), ('es', 'Spanish'), ('sw', 'Swahili'), ('tg', 'Tajik'), ('ta', 'Tamil'), ('ti', 'Tigrinya'), ('tr', 'Turkish'), ('uk', 'Ukraine'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('zu', 'Zulu'), ('xy', 'Testing')], default='en', help_text='Choose language', max_length=3, verbose_name='Language'),
        ),
    ]
