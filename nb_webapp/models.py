from django.db import models

# Create your models here.

# BasicInfo Table
class BasicInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    account_email= models.EmailField()
    account_type = models.CharField(max_length=1)
    password = models.CharField(max_length=100)
    linkedin_member_id=models.CharField(max_length=20)
    facebook_member_id=models.CharField(max_length=20)
    website = models.URLField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    #work is different form the db design
    about_me = models.CharField(max_length=300)
    ACCESS_RIGHTS = (
        ('PUB', 'Public'),
        ('PRI', 'Private')
    )
    access_rights = models.CharField(max_length=3, choices=ACCESS_RIGHTS)

# WorkInfo Table
class WorkInfo(models.Model):
    basic_info = models.ForeignKey(BasicInfo)
    company_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    position = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()

# KnowledgeProfile Table
class KnowledgeProfile(models.Model):
    basic_info = models.ForeignKey(BasicInfo)
    interests = models.CharField(max_length=50)
    num_flowers = models.PositiveIntegerField()
    num_posts = models.PositiveIntegerField()
    num_tags = models.PositiveIntegerField()
    num_thumbs = models.PositiveIntegerField()
    num_followings = models.PositiveIntegerField()
    num_followers = models.PositiveIntegerField()
    ACCESS_RIGHTS = (
        ('PUB', 'Public'),
        ('PRI', 'Private'),
    )
    access_rights = models.CharField(max_length=3, choices=ACCESS_RIGHTS)
    # knowledge_board = models.OneToOneField(KnowledgeBoard)

# KnowledgeBoard
# class KnowledgeBoard(models.Model):
#    def __unicode__(self):
#        return ""

# KnowledgeCard Table
class KnowledgeCard(models.Model):
    # knowledge_card = models.ForeignKey(KnowledgeCard)
    card_id = models.AutoField(primary_key=True)
    basic_info = models.ForeignKey(BasicInfo)
    title = models.CharField(max_length=30)
    #need to verify max chars
    contents = models.CharField(max_length=150)
    # picture = models.ImageField(upload_to='/Users/jinguangzhou/git/NoahBoard/images')
    video_link = models.URLField()
    source_link = models.URLField()
    CATEGORIES = (
        ('MI', 'Mobile & Internet industry'),
        ('BE', 'Business & Entrepreneur'),
        ('LM', 'Leadership & Management'),
        ('MA', 'Marketing & Advertising'),
        ('CS', 'Consulting & Strategy'),
        ('SD', 'Sales & Distribution'),
        ('CT', 'Computer & Technology'),
        ('DU', 'Design & User experience'),
        ('NS', 'NGO & Social enterprise'),
    )
    category = models.CharField(max_length=2, choices=CATEGORIES)
    #TAGS = (
    #    ('JAVA', 'Java'),
    #    ('Python', 'Python'),
    #)
    tags = models.CharField(max_length=50)
    post_date = models.DateField()
    num_thumbs = models.PositiveIntegerField()
    num_reposts = models.PositiveIntegerField()
    num_shares = models.PositiveIntegerField()
    num_comments = models.PositiveIntegerField()
    ACCESS_RIGHTS = (
        ('PUB', 'Public'),
        ('PRI', 'Private'),
    )
    access_rights = models.CharField(max_length=3, choices=ACCESS_RIGHTS)

#UserProfile
#class UserProfile(models.Model):
#    basic_info = models.OneToOneField(BasicInfo)
#    followers = models.ManyToManyField(BasicInfo,related_name="followers_basic_info")
#    knowledge_profile = models.OneToOneField(KnowledgeProfile)

# CommentInfo Table
class CommentInfo(models.Model):
    knowledge_card = models.ForeignKey(KnowledgeCard)
    comment_index = models.PositiveIntegerField()
    commentator_id = models.ForeignKey(BasicInfo)
    contents = models.CharField(max_length=100)
    post_date = models.DateField()
    num_upvotes = models.PositiveIntegerField()

# FollowerInfo Table
class FollowerInfo(models.Model):
    basic_info = models.ForeignKey(BasicInfo, related_name='+')
    follower_info = models.ForeignKey(BasicInfo, related_name='+')

# FollowingInfo Table
class FollowingInfo(models.Model):
    basic_info = models.ForeignKey(BasicInfo, related_name='+')
    following_info = models.ForeignKey(BasicInfo, related_name='+')

# RepostInfo Table
class RepostInfo(models.Model):
    knowledge_card = models.ForeignKey('KnowledgeCard')
    sharer_info = models.ForeignKey('BasicInfo')
    share_type = models.BooleanField() # True: reposts, False: share
