# Generated by Django 4.1.2 on 2024-03-02 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abadi', '0002_remove_produk_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penyusun',
            name='Lokasi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.lokasi'),
        ),
        migrations.AlterField(
            model_name='transaksigudang',
            name='Lokasi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='abadi.lokasi'),
        ),
    ]
