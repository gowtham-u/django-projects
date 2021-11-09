# Generated by Django 3.2.9 on 2021-11-05 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.IntegerField()),
                ('heading', models.CharField(max_length=255)),
                ('definition', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related_text', models.CharField(max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aptitude.question')),
            ],
        ),
    ]
