# Generated by Django 3.1.2 on 2021-03-17 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caruserfirstname', models.CharField(max_length=255)),
                ('caruserlastname', models.CharField(max_length=255)),
                ('caruseremail', models.CharField(max_length=255)),
                ('carusermobile', models.CharField(max_length=255)),
                ('caruseraddress', models.TextField(max_length=500)),
                ('carname', models.CharField(max_length=255)),
                ('carmodel', models.CharField(max_length=255)),
                ('carnumber', models.CharField(max_length=255)),
                ('carlaunchdate', models.CharField(max_length=255)),
                ('carimagefront', models.ImageField(upload_to='myappointment1')),
                ('carimageright', models.ImageField(upload_to='myappointment1')),
                ('carimageleft', models.ImageField(upload_to='myappointment1')),
                ('carimageback', models.ImageField(upload_to='myappointment1')),
                ('date', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='appointment2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caruserfirstname', models.CharField(max_length=255)),
                ('caruserlastname', models.CharField(max_length=255)),
                ('caruseremail', models.CharField(max_length=255)),
                ('carusermobile', models.CharField(max_length=255)),
                ('caruseraddress', models.TextField(max_length=500)),
                ('carname', models.CharField(max_length=255)),
                ('carmodel', models.CharField(max_length=255)),
                ('carnumber', models.CharField(max_length=255)),
                ('carlaunchdate', models.CharField(max_length=255)),
                ('carimagefront', models.ImageField(upload_to='myappointment2')),
                ('carimageright', models.ImageField(upload_to='myappointment2')),
                ('carimageleft', models.ImageField(upload_to='myappointment2')),
                ('carimageback', models.ImageField(upload_to='myappointment2')),
                ('date', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='time1',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='time2',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='time3',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='carimageback',
            field=models.ImageField(upload_to='myappointment'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='carimagefront',
            field=models.ImageField(upload_to='myappointment'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='carimageleft',
            field=models.ImageField(upload_to='myappointment'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='carimageright',
            field=models.ImageField(upload_to='myappointment'),
        ),
        migrations.AlterField(
            model_name='usedcar',
            name='carimageback',
            field=models.ImageField(upload_to='myusedcar'),
        ),
        migrations.AlterField(
            model_name='usedcar',
            name='carimagefront',
            field=models.ImageField(upload_to='myusedcar'),
        ),
        migrations.AlterField(
            model_name='usedcar',
            name='carimageleft',
            field=models.ImageField(upload_to='myusedcar'),
        ),
        migrations.AlterField(
            model_name='usedcar',
            name='carimageright',
            field=models.ImageField(upload_to='myusedcar'),
        ),
    ]
