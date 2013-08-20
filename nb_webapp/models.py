from django.db import models

# Create your models here.

#ContactInfo class
class ContactInfo(models.Model):
    email = models.EmailField()
    facebook_account = models.URLField()
    linkedin_account = models.URLField()
    website = models.URLField()

    def __unicode__(self):
        return self.email


#WorkPlace class
class WorkPlace(models.Model):
    company_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    position = models.CharField(max_length=30)
    start_date = models.DateField()


#BasicInfo
class BasicInfo(models.Model):
    account_type = models.CharField(max_length=1)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_info = models.OneToOneField(ContactInfo)
    #work is different form the db design
    work = models.ForeignKey(WorkPlace)
    about_me = models.CharField(max_length=300)
    ACCESS_RIGHTS = (
        ('PUB', 'Public'),
        ('PRI', 'Private')
    )
    access_rights = models.CharField(max_length=3, choices=ACCESS_RIGHTS)

#UserProfile
class UserProfile(models.Model):
    basic_info = models.OneToOneField(BasicInfo)
    followers = models.ManyToManyField(BasicInfo)
    knowledge_profile = models.OneToOneField(KnowledgeProfile)


#KnowledgProfile
class KnowledgeProfile(models.Model):
    interests = models.CharField(max_length=50)
    num_flowers = models.IntegerField()
    num_posts = models.IntegerField()
    num_tags = models.IntegerField()
    num_followings = models.IntegerField()
    num_followers = models.IntegerField()
    ACCESS_RIGHTS = (
        ('PUB', 'Public'),
        ('PRI', 'Private'),
    )
    access_rights = models.CharField(max_length=3, choices=ACCESS_RIGHTS)
    knowledge_board = models.OneToOneField(KnowledgeBoard)

#KnowledgeBoard
class KnowledgeBoard(models.Model):
    def __unicode__(self):
        return ""

#KnowledgeCard


class KnowledgeCard(models.Model):
    knowledge_board = models.ForeignKey(KnowledgeBoard)
    title = models.CharField(max_length=30)
    #need to verify max chars
    contents = models.CharField(max_length=450)
    picture = models.ImageField()
    video_link = models.URLField()
    source_link = models.URLField()
    CATEGORIES = (
        ('IT', 'Technology'),
        ('ST', 'Startup'),
    )
    category = models.CharField(max_length=2, choices=CATEGORIES)
    TAGS = (
        ('JAVA', 'Java'),
        ('Python', 'Python'),
    )
    tags = models.CharField(max_length=10, choices=TAGS)
    post_date = models.DateField()
    num_thumbs = models.IntegerField()
    num_shares = models.IntegerField()
    num_comments = models.IntegerField()
    ACCESS_RIGHTS = (
        ('PUB', 'Public'),
        ('PRI', 'Private'),
    )
    access_rights = models.CharField(max_length=3, choices=ACCESS_RIGHTS)


#Comments
class Comment(models.Model):
    knowledge_card=models.ForeignKey(KnowledgeCard)
    contents =models.CharField(max_length=100)
    post_date=models.DateField()
    num_upvotes=models.IntegerField()
