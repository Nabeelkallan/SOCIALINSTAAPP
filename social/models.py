from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    bio=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to="profile",null=True,blank=True)
    cover_pic=models.ImageField(upload_to="covers",null=True,blank=True)
    dob=models.DateTimeField(null=True)
    phone=models.CharField(max_length=50,null=True,blank=True)
    followings=models.ManyToManyField(User)

    @property
    def friend_requests(self):
        all_users=User.objects.all().exclude(username=self.user)
        my_friends=self.followings.all()
        suggestions=set(all_users)-set(my_friends)
        return suggestions
    
    def followers_count(self):
        all_users=User.objects.all().exclude(username=self.user)
        

class Posts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="posts",null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    lat=models.FloatField(null=True,blank=True)
    long=models.FloatField(null=True,blank=True)
    liked_by=models.ManyToManyField(User,related_name="post")

    @property
    def get_comments(self):
        return Comments.objects.filter(post=self)

    

    # @property
    # def comment_count(self):
    #     return Comments.objects.filter(post=self).count()

    def __str__(self) -> str:
        return self.title


class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    Comments=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)

