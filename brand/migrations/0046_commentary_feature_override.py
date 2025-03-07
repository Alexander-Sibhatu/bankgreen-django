# Generated by Django 5.0.6 on 2024-10-01 22:25

import brand.models.commentary
import yamlfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("brand", "0045_commentary_feature_json_and_more")]

    operations = [
        migrations.AddField(
            model_name="commentary",
            name="feature_override",
            field=yamlfield.fields.YAMLField(
                blank=True,
                default=dict,
                help_text="Provide harvest features in yaml format with valid keys",
                validators=[],
                verbose_name="Update Feature (Yaml)",
            ),
        )
    ]
