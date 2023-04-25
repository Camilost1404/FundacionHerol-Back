# Generated by Django 4.1.7 on 2023-04-24 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Persona', '0003_voluntario_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Persona.persona')),
            ],
        ),
    ]