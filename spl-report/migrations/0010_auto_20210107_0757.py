# Generated by Django 3.0.8 on 2021-01-07 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0009_auto_20210106_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spl_id', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.user_n')),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('par_cat', models.CharField(max_length=50)),
                ('cat_tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_no', models.IntegerField()),
                ('cat_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.questions')),
            ],
        ),
        migrations.RemoveField(
            model_name='answers',
            name='email',
        ),
        migrations.RemoveField(
            model_name='essay',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='gd',
            name='interviewer1',
        ),
        migrations.RemoveField(
            model_name='gd',
            name='interviewer2',
        ),
        migrations.RemoveField(
            model_name='gd',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='pi',
            name='interviewer1',
        ),
        migrations.RemoveField(
            model_name='pi',
            name='interviewer2',
        ),
        migrations.RemoveField(
            model_name='pi',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='pt',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='question',
            name='q_no',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='uid',
        ),
        migrations.DeleteModel(
            name='answers',
        ),
        migrations.DeleteModel(
            name='essay',
        ),
        migrations.DeleteModel(
            name='gd',
        ),
        migrations.DeleteModel(
            name='pi',
        ),
        migrations.DeleteModel(
            name='pt',
        ),
        migrations.DeleteModel(
            name='question',
        ),
        migrations.DeleteModel(
            name='resume',
        ),
        migrations.DeleteModel(
            name='user',
        ),
        migrations.AddField(
            model_name='answer',
            name='q_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.questions'),
        ),
    ]
