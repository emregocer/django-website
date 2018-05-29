from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, HttpResponseRedirect, reverse
from django.http import HttpResponse, Http404
from django.utils.timezone import now
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Category, Topic, Reply

from apps.forum.forms.topic.create import CreateTopicForm


class ForumIndexView(ListView):
    model = Category
    context_object_name="categories"
    template_name="forum/index.html"

class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topics'] = Topic.objects.filter(topic_cat_id = self.kwargs['pk'])
        return context

    template_name="forum/category.html"

class TopicDetailView(DetailView):
    model = Topic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reply_list = Reply.objects.filter(reply_topic_id = self.kwargs['pk']).order_by('reply_date')
        paginator = Paginator(reply_list, 4)
        page = self.request.GET.get('page')
        replies = paginator.get_page(page)
        context['replies'] = replies
        return context

    template_name="forum/topic.html"

class CreateTopic(CreateView):
    model = Topic
    fields=['topic_subject', 'topic_content']

    def dispatch(self, request, *args, **kwargs):
        self.category = get_object_or_404(Category, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.topic_date = now()
        form.instance.topic_by = self.request.user
        form.instance.topic_cat = self.category
        return super(CreateTopic, self).form_valid(form)

    def get_success_url(self):
        return reverse("forum:topic", args=(self.object.id,))

class CreateReply(CreateView):
    model = Reply
    fields=['reply_content']

    def dispatch(self, request, *args, **kwargs):
        self.topic = get_object_or_404(Topic, pk=kwargs['pk']) # get the topic_id from the url
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.reply_date = now()
        form.instance.reply_topic = self.topic
        form.instance.reply_by = self.request.user
        return super(CreateReply, self).form_valid(form)

    def get_success_url(self):
        return reverse("forum:topic", args=(self.topic.id,))

#replies = Reply.objects.filter(reply_topic_id=topic_id)
#return render(request, "forum/topic.html", {'topic':topic, 'replies':replies, 'error_message':"Something happened while sending the message, couldn't send"})