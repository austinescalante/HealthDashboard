# Generated by Django 3.1.4 on 2020-12-22 23:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('DoctorID', models.IntegerField(max_length=9, primary_key=True, serialize=False)),
                ('Qualifications', models.TextField(max_length=100)),
                ('Speciality', models.TextField(max_length=100)),
                ('DOB', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_VisitHistory',
            fields=[
                ('VID', models.IntegerField(primary_key=True, serialize=False)),
                ('DID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeID', models.IntegerField(max_length=9, primary_key=True, serialize=False)),
                ('EmployeeSSN', models.CharField(max_length=30)),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Address', models.TextField(max_length=200)),
                ('Sex', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('NurseID', models.IntegerField(max_length=9, primary_key=True, serialize=False)),
                ('Qualifications', models.TextField(max_length=100)),
                ('Speciality', models.TextField(max_length=100)),
                ('DOB', models.DateField(default=django.utils.timezone.now)),
                ('EID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Nurse_VisitHistory',
            fields=[
                ('DID', models.IntegerField(primary_key=True, serialize=False)),
                ('NID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.nurse')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientID', models.IntegerField(max_length=9)),
                ('PatientSSN', models.CharField(max_length=30)),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Address', models.TextField(max_length=200)),
                ('Sex', models.CharField(max_length=1)),
                ('DOB', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Bill',
            fields=[
                ('BillID', models.IntegerField(primary_key=True, serialize=False)),
                ('BillDate', models.DateField(default=django.utils.timezone.now)),
                ('TotalCost', models.CharField(max_length=20)),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_VisitHistory',
            fields=[
                ('VisitedID', models.IntegerField(primary_key=True, serialize=False)),
                ('PID', models.IntegerField()),
                ('VisitDate', models.DateField(default=django.utils.timezone.now)),
                ('DID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='doctor',
            name='EID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employee'),
        ),
    ]
