from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . models import Score


class ScoreListView(ListView):
    model = Score
    template_name = 'home.html'


class ScoreDetailView(DetailView):
    model = Score
    template_name = 'score_detail.html'

class ScoreCreateView(CreateView):
    model = Score
    template_name = 'score_new.html'
    fields = ['name', 'score']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.scoreadmin = self.request.user
        return super(ScoreCreateView, self).form_valid(form)


class ScoreUpdateView(UpdateView):
    model = Score
    fields = ['name', 'score']
    template_name = 'score_update.html'

class ScoreDeleteView(DeleteView):
    model = Score
    template_name = 'score_delete.html'
    success_url = reverse_lazy('home')


def scoreUserView(request, queryset=None):
    object_list = Score.objects.filter(scoreadmin=request.user)
    context = {
        "object_list" : object_list
    }
    return render(request, 'score_user.html', context)
