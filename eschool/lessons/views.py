from django.shortcuts import render
from django.views import generic
from .models import Lesson

# Create your views here.

def index(request):
    num_lessons = Lesson.objects.all().count()

    context = {
        'num_lessons': num_lessons
    }

    return render(request, 'index.html', context=context)


class LessonListView(generic.ListView):
    model = Lesson

    # Get 2 Lessons with 'programming' in their name, instead of all lessons
    # def get_queryset(self):
    #     return Lesson.objects.filter(name__icontains="programming")[:2]

class LessonDetailView(generic.DetailView):
    model = Lesson











