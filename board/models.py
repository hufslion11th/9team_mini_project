from django.db import models

# Create your models here.
#class Post(models.Model): #글 게시
    #title = models.CharField(max_length=100)                  #제목
    #contents = models.TextField()                             #내용
    #mainphoto = models.ImageField(blank=True, null=True)


class Group(models.Model):
    # 그룹의 이름
    name = models.CharField(max_length=10)

    # 그룹 로고
    logo = models.ImageField(blank=True, null=True, upload_to = 'logo/%Y%m%d')
    # 그룹의 종류 선택지
    GROUP_TYPE_CHOICES = [
        ('동아리', '동아리'),
        ('기타모임', '기타모임'),
        ('스터디', '스터디'),
        ('학회', '학회'),
    ]
    group_type = models.CharField(max_length=10)

    # 그룹의 분야
    field = models.CharField(max_length=10)

    # 짧은 소개글
    short_introduce = models.TextField(max_length=50)

    # 그룹의 성격
    natures = models.CharField(max_length=10)

    # 모집인원
    recruitment_count = models.PositiveIntegerField()

    # 마감기한
    deadline = models.DateField()

    # 모집 링크
    recruiting_url = models.TextField(max_length=100)


class Natures(models.Model):
    # 성격 이름
    name = models.CharField(max_length=10)


class Fields(models.Model):
    # 분야
    name = models.CharField(max_length=10)


