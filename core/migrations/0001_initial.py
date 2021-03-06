# Generated by Django 2.0.4 on 2018-04-15 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backpack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('day', models.IntegerField(default=0)),
                ('cash', models.IntegerField(default=2000)),
                ('debt', models.IntegerField(default=5500)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price_min', models.IntegerField()),
                ('price_max', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('backpack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Backpack')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Item')),
            ],
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Game')),
                ('items', models.ManyToManyField(through='core.ItemPrice', to='core.Item')),
            ],
        ),
        migrations.AddField(
            model_name='itemprice',
            name='pricelist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PriceList'),
        ),
        migrations.AddField(
            model_name='backpack',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Game'),
        ),
        migrations.AddField(
            model_name='backpack',
            name='items',
            field=models.ManyToManyField(through='core.ItemQuantity', to='core.Item'),
        ),
        migrations.AlterUniqueTogether(
            name='itemquantity',
            unique_together={('item', 'backpack')},
        ),
        migrations.AlterUniqueTogether(
            name='itemprice',
            unique_together={('item', 'pricelist')},
        ),
    ]
