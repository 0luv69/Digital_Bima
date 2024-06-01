# Generated by Django 5.0.6 on 2024-06-01 04:21

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('registration_num', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hos_name', models.CharField(max_length=100)),
                ('hos_address', models.CharField(max_length=200)),
                ('hos_type', models.CharField(choices=[('gov', 'government'), ('private', 'private')], default='gov', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hospital', models.CharField(choices=[('H1', 'H1'), ('H2', 'H2')], default='H1', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('appoinment_status', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]