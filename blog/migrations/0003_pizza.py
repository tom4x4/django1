# Generated by Django 2.2.5 on 2020-02-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30, verbose_name='Pizza')),
                ('opis', models.TextField(blank=True, help_text='Opis Pizzy')),
                ('rozmiar', models.CharField(choices=[('L', 'duża'), ('M', 'średnia'), ('S', 'mała')], default='L', max_length=1)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data', models.DateField(auto_now_add=True, verbose_name='dodano')),
            ],
        ),
    ]