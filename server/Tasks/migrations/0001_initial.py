# Generated by Django 4.1.7 on 2023-04-05 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('property', '0008_leasemodel'),
        ('managers', '0001_initial'),
        ('Vendors', '0001_initial'),
        ('owners', '0004_ownermodel_management'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStatusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_number', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('due_date', models.DateField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('asssigned_vendor', models.ManyToManyField(blank=True, default=None, related_name='Task_vendors', to='Vendors.vendormodel')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_byTask', to='managers.managermodel')),
                ('managers', models.ManyToManyField(blank=True, default=None, related_name='Task_managers', to='managers.managermodel')),
                ('owners', models.ManyToManyField(blank=True, default=None, related_name='Task_owner', to='owners.ownermodel')),
                ('property', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Task_Property', to='property.propertymodel')),
                ('status', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Task_status', to='Tasks.taskstatusmodel')),
            ],
        ),
    ]