# Generated by Django 2.0 on 2020-10-02 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('otp', models.BigIntegerField()),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]
