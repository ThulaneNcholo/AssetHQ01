# Generated by Django 4.1.7 on 2023-04-08 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applications', '0001_initial'),
        ('property', '0008_leasemodel'),
        ('managers', '0001_initial'),
        ('owners', '0004_ownermodel_management'),
        ('Vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceStatusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PriorityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('assigned_manager', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_manager', to='managers.managermodel')),
                ('owners', models.ManyToManyField(blank=True, default=None, related_name='maintenance_owner', to='owners.ownermodel')),
                ('priority', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_priority', to='Requests.prioritymodel')),
                ('property', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Property_maintenance', to='property.propertymodel')),
                ('status', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_status', to='Requests.maintenancestatusmodel')),
                ('tenant', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_tenant', to='applications.applicationmodel')),
                ('vendor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_vendor', to='Vendors.vendormodel')),
            ],
        ),
    ]
