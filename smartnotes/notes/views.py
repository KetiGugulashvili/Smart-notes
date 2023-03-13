from .models import Notes
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import NoteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    form_class = NoteForm
    template_name = 'notes/notes_form.html'
    success_url = '/smart/notes'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NoteUpdateView(UpdateView):
    model = Notes
    form_class = NoteForm
    success_url = '/smart/notes'


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/list.html'
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()


class NoteDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = 'notes/detail.html'


class NoteDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
