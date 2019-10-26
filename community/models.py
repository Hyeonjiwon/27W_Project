from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField
#from ckeditor.fields import RichTextField
# Create your models here.

COMMUNITY_CATEGORY = [
    ('Art', 'Art'),
    ('Design', 'Design'),
    ('Social Media', 'Social Media'),
]

class Community(models.Model):
    # one to one field
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=100)
    text = RichTextUploadingField()
    #text = models.TextField()

    # many to one field
    #comments = models.ForeignKey(CommunityComment, on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to='community_images/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=COMMUNITY_CATEGORY, default='None') # make category
    created_at = models.DateField(auto_now=True)

    #like = models.IntegerField()  # 미확정
    #unlike = models.IntegerField() # 미확정

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Community.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(Community, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs): 
        # You have to prepare what you need before delete the model 
        storage, path = self.image.storage, self.image.path 
        # Delete the model before the file 
        super(Community, self).delete(*args, **kwargs) 
        # Delete the file after the model 
        storage.delete(path) 


class CommunityComment(models.Model):
    # one to one field
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now=True)