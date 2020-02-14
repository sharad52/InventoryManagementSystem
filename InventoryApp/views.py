from django.shortcuts import render,reverse,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Goods
from .forms import GoodsForm
from django.views.generic import ListView


# Create your views here.

    
# def index(request):

#     context={'title':'Inventory Management System'}
#     goods = Goods.objects.all()

#     return render(request,'index.html',{'context':context,'goods':goods})
class HomeView(ListView):
    model=Goods
    context_object_name='goods'
    template_name='index.html'

    # def get_context_data(self,**kwargs): #this is very powerful function inside list view we can view multiple model throw this
	# 	context=super().get_context_data(**kwargs)
	# 	context['publicationlist']=Publication.objects.filter(active=True)
	# 	return context


def add_assets(request):
    form = GoodsForm(request.POST or None)
    # print(form)
    if form.is_valid():
        form.save()
        form=GoodsForm()
        # return HttpResponseRedirect(reverse('baseapp:index'))
    

    return render(request,'form.html',{'form':form})

def edit_assets(request,good_id):
    goods=get_object_or_404(Goods,pk=good_id)
    form=GoodsForm(request.POST or None,instance=goods)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('baseapp:index'))
    return render(request,'form.html',{'form':form})

def delete_assets(request,good_id):
    goods=get_object_or_404(Goods,pk=good_id)
    # form=GoodsForm(request.POST or None,instance=goods)
    goods.delete()
    return HttpResponseRedirect(reverse('baseapp:index'))

    # return render(request,'form.html',{'form':form})
