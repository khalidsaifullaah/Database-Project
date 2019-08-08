from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Idea

# Create your views here.
def allIdeas(request):
    context = {
        'ideas': Idea.objects.all()
    }

    return render(request, 'ideas/all_ideas.html', context)


class IdeaListView(ListView):
    model = Idea
    template_name = 'ideas/all_ideas.html'
    context_object_name = 'ideas'
    ordering = ['-date_posted']


class IdeaDetailView(DetailView):
    model = Idea


class IdeaCreateView(LoginRequiredMixin ,CreateView):
    model = Idea
    fields = ['title', 'description', 'catagory','area', 'thumbnail']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IdeaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Idea
    fields = ['title', 'description', 'catagory','area', 'thumbnail']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        idea = self.get_object()
        if self.request.user == idea.author:
            return True
        return False


class IdeaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Idea
    success_url = '/ideas'
    def test_func(self):
        idea = self.get_object()
        if self.request.user == idea.author:
            return True
        return False