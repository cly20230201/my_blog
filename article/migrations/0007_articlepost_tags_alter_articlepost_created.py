# Generated by Django 4.2.9 on 2024-01-09 02:27

import datetime
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):
    dependencies = [
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
        ("article", "0006_articlecolumn_alter_articlepost_created_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="articlepost",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="articlepost",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 9, 2, 27, 33, 360220, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
