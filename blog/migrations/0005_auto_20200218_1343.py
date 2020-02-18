# Generated by Django 2.2.5 on 2020-02-18 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200218_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizza',
            options={'verbose_name_plural': 'pizzunie'},
        ),
        migrations.AlterField(
            model_name='pizza',
            name='autor',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Skladnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30, verbose_name='składnik')),
                ('jarski', models.BooleanField(default=False, help_text='Zaznacz, jeżeli składnik jest odpowiedni dla wegetarian.', verbose_name='jarski ?')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skladniki', to='blog.Pizza')),
            ],
        ),
    ]
