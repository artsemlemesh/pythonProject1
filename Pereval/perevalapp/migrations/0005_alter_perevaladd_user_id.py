# Generated by Django 4.2.7 on 2023-12-06 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("perevalapp", "0004_alter_perevaladd_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="perevaladd",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="perevalapp.users"
            ),
        ),
    ]