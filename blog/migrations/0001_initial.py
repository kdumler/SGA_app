# Generated by Django 2.0.2 on 2018-05-01 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory_Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Curr_date', models.DateTimeField(verbose_name='Current Date')),
                ('Condition', models.CharField(choices=[('NEW', 'NEW'), ('LIKE NEW', 'LIKE NEW'), ('GOOD', 'GOOD'), ('FAIR', 'FAIR'), ('POOR', 'POOR'), ('UNUSABLE', 'UNUSABLE'), ('LOST', 'LOST'), ('LOST', 'LOST'), ('LOST', 'LOST')], max_length=100, verbose_name='Condition')),
                ('Retire_Date', models.DateTimeField(verbose_name='Retire Date')),
                ('Ck_Notes', models.TextField(verbose_name='Item Notes')),
            ],
            options={
                'db_table': 'inventory_check',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag_num', models.CharField(max_length=5, verbose_name='Tag Number')),
                ('NOA_num', models.CharField(max_length=100, verbose_name='Aproval Bill Number')),
                ('Item_name', models.CharField(max_length=100, verbose_name='Item Name')),
                ('Item_des', models.TextField(verbose_name='Item Description')),
                ('Manf_name', models.CharField(max_length=100, verbose_name='Manufaturer Name')),
                ('Model_num', models.CharField(max_length=100, verbose_name='Model Number')),
                ('Ser_num', models.CharField(max_length=100, verbose_name='Serial Number')),
                ('Seller_name', models.CharField(max_length=100, verbose_name='Seller Name')),
                ('Pur_date', models.DateTimeField(verbose_name='Purchase Date')),
                ('Pur_price', models.CharField(max_length=100, verbose_name='Purchase Price')),
                ('Warranty', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, verbose_name='Warranty')),
                ('War_end_date', models.DateTimeField(max_length=100, verbose_name='Warranty End Date')),
                ('Store_local', models.CharField(max_length=40, verbose_name='Storage Location Name')),
                ('Store_add', models.CharField(max_length=40, verbose_name='Storage Location Address')),
                ('Store_room', models.CharField(blank=True, max_length=40, verbose_name='Storage Location Room')),
                ('FOC_cat', models.CharField(choices=[('SEMESTER', 'SEMESTER'), ('1 yr ', '1 yr'), ('2 yr', '2 yr'), ('3 yr', '3 yr'), ('4 yr', '4 yr'), ('5 yr', '5 yr'), ('6 yr', '6 yr')], max_length=100, verbose_name='FOC Replacement Guidline')),
            ],
            options={
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RSO', models.CharField(max_length=40)),
                ('Description', models.TextField()),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Student_Post',
            },
        ),
        migrations.CreateModel(
            name='RSO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RSO_name', models.CharField(max_length=40, verbose_name='RSO Name')),
                ('RSO_prez', models.CharField(max_length=40, verbose_name='RSO President')),
                ('Prez_ph', models.CharField(max_length=12, verbose_name='President Phone Number')),
                ('Prez_email', models.CharField(max_length=40, verbose_name='President Email')),
                ('RSO_advisor', models.CharField(max_length=40, verbose_name='RSO Advisor')),
                ('Advisor_ph', models.CharField(max_length=40, verbose_name='Advisor Phone Number')),
                ('Advisor_email', models.CharField(max_length=40, verbose_name='Advisor Email')),
            ],
            options={
                'db_table': 'RSO',
            },
        ),
        migrations.AddField(
            model_name='inventory_check',
            name='RSO_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.RSO'),
        ),
        migrations.AddField(
            model_name='inventory_check',
            name='Tag_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Item'),
        ),
    ]
