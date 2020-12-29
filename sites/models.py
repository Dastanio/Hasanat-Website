from django.db import models

class News(models.Model):
	title = models.CharField(max_length=128, default='')
	sub_title = models.CharField(max_length=2048, default='')
	img = models.ImageField(upload_to='News_images/')
	img_2 = models.ImageField(upload_to='News_images/', default='', blank=True)


	def __str__(self):
		return self.title

class Images_news(models.Model):
	new = models.ForeignKey(News, on_delete=models.CASCADE)
	image = models.ImageField(upload_to = 'News_multiple_images/')

	def __str__(self):
		return self.new.title


class Tags(models.Model):
	tag_name = models.CharField('Имя тега', max_length= 255)


	def __str__(self):
		return self.tag_name

class Projects(models.Model):
	title = models.CharField(max_length=128, default='')
	title_2 = models.CharField(max_length=128, default='')
	sub_title = models.CharField(max_length=2048, default='')
	sub_title_2 = models.CharField(max_length=2048, default='')
	collapse_title_1 = models.CharField(max_length=128, default='')
	collapse_sub_title_1 = models.CharField(max_length=1280, default='')
	collapse_title_2 = models.CharField(max_length=128, default='')
	collapse_sub_title_2 = models.CharField(max_length=1280, default='')
	collapse_title_3 = models.CharField(max_length=128, default='')
	collapse_sub_title_3 = models.CharField(max_length=1280, default='')
	collapse_title_4 = models.CharField(max_length=128, default='')
	collapse_sub_title_4 = models.CharField(max_length=1280, default='')
	img = models.ImageField(upload_to='Projects_images/')
	img_2 = models.ImageField(upload_to='Projects_images/', default='', blank=True)
	tags = models.ForeignKey(Tags, on_delete= models.CASCADE, default = '', null = True)
	def __str__(self):
		return self.title

class Images(models.Model):
	project = models.ForeignKey(Projects, on_delete=models.CASCADE)
	image = models.ImageField(upload_to = 'Projects_multiple_images/', blank=True)

	def __str__(self):
		return self.project.title


class Calculate(models.Model):
	name = models.CharField('Имя',max_length = 255)
	email = models.EmailField('Почта')
	phone_num = models.CharField('Номер телефона', max_length = 255)
	comment_text = models.TextField('Комментарий')

	def __str__(self):
		return self.name