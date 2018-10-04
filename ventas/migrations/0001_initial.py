# Generated by Django 2.0.6 on 2018-09-09 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('products', models.ManyToManyField(blank=True, null=True, to='productos.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bag', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='ventas.Bag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sells', to='usuarios.UDUser')),
            ],
        ),
    ]
