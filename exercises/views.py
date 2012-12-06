# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404
from django.template import RequestContext
from django.utils import simplejson
import random
from django.views.decorators.csrf import csrf_protect
from django.template.loader import render_to_string

def base_exercise(request):
	return render_to_response('base.html',context_instance=RequestContext(request))
def schulte_table(request):
	table_values = range(1,26)
	table_indexes = range(25)
	random.shuffle(table_values)

	return render_to_response('SchulteTable.html',{'table':table_values,'index':table_indexes},context_instance=RequestContext(request))
def schulte_table_about(request):
	return render_to_response('SchulteTable_about.html',context_instance=RequestContext(request))
def field_of_view_exercise_about(request):
	return render_to_response('base_field_of_view_exercise_about.html',context_instance=RequestContext(request))

def schulte_table_inf(request):
	if request.is_ajax():
		if request.method == 'POST':
			try:
				min =  int(request.POST['min'])
				sec =  int(request.POST['sec'])
				ex_name = request.POST['ex_name']	
			except Exception,e:
				print e
		return render_to_response('thanks.html',{'data':request.raw_post_data},context_instance=RequestContext(request))
	

def green_point(request):
	return render_to_response('GreenPoint.html',context_instance=RequestContext(request))

def green_point_about(request):
	return render_to_response('GreenPoint_about.html',context_instance=RequestContext(request))

def vertical_about(request):
	return render_to_response('VerticalAbout.html',context_instance=RequestContext(request))

def vertical(request):
	return render_to_response('Vertical.html',context_instance=RequestContext(request))

def storm_about(request):
	return render_to_response('StormAbout.html',context_instance=RequestContext(request))

def storm(request):
	return render_to_response('Storm.html',context_instance=RequestContext(request))

def attention_letters_about(request):
	letters = ['К','Е','Х','Н','В','А','С','И']
	letter1 = random.choice(letters)
	letter2 = random.choice(letters)
	letters.remove(letter2)
	letter3 = random.choice(letters)
	return render_to_response('AttentionLettersAbout.html',{'letter1':letter1,'letter2':letter2,'letter3':letter3},context_instance=RequestContext(request))

def attention_letters(request):
	letters_to_search = " ";
	letters_to_find = []
	letters = [u'К',u'Е',u'Х',u'Н',u'В',u'А',u'С',u'И']
	w = 22
	h = 10
	letters_array = [random.choice(letters) for x in range(w) for y in range(h)]	
	try:
		if request.method == 'POST':
			# print request.POST
			letters_to_find = request.POST['chosen_letters']
			if len(letters_to_find) == 1:
				
				letter1 = letters_to_find[0]
				
				letter1_count = letters_array.count(letter1)
				# print letter1_count
			if len(letters_to_find) == 2:
				letter2 = letters_to_find[0]
				letter3 = letters_to_find[1]
				letter2_count = letters_array.count(letter2)
				letter3_count = letters_array.count(letter3)
				# print letter2_count,letter3_count
			

		
	
		s =  render_to_string('AttentionLetters.html',{'letters_array':letters_array,'width':w,'letters_to_find':letters_to_find})
		# print s
	except Exception,e:
		print e
	return HttpResponse(s)



def summ(request):
	return render_to_response('Summ.html',context_instance=RequestContext(request))


