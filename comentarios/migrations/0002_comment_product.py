# Generated by Django 2.0.6 on 2018-09-10 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20180910_0320'),
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='productos.Product'),
            preserve_default=False,
        ),
    ]
