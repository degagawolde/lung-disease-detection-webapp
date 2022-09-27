# Generated by Django 4.1.1 on 2022-09-27 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('dateOfSubmission', models.DateTimeField(auto_now_add=True)),
                ('diagnosis', models.TextField(default='None', max_length=200)),
                ('confidence', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
            options={
                'ordering': ['-dateOfSubmission'],
            },
        ),
    ]