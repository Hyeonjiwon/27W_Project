from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
# Create your models here.

COMMUNITY_CATEGORY = [
    ('Art', 'Art'),
    ('Design', 'Design'),
    ('Social Media', 'Social Media'),
]

class Community(models.Model):
    # one to one field
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100)
    text = RichTextField()

    # many to one field
    #comments = models.ForeignKey(CommunityComment, on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to='community_images/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=COMMUNITY_CATEGORY, default='None') # make category
    created_at = models.DateField(auto_now=True)

    #like = models.IntegerField()  # 미확정
    #unlike = models.IntegerField() # 미확정

    def __str__(self):
        return self.title

    def delete(self, *args, **kargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(Community, self).delete(*args, **kargs)


class CommunityComment(models.Model):
    # one to one field
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now=True)