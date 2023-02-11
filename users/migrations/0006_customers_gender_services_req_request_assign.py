# Generated by Django 4.0.3 on 2022-06-26 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_mechanic_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='Gender',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Services_req',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_company', models.CharField(max_length=15)),
                ('car_model', models.CharField(max_length=15)),
                ('car_number', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=15)),
                ('area', models.CharField(max_length=15)),
                ('Mobile_Number', models.CharField(max_length=10)),
                ('Fuel', models.CharField(max_length=15, null=True)),
                ('fuel_liter', models.IntegerField(blank=True, null=True)),
                ('Address', models.CharField(max_length=100, null=True)),
                ('pd_date', models.DateField(blank=True, null=True)),
                ('pd_time', models.CharField(max_length=15, null=True)),
                ('pd_service', models.CharField(max_length=100, null=True)),
                ('Status', models.IntegerField(blank=True, default=1)),
                ('Date', models.DateTimeField(auto_now_add=True, null=True)),
                ('Mechanic', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.mechanic')),
                ('Service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.add_service')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customers')),
            ],
        ),
        migrations.CreateModel(
            name='request_assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.IntegerField(blank=True, default=1)),
                ('Date', models.DateTimeField(auto_now_add=True, null=True)),
                ('Mechanic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.mechanic')),
                ('Service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.services_req')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customers')),
            ],
        ),
    ]