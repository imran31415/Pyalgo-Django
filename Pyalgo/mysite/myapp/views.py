from __future__ import print_function
from django.shortcuts import render
import random
import time
from django.http import HttpResponse
from myapp.forms import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
import os
import csv
#from pyalgotrade import strategy
#from pyalgotrade.barfeed import yahoofeed
#from pyalgotrade.technical import ma
#import pyalgotrade

def index(request):
	form = CodeForm()
	variables = RequestContext(request, {
	'form': form})
	return render_to_response('formdata.html',variables)
 

def runcode(request):

 	if request.method == 'POST':
 		form = CodeForm(request.POST)
 		if form.is_valid():
			c = form.cleaned_data['code']
			clist = c.split("\n")
			try:
				unique = str(random.randint(0,10000)) + str(time.strftime("%H-%M-%S")) +'temp'
				with open(unique+'.py', 'w') as the_file:
					#the_file.write("\nif '__name__' =='__main__':\n")
					for x in clist:
		   				the_file.write(x)
				import importlib

				importlib.import_module(unique)

			   	if isinstance(main_out, list):
				   	variables = RequestContext(request, {'form':form,
					'main_out': main_out})
					return render_to_response('formview.html',variables)
			except Exception, e:
				error = ['Error in your code: ', str(e)]
				variables = RequestContext(request, {'form':form,'main_out': error})
				return render_to_response('formview.html',variables)

			#return HttpResponse(main_out)
		else:
			form = CodeForm()
			variables = RequestContext(request, {
			'form': form})
			return render_to_response('formdata.html',variables)