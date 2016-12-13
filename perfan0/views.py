from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# from django.template import loader

from .models import PerformanceSummary


def index(request):
	biggest_system_list = PerformanceSummary.objects.order_by('-capacity_total_sizetib')[:5].values()
	# template = loader.get_template('perfan0/index.html')
	context = {'biggest_system_list': biggest_system_list}
	# return HttpResponse(template.render(context, request))
	return render(request, 'perfan0/index.html', context)

def detail(request, system_id):
	company_name = PerformanceSummary.objects.get(serialnumberinserv__exact=system_id).system_companyname
	return HttpResponse("You're looking at system %s. It's owned by %s" % (system_id, company_name))