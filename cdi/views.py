import hashlib
from django.shortcuts import redirect, render
from .models import Formation,Course
from .form import ApplyForm
from django.core.paginator import Paginator
from .filters import CoursFilter
# Create your views here.

def formation_list(request):
    course_list = Formation.objects.all()
    sp_course_list = Course.objects.all()
    #filters
    context = {'coureses':course_list,'sp_coureses':sp_course_list}
    return render(request,'home/home.html',context)

def formation_detaile(request,id):
    formation_detail = Formation.objects.get(id=id)
    context = {'formation_detail': formation_detail}
    return render(request,'home/deataille_formation.html',context)

def course_detail(request, id):
     
    id = int(hashlib.sha256(hashed_id.encode()).hexdigest(), 16)
    course_detail = Course.objects.get(id=id)
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.course = course_detail
            myform.save()
            # Rediriger l'utilisateur vers la même page de détail de cours
            # return redirect('course_detail', id=id)
    else:
        form = ApplyForm()
    context = {'course_detail': course_detail, 'form': form}
    return render(request, 'home/detaille_course.html', context)

#######contact########
def contact(request):
    course_list = Formation.objects.all()
    sp_course_list = Course.objects.all()
    #filters
    context = {'coureses':course_list,'sp_coureses':sp_course_list}
    return render(request,'home/contact.html',context)

####about#######
def about(request):
    course_list = Formation.objects.all()
    sp_course_list = Course.objects.all()
    #filters
    context = {'coureses':course_list,'sp_coureses':sp_course_list}
    return render(request,'home/about.html',context)

########course#######
def course(request):
    course_list = Formation.objects.all()
    sp_course_list = Course.objects.all()
    #filters
    context = {'coureses':course_list,'sp_coureses':sp_course_list}
    return render(request,'home/course.html',context)

########allFormation#######
def allFormation(request):
    sp_course_list = Course.objects.all()
    #filters
    my_filter = CoursFilter(request.GET,queryset=sp_course_list)
    sp_course_list = my_filter.qs
    paginator = Paginator(sp_course_list,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number )
    context = {'coureses':page_obj,'sp_coureses':my_filter}

    return render(request,'home/formation.html',context)

