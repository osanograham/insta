from django.shortcuts import render
from .models import faq
# Create your views here.
def index(request):
	faqs=list(faq.objects.all())

	return render(request,"index.html",{"faqs":faqs})
