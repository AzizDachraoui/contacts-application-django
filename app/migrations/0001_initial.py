# Generated by Django 3.0.8 on 2020-08-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.IntegerField()),
                ('info', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]