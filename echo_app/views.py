from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm  # 後でフォームを作成

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}
    return render(request, 'echo_app/index.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # index ページにリダイレクト
    else:
        form = PostForm()
    return render(request, 'echo_app/create_post.html', {'form': form})