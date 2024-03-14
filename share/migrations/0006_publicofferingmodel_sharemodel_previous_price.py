# Generated by Django 5.0.2 on 2024-03-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0005_alter_slotmodel_options_slotmodel_action_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicOfferingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('details', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='sharemodel',
            name='previous_price',
            field=models.CharField(default='0', max_length=50),
        ),
    ]