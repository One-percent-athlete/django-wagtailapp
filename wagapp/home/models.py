from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField

from .blocks import ImageText, Quote, List

class HomePage(Page):
    pass

class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    intro = models.TextField(max_length=50)
    body = StreamField([("photo", ImageChooserBlock()),
                        ("Image_with_text", ImageText()),
                        ("h1", blocks.CharBlock()),
                        ("h2", blocks.CharBlock()),
                        ("h3", blocks.CharBlock()),
                        ("h4", blocks.CharBlock()),
                        ("h5", blocks.CharBlock()),
                        ("paragraph", blocks.TextBlock()),
                        ("quote", Quote()),
                        ("link", blocks.URLBlock()),
                        ("list", List()),
                        ])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta: 
        ordering = ['-published']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home:post_detail', args=[str(self.slug)])
