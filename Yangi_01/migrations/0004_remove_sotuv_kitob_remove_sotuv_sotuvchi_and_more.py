# Generated by Django 4.2 on 2023-04-18 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Yangi_01', '0003_kitob_nashriyot_sotuv_sotuvchi_delete_foydalanuvchi_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sotuv',
            name='kitob',
        ),
        migrations.RemoveField(
            model_name='sotuv',
            name='sotuvchi',
        ),
        migrations.DeleteModel(
            name='Kitob',
        ),
        migrations.DeleteModel(
            name='Nashriyot',
        ),
        migrations.DeleteModel(
            name='Sotuv',
        ),
        migrations.DeleteModel(
            name='Sotuvchi',
        ),
    ]
