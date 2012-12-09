# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import RequestContext
from django.utils import simplejson as sj
import random
from django.views.decorators.csrf import csrf_protect
from django.template.loader import render_to_string
from django.conf import settings
import os

def home_page(request):
	return render_to_response('Home_page.html',context_instance=RequestContext(request))
def base_exercise(request):
	return render_to_response('base.html',context_instance=RequestContext(request))

def schulte_table_html(request):
	html_content = "empty"
	if request.is_ajax():
		table_values = range(1,26)
		table_indexes = range(25)
		random.shuffle(table_values)
		html_content = render_to_string('SchulteTable.html',{'table':table_values,'index':table_indexes},context_instance=RequestContext(request))
	return HttpResponse(html_content,mimetype="application/html")
def schulte_table_about(request):
	return render_to_response('SchulteTable_about.html',context_instance=RequestContext(request))
def schulte_table_result(request):
	if request.is_ajax():
		if request.method == 'POST':
			try:
				print request.POST['ex_name'],request.POST['min'],request.POST['sec']
			except Exception,e:
				print e
		return HttpResponse()

def field_of_view_exercise_about(request):
	return render_to_response('base_field_of_view_exercise_about.html',context_instance=RequestContext(request))



	

def green_point(request):
	return render_to_response('GreenPoint_about.html',context_instance=RequestContext(request))
def green_point_html(request):
	try:
		if request.is_ajax():
			if request.method == 'GET':
				html_content = render_to_string('GreenPoint.html',context_instance=RequestContext(request))
				html_content =  " ".join(html_content.split())
				#print html_content
				# page_data = {'html_content':html_content}
				# print page_data
				    			    		  		
	except Exception,e:
		print e
	# return HttpResponse(sj.dumps(page_data),mimetype="application/json")
	return HttpResponse(html_content,mimetype="application/html")
def green_point_result(request):
	if request.is_ajax():
		if request.method == 'POST':
			try:
				print request.POST['ex_name'],request.POST['done'],request.POST['min'],request.POST['sec']
			except Exception,e:
				print e
	return HttpResponse()

def vertical_about(request):
	return render_to_response('VerticalAbout.html',context_instance=RequestContext(request))

def vertical(request):
	return render_to_response('Vertical.html',context_instance=RequestContext(request))

def storm_about(request):
	return render_to_response('StormAbout.html',context_instance=RequestContext(request))

def storm(request):
	return render_to_response('Storm.html',context_instance=RequestContext(request))

def attention_letters_html_from_modal(request):
	letters = ['К','Е','Х','Н','В','А','С','И']
	letter1 = random.choice(letters)
	letter2 = random.choice(letters)
	letters.remove(letter2)
	letter3 = random.choice(letters)
	html_content = render_to_string('AttentionLettersAboutFromModal.html',{'letter1':letter1,'letter2':letter2,'letter3':letter3},context_instance=RequestContext(request))
	html_content =  " ".join(html_content.split())
	print html_content
	# return render_to_response('AttentionLettersAbout.html',{'letter1':letter1,'letter2':letter2,'letter3':letter3},context_instance=RequestContext(request))
	return HttpResponse(html_content,mimetype="application/html")
def attention_letters(request):
	letters = ['К','Е','Х','Н','В','А','С','И']
	letter1 = random.choice(letters)
	letter2 = random.choice(letters)
	letters.remove(letter2)
	letter3 = random.choice(letters)
	# html_content = render_to_string('AttentionLettersAbout.html',{'letter1':letter1,'letter2':letter2,'letter3':letter3},context_instance=RequestContext(request))
	return render_to_response('AttentionLettersAbout.html',{'letter1':letter1,'letter2':letter2,'letter3':letter3},context_instance=RequestContext(request))
	# return HttpResponse()
def attention_letters_json(request):
	page_data = {}
	letters_to_search = " ";
	letters_to_find = []
	letters = [u'К',u'Е',u'Х',u'Н',u'В',u'А',u'С',u'И']
	w = 22
	h = 10
	letters_array = [random.choice(letters) for x in range(w) for y in range(h)]	
	try:
		if request.method == 'GET':
			# print request.POST
			letters_to_find = request.GET['chosen_letters']
			if len(letters_to_find) == 1:
				
				letter1 = letters_to_find[0]
				# print letters_array,letter1,letters_array.count(letter1)
				letter1_count = letters_array.count(letter1)
				html_content = render_to_string('AttentionLetters.html',{'letters_array':letters_array,'width':w,'letters_to_find':letters_to_find})
				html_content =  " ".join(html_content.split())
				# print html_content
				page_data = {'letter1_count':letter1_count,'html_content':html_content}
				# print letter1_count
			if len(letters_to_find) == 2:
				letter1 = letters_to_find[0]
				letter2 = letters_to_find[1]
				letter1_count = letters_array.count(letter1)
				letter2_count = letters_array.count(letter2)
				html_content =  render_to_string('AttentionLetters.html',{'letters_array':letters_array,'width':w,'letters_to_find':letters_to_find})
				html_content =  " ".join(html_content.split())
				page_data = {'letter1_count':letter1_count,'letter2_count':letter2_count,'html_content':html_content}
				# print letter2_count,letter3_count
			

		
			# print sj.dumps(json)
	except Exception,e:
		print e
	return HttpResponse(sj.dumps(page_data), mimetype="application/json")

def get_attention_letters_result(request):
	if request.is_ajax():
		if request.method == 'POST':
			try:
				print request.POST['ex_name'],request.POST['mistake_count'],request.POST["min"],request.POST["sec"]
			except Exception,e:
				print e
	return  HttpResponse()

def double_images(request):
	return render_to_response("DoubleImagesAbout.html",context_instance=RequestContext(request))

def double_images_json(request):
	try:
		if request.is_ajax():
			if request.method == 'GET':
				img_files_list = []
				path = "static/img/double_images"
				# path = "/Users/igor/Desktop/SpeedReading/static/img/double_images"
				for files in os.listdir(path):
					if files.endswith(".jpeg"):
						img_files_list.append(files)
				img_src = "/static/double_images/" + random.choice(img_files_list)
				# print img_src
				# print img_files_list
				html_content = render_to_string('DoubleImages.html',{'img_src':img_src},context_instance=RequestContext(request))
				html_content =  " ".join(html_content.split())
				print html_content
				page_data = {'html_content':html_content}
				
				    			    		  		
	except Exception,e:
		print e
	return HttpResponse(sj.dumps(page_data),mimetype="application/json")
# def double_images(request):
# 	return render_to_response("")

def summ(request):
	return render_to_response('Summ.html',context_instance=RequestContext(request))


