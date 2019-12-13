from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

from filer.fields.image import FilerFileField

# Create your models here.
class Document(models.Model):
    '''Represents a single document entry'''
    title = models.CharField('Title', max_length=120, unique=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                            help_text="The user that posted this article.")
    slug = models.CharField(max_length=120, blank=True, editable=False, help_text="Unique URL path to access this page. Generated by the system.")
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/this-is-my-hair). """
        path_components = {'slug': self.slug}
        return reverse('document-detail-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new page is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Document, self).save(*args, **kwargs)

class FileUpload(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = FilerFileField(null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title