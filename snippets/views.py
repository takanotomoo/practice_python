from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from snippets.forms import SnippetForm
from snippets.models import Snippet
from django.http import HttpResponseForbidden


def top(request):
    snippets = Snippet.objects.all()
    context = {"snippets":snippets}
    return render(request, "snippets/top.html", context)

@login_required
def snippet_new(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit = False) 
            snippet.created_by = request.user
            snippet.save()
            return redirect(snippet_detail, snippet_id=snippet.pk) 
    else:
        form = SnippetForm()
    return render(request, "snippets/snippet_new.html" ,{'form':form})

@login_required
def snippet_edit(request, snippets_id):
    snippet = get_object_or_404(Snippet, pk=snippets_id)
    if snippet.created_by_id != request.user.id:
        return HttpResponseForbidden("スニペットの編集は許可されていません。")
    
    if request.method =="POST":
        form = SnippetForm(request.POST, instance=snippet) 
        if form.is_valid():
            form.save()
            return redirect('snippet_detail', snippet_id=snippet_id)    
    else:
        form = SnippetForm(instance=snippet)
    return render(request, "snippets/snippet_edit.html" ,{'form':form})


def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    Snippet.objects.all()
    return render(request, 'snippets/snippet_detail.html',
        {'snippet': snippet})

'''
# フォームを使った登録処理の流れ
@required_http_methods(["GET", "POST"])
def signup(request):
    if request.method =="POST":
        # POSTリクエストを受けとったらxxxメソッドとxxxメソッドを呼ぶ
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(・・・)
        else:
            # GETリクエストを受けとったらformオブジェクトを用意して、テンプレートで表示
            form = UserCreationForm()
        return render(request, "signup.html" ,{'form':form})
'''
