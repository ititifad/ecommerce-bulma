from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    image = models.ImageField(upload_to='uploads/')
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural='Categories'
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_list_by_category',
                       args=[self.slug])
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(db_index=True, max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    #description = models.TextField()
    description = RichTextField(blank=True, null=True)
    product_detail = RichTextField(blank=True, null=True)
    brand = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.IntegerField(default=1)
    image = models.ImageField(upload_to='uploads/')
    available = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural='Products'
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.id, self.slug])