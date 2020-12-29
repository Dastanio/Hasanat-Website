from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.generic import ListView, TemplateView
from django.db.models import Q
from .forms import *


# class SearchNewsView(ListView):
#     model = News
#     template_name = 'main/news.html'
#     def get_queryset(self): # новый
#         query = self.request.GET.get('q')
#         news_list = News.objects.filter(
#             Q(title__icontains=query) | Q(sub_title__icontains=query)
#         )
#         return news_list

# class SearchProjectView(ListView):
#     template_name = 'main/projects.html'
#     def get_queryset(self): # новый
#         query = self.request.GET.get('q')
#         projects_list = Projects.objects.filter(
#             Q(title__icontains=query) | Q(sub_title__icontains=query)
#         )
#         return (projects_list)


def index(request):
	projects = Projects.objects.order_by('-id')[:8]
	news = News.objects.order_by('-id')[:8]
	context = {
				"projects": projects,
				'news': news,
	}
	template_name = 'main/index.html'
	return render(request, template_name, context)


def podbor_oborudovania(request):
	template_name = 'main/slider.html'
	return render(request, template_name)

def create_documetation(request):
	template_name = 'main/nine_page.html'
	return render(request, template_name)

def new_news_detail(request, new_id):
	template_name = 'main/five_blocks.html'
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	new = get_object_or_404(News, id=new_id)
	new_images = Images_news.objects.filter(new=new)
	context = {
				"new": new,
				'new_images': new_images,
				'all_projects': all_projects,
				'all_news': all_news,
	}
	return render(request, template_name, context)

def detail_five(request):
	template_name = 'main/detail_five.html'
	return render(request, template_name)

def new_detail(request, id):
	template_name = 'main/new-detail.html'
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	project = get_object_or_404(Projects, id=id)
	images = Images.objects.filter(project=project)
	context = {
				"project": project,
				'images': images,
				'all_projects': all_projects,
				'all_news': all_news,
	}
	return render(request, template_name, context)

def about_company(request):
	template_name = 'main/second_page.html'
	return render(request, template_name)

def shef_montaj(request):
	template_name = 'main/five_page.html'
	return render(request, template_name)

def vakansii(request):
	template_name = 'main/vakansii.html'
	return render(request, template_name)

def pusko_naladochnue(request):
	template_name = 'main/four_page.html'
	return render(request, template_name)

def liscence(request):
	template_name = 'main/liscence.html'
	return render(request, template_name)

# def three(request):
# 	template_name = 'main/3.html'
# 	return render(request, template_name)

def contacts(request):
	template_name = 'main/six_page.html'
	return render(request, template_name)

def voprosy_otvety(request):
	template_name = 'main/seven_page.html'
	return render(request, template_name)

def projects(request):
	template_name = 'main/projects_all.html'
	projects = Projects.objects.all()
	context = {
		'projects': projects
	}
	return render(request, template_name, context)

def news(request):
	template_name = 'main/news_all.html'
	news = News.objects.all()
	context = {
		'news': news
	}
	return render(request, template_name, context)




