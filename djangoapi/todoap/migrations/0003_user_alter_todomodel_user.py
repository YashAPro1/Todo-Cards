# Generated by Django 4.1.3 on 2023-08-01 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoap', '0002_alter_todomodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=35)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todoap.user'),
        ),
    ]
