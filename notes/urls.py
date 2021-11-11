from django.urls import path
from . import views
urlpatterns = [
    path('',views.note_list_view,name="home"),
    path('finished/<int:id>/',views.finished_item,name="finished"),
    path('undo/<int:id>/',views.undo_item,name="undo"),
    path('delete/<int:id>/',views.delete_item,name="delete"),
]
