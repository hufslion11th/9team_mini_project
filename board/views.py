from django.shortcuts import render, redirect
from .forms import PostForm
from django.core import serializers
from django.http import HttpResponse
from board.models import Group, Fields, Natures

# Create your views here.

def main(request):      #메인
    glist = Group.objects.all()
    return render(request, "main.html", {'groups' : glist})


def detail(request):
    return render(request, "detail.html")

def register(request):
    return render(request, "register.html")

def create(request):
    if request.method == "GET":
        postForm = PostForm()
        context = {'postForm': postForm} #{key:값}
        return render(request, "board/create.html", context)
    elif request.method =="POST":
        postForm = PostForm(request.POST)

        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.save()
        return redirect("/admin/")

def search(request):    #필터를 위한 함수(작성중)
    postlist = Group.objects.all()
    fieldlist = Fields.objects.all()
    naturelist = Natures.objects.all()
    name = request.GET.get('name', '')  # 검색어
    fname = request.GET.get('fname', '')
    nname = request.GET.get('nname', '')
    if name:
        postlist = postlist.filter(
            Q(subject__icontains=name) |  # 제목 검색
            Q(content__icontains=fname) |  # 분야 검색
            Q(answer__content__icontains=nname) # 분위기 검색
            # Q(author__username__icontains=) |  # 글쓴이 검색
        ).distinct()  # get 값을 가지는 필드의 내용을 가져 오기
    json_post_list = serializers.serialize("json", postlist)
    return HttpResponse(json_post_list)
