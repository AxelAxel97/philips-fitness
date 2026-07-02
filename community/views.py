from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SuccessPost
from .forms import SuccessPostForm


@login_required
def post_list(request):
    posts = SuccessPost.objects.all()
    return render(request, 'community/post_list.html', {'posts': posts})


@login_required
def create_post(request):
    profile = request.user.profile

    if not profile.is_subscriber:
        messages.error(request, 'Only subscribers can create success posts.')
        return redirect('community')

    if request.method == 'POST':
        form = SuccessPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Success post created!')
            return redirect('community')
    else:
        form = SuccessPostForm()

    return render(request, 'community/create_post.html', {'form': form})
