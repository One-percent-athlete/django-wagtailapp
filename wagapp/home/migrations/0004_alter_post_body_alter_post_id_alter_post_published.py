# Generated by Django 5.0.7 on 2024-07-27 20:55

import django.utils.timezone
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=wagtail.fields.StreamField([('photo', wagtail.images.blocks.ImageChooserBlock()), ('Image_with_text', wagtail.blocks.StructBlock([('reverse', wagtail.blocks.BooleanBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('h1', wagtail.blocks.CharBlock()), ('h2', wagtail.blocks.CharBlock()), ('h3', wagtail.blocks.CharBlock()), ('h4', wagtail.blocks.CharBlock()), ('h5', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.TextBlock()), ('quote', wagtail.blocks.StructBlock([('qupted_by', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.CharBlock())])), ('link', wagtail.blocks.URLBlock()), ('list', wagtail.blocks.StructBlock([('ordered', wagtail.blocks.BooleanBlock()), ('text', wagtail.blocks.CharBlock())]))]),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
