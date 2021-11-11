from django.shortcuts import redirect, render
from . import models
from .forms import NoteModelForm
# Create your views here.


def note_list_view(request):
    form = NoteModelForm()
    if request.method=="POST":
        form = NoteModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    todo_list = models.Note.objects.filter(finished=False)
    finished_list = models.Note.objects.filter(finished=True)
    return render(request, "note_list.html", context={"todo_list": todo_list, "finished_list": finished_list,"form":form})
def finished_item(request,id):
    item=models.Note.objects.get(pk=id)
    item.finished=True
    item.save()
    return redirect("home")
def undo_item(request,id):
    item=models.Note.objects.get(pk=id)
    item.finished=False
    item.save()
    return redirect("home")
def delete_item(request,id):
    item=models.Note.objects.get(pk=id)
    item.delete()
    return redirect("home")