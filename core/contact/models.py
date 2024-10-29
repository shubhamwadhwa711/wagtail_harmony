from django.db import models

# Create your models here.
class ContactCategory(models.Model):
    name = models.CharField(max_length=255)
    #for eg ->  Host an event or other ,# Share History story ,# Develop in Harmony 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact Category'
        verbose_name_plural = 'Contact Categories'




