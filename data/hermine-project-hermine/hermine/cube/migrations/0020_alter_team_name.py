# Generated by Django 4.1.1 on 2022-10-10 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cube", "0019_licensecuration_alter_usagedecision_decision_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="name",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
