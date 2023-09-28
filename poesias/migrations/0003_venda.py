# Generated by Django 4.2.4 on 2023-09-26 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poesias', '0002_poesia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_venda', models.DateField(auto_now=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='poesias.livro')),
                ('poesia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='poesias.poesia')),
            ],
        ),
    ]
