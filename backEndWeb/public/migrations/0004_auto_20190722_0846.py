# Generated by Django 2.2.3 on 2019-07-22 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_auto_20190722_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member1model',
            name='state',
            field=models.CharField(choices=[('Y', '正常'), ('F', '冻结')], default='Y', max_length=3),
        ),
    ]