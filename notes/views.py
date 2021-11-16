from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import models
from .forms import NoteModelForm
# Create your views here.


@login_required
def note_list_view(request):
    form = NoteModelForm()
    if request.method == "POST":
        form = NoteModelForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect("home")
    user = request.user
    todos = user.todos.all()
    todo_list = todos.filter(finished=False)
    finished_list = todos.filter(finished=True)
    return render(request, "notes/note_list.html", context={"todo_list": todo_list, "finished_list": finished_list, "form": form})


@login_required
def finished_item(request, id):
    item = models.Note.objects.get(pk=id)
    item.finished = True
    item.save()
    return redirect("home")


@login_required
def undo_item(request, id):
    item = models.Note.objects.get(pk=id)
    item.finished = False
    item.save()
    return redirect("home")


@login_required
def delete_item(request, id):
    item = models.Note.objects.get(pk=id)
    item.delete()
    return redirect("home")
