# Generated by Django 3.0.8 on 2021-01-06 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0006_auto_20210106_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='apti_t',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=20)),
                ('q_1', models.IntegerField()),
                ('q_2', models.IntegerField()),
                ('q_3', models.IntegerField()),
                ('q_4', models.IntegerField()),
                ('q_5', models.IntegerField()),
                ('q_6', models.IntegerField()),
                ('q_7', models.IntegerField()),
                ('q_8', models.IntegerField()),
                ('q_9', models.IntegerField()),
                ('q_10', models.IntegerField()),
                ('q_11', models.IntegerField()),
                ('q_12', models.IntegerField()),
                ('q_13', models.IntegerField()),
                ('q_14', models.IntegerField()),
                ('q_15', models.IntegerField()),
                ('q_16', models.IntegerField()),
                ('q_17', models.IntegerField()),
                ('q_18', models.IntegerField()),
                ('q_19', models.IntegerField()),
                ('q_20', models.IntegerField()),
                ('q_21', models.IntegerField()),
                ('q_22', models.IntegerField()),
                ('q_23', models.IntegerField()),
                ('q_24', models.IntegerField()),
                ('q_25', models.IntegerField()),
                ('q_26', models.IntegerField()),
                ('q_27', models.IntegerField()),
                ('q_28', models.IntegerField()),
                ('q_29', models.IntegerField()),
                ('q_30', models.IntegerField()),
                ('q_31', models.IntegerField()),
                ('q_32', models.IntegerField()),
                ('q_33', models.IntegerField()),
                ('q_34', models.IntegerField()),
                ('q_35', models.IntegerField()),
                ('q_36', models.IntegerField()),
                ('q_37', models.IntegerField()),
                ('q_38', models.IntegerField()),
                ('q_39', models.IntegerField()),
                ('q_40', models.IntegerField()),
                ('q_41', models.IntegerField()),
                ('q_42', models.IntegerField()),
                ('q_43', models.IntegerField()),
                ('q_44', models.IntegerField()),
                ('q_45', models.IntegerField()),
                ('q_46', models.IntegerField()),
                ('q_47', models.IntegerField()),
                ('q_48', models.IntegerField()),
                ('q_49', models.IntegerField()),
                ('q_50', models.IntegerField()),
                ('q_51', models.IntegerField()),
                ('q_52', models.IntegerField()),
                ('q_53', models.IntegerField()),
                ('q_54', models.IntegerField()),
                ('q_55', models.IntegerField()),
                ('q_56', models.IntegerField()),
                ('q_57', models.IntegerField()),
                ('q_58', models.IntegerField()),
                ('q_59', models.IntegerField()),
                ('q_60', models.IntegerField()),
                ('q_61', models.IntegerField()),
                ('q_62', models.IntegerField()),
                ('q_63', models.IntegerField()),
                ('q_64', models.IntegerField()),
                ('q_65', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
    ]
