# Generated by Django 4.1.3 on 2022-12-06 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('detail', models.CharField(max_length=500)),
                ('price', models.FloatField()),
                ('photo', models.ImageField(upload_to='products')),
                ('category', models.CharField(choices=[('IT', 'IT & Gadget'), ('EL', 'Electronics'), ('FA', 'Fashion')], max_length=2)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
