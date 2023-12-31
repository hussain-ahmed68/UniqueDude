# Generated by Django 3.1.1 on 2021-05-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20210511_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom',
            name='design_size',
            field=models.CharField(choices=[('large', 'large'), ('medium', 'medium'), ('small', 'small')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='custom',
            name='tshirt_size',
            field=models.CharField(choices=[('s', 's'), ('m', 'm'), ('l', 'l'), ('xl', 'xl'), ('xxl', 'xxl')], max_length=100, null=True),
        ),
    ]
