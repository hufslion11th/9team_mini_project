from django.shortcuts import render, redirect

# Create your views here.

def main(request):      #메인
    return render(request, "main.html")

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

def list(request):      #목록
    posts= Post.objects.all().order_by('-id') #게시글 나열, 정렬
    context = { 'posts': posts}
    return render(request, 'board/list.html', context)
#
def read(request, bid):      #한가지 게시글만 읽어오기
    post = Post.objects.get(id=bid) #게시글 나열, 정렬
    context = { 'post ': post}
    return render(request, 'board/read.html', context)

def info(request):      #상세
    return render(request, "info.html")

# def getdata(request):
#     num1 = request.GET.get("var1")
#     num2 = request.GET.get("var2")
#     print(int(num1)+int(num2))
#
#     return render(request, "getdata.html")