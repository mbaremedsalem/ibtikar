from django.db import models
from django.utils.text import slugify
# Create your models here.



class Matiere(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title

class Formation(models.Model):
    title = models.CharField(max_length=250)
    matiere1 = models.OneToOneField(Matiere, on_delete=models.CASCADE, related_name='matiere1_formations') 
    matiere2 = models.OneToOneField(Matiere, on_delete=models.CASCADE, related_name='matiere2_formations')  
    matiere3 = models.OneToOneField(Matiere, on_delete=models.CASCADE, related_name='matiere3_formations') 
    matiere4 = models.OneToOneField(Matiere, on_delete=models.CASCADE, related_name='matiere4_formations')  
    matiere5 = models.OneToOneField(Matiere, on_delete=models.CASCADE, related_name='matiere5_formations')  
    nbrmatier = models.CharField(max_length=250)
    description = models.CharField(max_length=250,blank=True)

    def __str__(self):
        return self.title
    

def image_uoload_profile(instance,filname):
    imagename,extention =  filname.split(".")
    return "course/%s.%s"%(instance.id,extention)    

class Course(models.Model):
    title = models.CharField(max_length=250)
    title_ar = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to=image_uoload_profile ,null=True)
    pourcatange = models.FloatField(blank=True, null=True)
    price = models.FloatField()
    pricenet = models.FloatField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)

    slug = models.SlugField(blank=True, null=True)
    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.pricenet = self.price * self.pourcatange
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)


class Apply(models.Model):
   course = models.ForeignKey(Course,related_name='comment_course',on_delete=models.CASCADE)
   comment = models.TextField(max_length=500)
   created_at = models.DateTimeField(auto_now=True)
   def __str__(self):
       return self.comment        