# -*- coding: utf-8 -*-
from django import forms
from exercises.models import vertical
from django.forms import ModelForm


class verticalForm(forms.Form):
	def __init__(self,*args,**kwargs):
		text_name = kwargs.pop('text_name')	
		super(verticalForm, self).__init__(*args, **kwargs)
		vertical_obj = vertical.objects.filter(name=text_name)[0]
		for field in range(1,11):
			self.fields['q%d_field' % field] = forms.CharField(label=vertical_obj.__dict__['question%d' % field])
		# self.fields['q1_field'] = forms.CharField(label=vertical_obj.question1)
		
		# self.fields['q2_field'] = forms.CharField(label=vertical_obj.question2)
		# self.fields['q3_field'] = forms.CharField(label=vertical_obj.question3)
		# self.fields['q4_field'] = forms.CharField(label=vertical_obj.question4)
		# self.fields['q5_field'] = forms.CharField(label=vertical_obj.question5)
		# self.fields['q6_field'] = forms.CharField(label=vertical_obj.question6)
		# self.fields['q7_field'] = forms.CharField(label=vertical_obj.question7)
		# self.fields['q8_field'] = forms.CharField(label=vertical_obj.question8)
		# self.fields['q9_field'] = forms.CharField(label=vertical_obj.question9)
		# self.fields['q10_field'] = forms.CharField(label=vertical_obj.question10)
		


