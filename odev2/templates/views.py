from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from odev2.models import Blog
from odev2.models import Industry
     


from odev2.forms import IndustryForm
from odev2.forms import BlogForm



def index(request):
    if request.user.is_authenticated :
        username = request.user.username
        return render (request , 'indexUser.html', {
                                'username' : username
        })
    else:
        return render(request , 'index.html')


@login_required
def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

@login_required
def singleBlog(request,pk):
    blog = Blog.objects.get(pk=pk)
    return render (request ,'blog-single-post.html', {'blog' : blog})  


@login_required
def industries(request):
    industries = Industry.objects.all()
    return render(request, 'industries.html' ,{'industries' : industries })

@login_required
def singleIndustry(request, pk):
    industry = Industry.objects.get(pk=pk)
    return render(request, 'industries-single-industry.html', {'industry': industry})
          
            
def register(request):
    if request.method == "POST":
        username = request.POST["email"]
        email = request.POST["email"]
        password = request.POST["password"]
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return HttpResponseRedirect(reverse('index') + '#go-login')
        else:
            return HttpResponseRedirect(reverse('index'))    # Kullanıcı adı zaten var, ana sayfaya geri yönlendir
            #return render(request, 'index.html')    
    return HttpResponseRedirect(reverse('index') + '#go-register')  

# def show_login_popup(request):
#     return HttpResponseRedirect(reverse('index') + '#go-login')


def login(request):
    if request.method == 'POST':
        username = request.POST["email"]
        email = request.POST ["email"]
        password = request.POST ["password"]
        user = authenticate ( username= username , email=email, password=password)
        if user is not None:
            auth.login (request, user)
            return render (request , "indexUser.html" , {'username' : username})
        else:
             return HttpResponseRedirect(reverse('index') + '#go-login')
            # return render (request, 'Login.html', {'Error' : True})
    return HttpResponseRedirect(reverse('index') + '#go-login') 

# @login_required      
# def indexUser(request):
#     return render (request , "indexUser.html" )
    
@login_required      
def logout (request):
    if request.method== 'POST' :
        auth.logout(request)  # Kullanıcıyı oturumdan çıkart
        request.session.flush()  # Oturum verilerini temizle
        return redirect ("index")
            #devamı var
    return redirect ("index")



def add_industry(request):
    message = None
    if request.method == 'POST':
        form = IndustryForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Industry added successfully.'  # Başarılı mesajı gönder
        else:
            message = 'Failed to add industry. Please check your input.'  # Başarısız mesajı gönder
    else:
        form = IndustryForm()
    return render(request, 'industries.html', { 'message': message})


def add_blog(request):
    message = None
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Blog post added successfully.'  # Başarılı mesajı gönder
        else:
            message = 'Failed to add blog post. Please check your input.'  # Başarısız mesajı gönder
    else:
        form = BlogForm()
    return render(request, 'blog.html', { 'message': message})

def show_login_popup(request):
    return HttpResponseRedirect(reverse('index') + '#go-login')