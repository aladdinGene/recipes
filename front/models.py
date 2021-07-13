from django.db import models
import string  # for string constants
import random  # for generating random strings
from django.utils.text import slugify

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField(null=True)
    ingredients = models.TextField(null=True)
    method = models.TextField(null=True)
    prepare_time = models.CharField(max_length=200)
    cook_time = models.CharField(max_length=200)
    uploader = models.IntegerField()
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = self.generate_slug()
        return super().save(*args, **kwargs)

    def generate_slug(self, save_to_obj=False, add_random_suffix=True):
        generated_slug = slugify(self.title)

        # Generate random suffix here.
        random_suffix = ""
        if add_random_suffix:
            random_suffix = ''.join([
                random.choice(string.ascii_letters + string.digits)
                for i in range(5)
            ])
            generated_slug += '-%s' % random_suffix

        if save_to_obj:
            self.slug = generated_slug
            self.save(update_fields=['slug'])
        
        return generated_slug