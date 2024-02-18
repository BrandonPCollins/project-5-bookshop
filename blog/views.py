from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm, EditCommentForm, PostForm
from django.http import HttpResponseForbidden

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(parent__isnull=True) 
    new_comment = None
    comment_form = None

    if request.user.is_authenticated:
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.author = request.user
                parent_id = request.POST.get('parent')
                if parent_id:
                    new_comment.parent = Comment.objects.get(id=parent_id)
                new_comment.save()
        else:
            comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})

def create_post(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()  # Return a 403 Forbidden response

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('post_detail', post_id=new_post.id)
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author or request.user.is_staff:
        comment.delete()
    return redirect('post_detail', post_id=comment.post.id)


def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user != comment.author:
        return HttpResponseForbidden()  # Return a 403 Forbidden response
    if request.method == 'POST':
        form = EditCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=comment.post.id)
    else:
        form = EditCommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form})

