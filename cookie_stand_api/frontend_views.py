from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import CookieStand
from .forms import CustomForm


class CookieStandListView(ListView):
    template_name = 'list.html'
    model = CookieStand


class CookieStandDetailView(DetailView):
    template_name = 'detail.html'
    model = CookieStand
    fields = "__all__"


class CookieStandCreateView(CreateView):
    template_name = 'create.html'
    model = CookieStand
    form_class = CustomForm
    success_url = reverse_lazy('list')


class CookieStandUpdateView(UpdateView):
    template_name = 'update.html'
    form_class = CustomForm
    model = CookieStand
    success_url = reverse_lazy('list')


class CookieStandDeleteView(DeleteView):
    template_name = 'delete.html'
    model = CookieStand
    success_url = reverse_lazy('list')
