from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name='notes.list'),
    path('notes/new', views.NoteCreateView.as_view(), name='notes.new'),
    path('notes/<int:pk>', views.NoteDetailView.as_view(), name='notes.detail'),
    path('notes/<int:pk>/edit', views.NoteUpdateView.as_view(), name='notes.update'),
    path('notes/<int:pk>/delete', views.NoteDeleteView.as_view(), name='notes.delete'),
]