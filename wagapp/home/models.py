from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField
from wagtail.snippets.models import register_snippet

from .blocks import ImageText, Quote, List

class HomePage(Page):
    pass

@register_snippet
class Categories(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=80)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

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
    tags = TaggableManager(blank=True)
    category = models.ForeignKey(Categories, blank=True, null=True, on_delete=models.CASCADE, related_name='category')

    class Meta: 
        ordering = ['-published']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home:post_detail', args=[str(self.slug)])
    
    def get_average_rating(self):
        average = 0
        if self.reviews.count() > 0:
            total = sum([review.rating for review in self.reviews.all()])
            average = total/self.reviews.count()
        return round(average, 1)
    
    def get_review_count(self):
        return self.reviews.count()

class Review(models.Model):
    post = models.ForeignKey(Post, related_name='reviews', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created',)

    def get_star_count(self):
        return range(self.rating)
    
