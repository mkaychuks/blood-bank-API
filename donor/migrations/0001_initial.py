# Generated by Django 2.2.9 on 2020-01-20 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=21, region=None, unique=True)),
                ('address', models.TextField()),
                ('age', models.PositiveIntegerField()),
                ('blood_group', models.CharField(choices=[('A Positive', 'A+'), ('A Negative', 'A-'), ('AB Positive', 'AB+'), ('AB Negative', 'AB-'), ('B Positive', 'B+'), ('B Negative', 'B-'), ('O Positive', 'O+'), ('O Negative', 'O-')], max_length=21)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]