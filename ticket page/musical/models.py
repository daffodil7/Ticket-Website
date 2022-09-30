from django.db import models
from django.urls import reverse
from photo.fields import ThumbnailImageField

# Create your models here.
class Musical(models.Model):
    title = models.CharField('TITLE', max_length=30)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    upload_dt = models.DateTimeField('Upload Date', auto_now_add=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="OWNER",blank=True,null=True)

    class Meta:
        ordering = ('title',)
         
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('poster:poster_detail', args=(self.id,))