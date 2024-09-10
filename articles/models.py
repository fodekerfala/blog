from django.db import models
from django.contrib.auth.models import User


class Articles(models.Model):
    title = models.CharField(max_length=100, blank=False,verbose_name='Title')
    sumary = models.CharField(max_length=250,blank=True,verbose_name='Sumary')
    content = models.TextField(blank=False,verbose_name='Content')
    categorie = models.ForeignKey('Categories',on_delete=models.PROTECT)
    date_pub = models.DateField(verbose_name='Publication Date')
    publiche = models.BooleanField(default=False,verbose_name='Publish')
    imagearticle = models.ImageField(upload_to='article_image',null=True,blank=True, verbose_name='Select Your Image')
    autor = models.ForeignKey(User,on_delete=models.PROTECT)
    def __str__(self):
        return self.title
    
class Categories(models.Model):
    title = models.CharField(max_length=100,verbose_name='Title')
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    article = models.ForeignKey(Articles,on_delete=models.CASCADE)
    date_comment = models.DateField(auto_now_add=True)