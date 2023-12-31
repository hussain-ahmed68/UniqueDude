# Generated by Django 3.1.1 on 2021-05-10 14:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20210508_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.order'),
        ),
        migrations.CreateModel(
            name='Custom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.ImageField(null=True, upload_to='custom/')),
                ('color', models.CharField(choices=[('Black', 'black'), ('Gray', 'gray'), ('White', 'white'), ('Red', 'red'), ('Blue', 'blue'), ('Pink', 'pink')], max_length=100, null=True)),
                ('size', models.CharField(choices=[('Large', 'large'), ('Medium', 'medium'), ('Small', 'small')], max_length=100, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
            ],
        ),
    ]
