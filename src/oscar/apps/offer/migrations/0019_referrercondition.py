# Generated by Django 2.2.13 on 2020-08-26 06:28

import oscar.apps.offer.conditions
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0018_create_refferer_condition'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferrerCondition',
            fields=[
                ('condition_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='offer.Condition')),
            ],
            options={
                'verbose_name': 'Condition',
                'verbose_name_plural': 'Conditions',
                'abstract': False,
            },
            bases=(oscar.apps.offer.conditions.CustomConditionMixin, 'offer.condition'),
        ),
    ]