# Generated by Django 3.2.12 on 2023-02-07 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory', models.CharField(max_length=100)),
                ('brand', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.brand')),
            ],
        ),
    ]
