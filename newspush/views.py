from django.shortcuts import render

# Create your views here.

def commit_comment(request, news_id):
    news_ = news.objects.get(id=news_id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            newsComment.objects.create(
                
            )
