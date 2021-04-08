from django.db import models

# Create your models here.
class interviewer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
class pyt(models.Model):
    email=models.CharField(primary_key=True,max_length=30)
    personality=models.CharField(max_length=10)
    e_score=models.IntegerField()
    n_score=models.IntegerField()
    f_score=models.IntegerField()
    j_score=models.IntegerField()
    name=models.CharField(max_length=30)
class user_n(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(primary_key=True,max_length=50)
    dept = models.CharField(max_length=20)
    spl_b=models.IntegerField()
    isadmin = models.BooleanField()
class aptitude(models.Model):
    email=models.ForeignKey('user_n',on_delete=models.CASCADE)
    total=models.IntegerField()
    timespent=models.IntegerField()
class category(models.Model):
    category=models.CharField(max_length=50)
    par_cat=models.CharField(max_length=50)
    cat_tag=models.CharField(max_length=50)
class question(models.Model):
    cat_tag=models.ForeignKey('category',on_delete=models.CASCADE)
    q_no=models.IntegerField()
class answers(models.Model):
    spl_id=models.IntegerField()
    q_no=models.ForeignKey('question',on_delete=models.CASCADE)
    marks=models.IntegerField()
    email=models.ForeignKey('user_n',on_delete=models.CASCADE)
class gds(models.Model):
    email=models.ForeignKey('user_n',on_delete=models.CASCADE)
    spl_id=models.IntegerField()
    topic=models.CharField(max_length=100)
    analysis=models.IntegerField()
    body_l=models.IntegerField()
    team_s=models.IntegerField()
    articulation=models.IntegerField()
    participation=models.IntegerField()
    total=models.IntegerField()
    feedback=models.TextField()
    interviewer=models.ForeignKey('interviewer',on_delete=models.CASCADE)

    