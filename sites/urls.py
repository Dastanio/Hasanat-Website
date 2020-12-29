from django.urls import path
from .views import *
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about_company/', views.about_company, name='about_company'),
	path('shef_montaj/', views.shef_montaj, name='shef_montaj'),
	path('vakansii/', views.vakansii, name='vakansii'),
	path('pusko_naladochnue/', views.pusko_naladochnue, name='pusko_naladochnue'),
	path('voprosy_otvety/', views.voprosy_otvety, name='voprosy_otvety'),
	path('podbor_oborudovania/', views.podbor_oborudovania, name='podbor_oborudovania'),
	path('create_documetation/', views.create_documetation, name='create_documetation'),
	path('new_detail/<int:new_id>/', views.new_news_detail, name='new_news_detail'),
	path('project_detail/<int:id>/', views.new_detail, name='new_detail'),
	path('news/', views.news, name='news'),

	path('contacts/', views.contacts, name='contacts'),


	path('liscense/', views.liscence, name='liscence'),

	
	path('detail_five/', views.detail_five, name='detail_five'),








	path('projects/', views.projects, name='projects'),
	

]