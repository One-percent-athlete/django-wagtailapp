# Generated by Django 5.0.7 on 2024-07-30 03:43

import django.core.validators
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_post_image_post_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=wagtail.fields.StreamField([('photo', wagtail.images.blocks.ImageChooserBlock()), ('Image_with_text', wagtail.blocks.StructBlock([('reverse', wagtail.blocks.BooleanBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('h1', wagtail.blocks.CharBlock()), ('h2', wagtail.blocks.CharBlock()), ('h3', wagtail.blocks.CharBlock()), ('h4', wagtail.blocks.CharBlock()), ('h5', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.TextBlock()), ('quote', wagtail.blocks.StructBlock([('qupted_by', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.CharBlock())])), ('link', wagtail.blocks.URLBlock()), ('list', wagtail.blocks.StructBlock([('ordered', wagtail.blocks.BooleanBlock(required=False)), ('text', wagtail.blocks.CharBlock())]))]),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('text', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='home.post')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
