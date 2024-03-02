from django.db.models.query import QuerySet
from django.db.models import Q
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from a1site.utils import pick_best_image
from . models import Work, Image
from . forms import WorkForm,ImageForm

 

def home(request):
    return render(request, "catalog/home.html", {})

def catalog_cards(request):

    
    # works = Work.objects.raw("select c.*, i.* from catalog_work c left outer join catalog_image i on c.id = i.work_id and i.image_type = 'primary'")
    works = []
    for w in Work.objects.all():
        images = Image.objects.filter(work_id = w.id)
        best = pick_best_image(images)         
        works.append([w,best])


    context = {"works":works}
    return render(request, "catalog/catalog_cards.html", context)

def catalog_list(request):
    print("here I am")
    # works = Work.objects.raw("select c.*, i.* from catalog_work c left outer join catalog_image i on c.id = i.work_id and i.image_type = 'primary'")
    srch = request.GET.get('tsearch','')
    works = []
    for w in Work.objects.filter(Q(title__icontains=srch) | Q(media__icontains=srch) | Q(description__icontains=srch) | Q(notes__icontains=srch) | Q(inscription__icontains=srch) | Q(work_date__icontains=srch)):
    # for w in Work.objects.all():
        images = Image.objects.filter(work_id = w.id)
        best = pick_best_image(images)         
        works.append([w,best])


    context = {"works":works}
    return render(request, "catalog/catalog_list.html", context)

def catalog_detail(request,pk):
    work = Work.objects.get(pk=pk)
    images = Image.objects.filter(work=pk)
    context = {"work":work, "images":images}
    return render(request, "catalog/catalog_detail.html", context)


    
   

def catalog_add(request):
    # get the parent object or create a new one
    work = Work()
    ImageFormset = inlineformset_factory(Work, Image, form=ImageForm, extra=2)
    
    
    # check the request method
    if request.method == "POST":
        if request.POST.get("action") == "Save":
            # create the parent form and the child formset from the request data
            workForm = WorkForm(request.POST, instance=work)
            imageForms = ImageFormset(request.POST, request.FILES, instance=work)
            # validate the forms
            if workForm.is_valid() and imageForms.is_valid():
                # save the parent and the children
                workForm.save()
                imageForms.save()
                # return to list after successful add
                return HttpResponseRedirect("/catalog/catalog_list/")
            else:
                #handle errors
                print("hit errors.  Try again?")
                print(imageForms.errors)
                workForm = WorkForm(request.POST, instance=work)
                imageForms = ImageFormset(request.POST, request.FILES, instance=work)
                keys = Work.objects.raw("SELECT ID, WORK_KEY FROM CATALOG_WORK")
                context = {"workform":workForm, "imageset":imageForms, "keys":keys}
                return render(request, "catalog/catalog_add.html", context)
        else:
            return HttpResponseRedirect("/catalog/catalog_list/")

    else:
            
   
        # create the parent form and the child formset from the parent instance
        workForm = WorkForm(instance=work)
        imageForms = ImageFormset(instance=work)
        keys = Work.objects.raw("SELECT ID, WORK_KEY FROM CATALOG_WORK")
        context = {"workform":workForm, "imageset":imageForms,"keys":keys}
         # render the template with the forms
        return render(request, "catalog/catalog_add.html", context)
    


def catalog_edit(request,pk):
    # get the parent object or create a new one
    work = Work.objects.get(pk=pk)
    ImageFormset = inlineformset_factory(Work, Image, form=ImageForm, extra=1)
    
    # check the request method
    if request.method == "POST":
        if request.POST.get("action") == "Save":
            # create the parent form and the child formset from the request data
            workForm = WorkForm(request.POST, instance=work)
            imageForms = ImageFormset(request.POST, request.FILES, instance=work)
            # validate the form
            if workForm.is_valid() and imageForms.is_valid():
                # save the parent and the children
                workForm.save()
                imageForms.save()
                # return to list after successful update
                return HttpResponseRedirect("/catalog/catalog_list/")
            else:
                print(imageForms.errors)

                workForm = WorkForm(request.POST, instance=work)
                imageForms = ImageFormset(request.POST, request.FILES, instance=work)
                context = {"workform":workForm, "imageset":imageForms}
                return render(request, "catalog/catalog_add.html", context)
 
        else:

            if request.POST.get("action") == "Delete":
                # work = Work.objects.get(pk=pk)
                work.delete()
                return HttpResponseRedirect("/catalog/catalog_list/")
            else:
                return HttpResponseRedirect("/catalog/catalog_list/")
                    

      
    else:
            
   
        # create the parent form and the child formset from the parent instance
        workForm = WorkForm(instance=work)
        imageForms = ImageFormset(instance=work)
        context = {"workform":workForm, "imageset":imageForms}
         # render the template with the forms
        return render(request, "catalog/catalog_edit.html", context)
    
    # def catalog_edit(request,pk):

#     if request.method == "POST":
#         if request.POST.get("action") == "Save":
#             workform = WorkForm(request.POST,instance=Work.objects.get(pk=pk))
#             if workform.is_valid:
#                 workform.save()
#                 return HttpResponseRedirect("/catalog/catalog_cards/")
#             else:
#                 print("handle errors here")
#         else:
#             if request.POST.get("action") == "Delete":
#                 workform = WorkForm(request.POST,instance=Work.objects.get(pk=pk))
#                 work = Work.objects.get(pk=pk)
#                 work.delete()
#                 return HttpResponseRedirect("/catalog/catalog_cards/")
            

#     work = Work.objects.get(pk=pk)
#     form = WorkForm(instance=work)
#     images = Image.objects.filter(work=work)
#     context = {"work":form, "images":images}
#     # print(form.is_bound)
            
#     return render(request, "catalog/catalog_edit.html",context)
