# Generated by Django 4.2.16 on 2025-01-07 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proscheme_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductScheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100, unique=True)),
                ('investment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('days', models.IntegerField()),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='trans',
            name='trans_number',
        ),
        migrations.DeleteModel(
            name='Items',
        ),
        migrations.DeleteModel(
            name='Trans',
        ),
    ]
