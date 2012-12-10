# -*- coding: utf-8 -*-
from django import forms
from exercises.models import vertical
from django.forms import ModelForm


class verticalForm(forms.Form):
	def __init__(self,*args,**kwargs):
		text_name = kwargs.pop('text_name')
		super(verticalForm, self).__init__(*args, **kwargs)
		self.vertical_obj = vertical.objects.filter(name=text_name)[0]
		self.q1_field = forms.CharField(label=vertical_obj.question1)
		self.q2_field = forms.CharField(label=vertical_obj.question2)
		self.q3_field = forms.CharField(label=vertical_obj.question3)
		self.q4_field = forms.CharField(label=vertical_obj.question4)
		self.q5_field = forms.CharField(label=vertical_obj.question5)
		self.q6_field = forms.CharField(label=vertical_obj.question6)
		self.q7_field = forms.CharField(label=vertical_obj.question7)
		self.q8_field = forms.CharField(label=vertical_obj.question8)
		self.q9_field = forms.CharField(label=vertical_obj.question9)
		self.q10_field = forms.CharField(label=vertical_obj.question10)
# class verticalForm(ModelForm):
# 	class Meta:
# 		model = vertical
# 		fields = ['question1','answer1',
# 				  'question2','answer2',
# 				  'question3','answer3',
# 				  'question4','answer4',
# 				  'question5','answer5',
# 				  'question6','answer6',
# 				  'question7','answer7',
# 				  'question8','answer8',
# 				  'question9','answer9',
# 				  'question10','answer10',
# 				  ]

