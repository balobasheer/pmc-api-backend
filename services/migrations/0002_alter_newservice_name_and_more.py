# Generated by Django 5.0.3 on 2024-04-15 07:11

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='newservice',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newservice',
            name='service_picture',
            field=models.FileField(upload_to='Service/images', validators=[django.core.validators.FileExtensionValidator(['pdf', 'jpeg', 'jpg', 'png'])]),
        ),
        migrations.AlterField(
            model_name='newservice',
            name='service_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.service'),
        ),
        migrations.AlterField(
            model_name='newservice',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('in progress', 'in progress'), ('done', 'done')], default='awaiting...', max_length=50),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]
