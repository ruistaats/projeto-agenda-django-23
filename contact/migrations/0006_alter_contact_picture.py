# Generated by Django 4.2.7 on 2023-11-14 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_contact_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='picture',
            field=models.ImageField(default='pictures/fotopadrao.jepg', upload_to='pictures/%Y%m'),
        ),
    ]
