# Generated by Django 4.1.4 on 2022-12-23 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('c_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('m_id', models.PositiveIntegerField(unique=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StoreOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(blank=True, null=True)),
                ('bill_amount', models.PositiveIntegerField(blank=True, null=True)),
                ('cafe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='stores.cafe')),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managerid+', to='stores.cafe', to_field='m_id')),
            ],
        ),
    ]
