# Generated by Django 3.1.2 on 2021-04-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20210317_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='testemonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userfirstname', models.CharField(max_length=255)),
                ('userlastname', models.CharField(max_length=255)),
                ('useremail', models.CharField(max_length=255)),
                ('usermobile', models.CharField(max_length=255)),
                ('review', models.TextField(max_length=500)),
                ('imagefront', models.ImageField(upload_to='testemonial')),
            ],
        ),
    ]
