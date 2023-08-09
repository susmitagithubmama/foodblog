from django.shortcuts import render
from .models import FoodBlogModel
from .myform import MyForm
from .myform import BlogForm
from .studentReg import StudentReg
from django.http import HttpResponseRedirect
# Create your views here.
def bloghome(request):
    return render(request,'index.html')

def blogprofile(request):
    context={"name":"Rakesh Sahoo","email":"rakesh@gmail.com","phone":445879123,"address":"Ganesh bazar","pin":759001}
    return render(request,'profile.html',context)

def blogshake(request):
    desc1="""Lorem ipsum dolor sit amet consectetur adipisicing elit. Non tempore vero doloribus dolor odit, eligendi aliquam, earum quia sunt id explicabo? Aperiam quod nulla vel ratione sint vitae itaque eveniet! Similique nesciunt accusamus, veritatis maiores, dolore id vitae tempora repellendus cumque saepe quis. Molestias exercitationem, sequi ducimus natus possimus soluta!"""

    desc2="""Lorem ipsum, dolor sit amet consectetur adipisicing elit. Facilis nesciunt reiciendis debitis distinctio eveniet nulla molestias, nihil, tempora eligendi repellat, unde similique deleniti aliquam odit dolore obcaecati! Reiciendis cumque consectetur at repellendus voluptatum voluptas est nam debitis. Quidem ratione officia dolore mollitia, totam debitis aspernatur, harum aut rerum minima non sed in architecto beatae nam facere veritatis accusantium et consectetur nesciunt similique sapiente. """
    desc3="""Ab sit corrupti amet earum quibusdam expedita unde, excepturi atque nemo fuga enim saepe porro dicta iure ratione natus veritatis obcaecati delectus nobis esse doloribus ipsum ea. Necessitatibus est assumenda laudantium, commodi in accusantium magni deleniti pariatur."""

    d1={"blogTitle":"Mango Shake","description":desc1}
    d2={"blogTitle":"Chocolate Shake","description":desc2}
    d3={"blogTitle":"Banana Shake","description":desc3}

    shakeblogs=[d1,d2,d3]
    context={"blogs":shakeblogs}
    return render(request,'shake.html',context)

def travelblog(request):
    return render(request,'childblog.html')

def index2(request):
    return render(request,'index2.html')

def getAllBlogs(request):
    # data = FoodBlogModel.objects.all()
    # data = FoodBlogModel.objects.filter(id=1)
    # data = FoodBlogModel.objects.exclude(blog_title="Mango Shake")
    # data = FoodBlogModel.objects.order_by("-blog_title")
    data = FoodBlogModel.objects.all()
    print("data=",data)
    context={
        "blogs":data
    }
    return render(request,"blogs.html",context)


#def formView(request):
    # form = MyForm(auto_id=True)
    # form = MyForm(auto_id='myform_%s')
    #form = MyForm(auto_id=False)
    # form = MyForm(label_suffix='')
    # form = MyForm(label_suffix='-')
    # form = MyForm(initial={'sname':'Student Name','semail':'studentemail@example.com'})
    #form =MyForm()
    #form.order_fields(field_order=['semail','sname'])
    #return render(request,'myform.html',{'form':form})

def successView(request):
    return render(request,'success.html')
def formView(request):
    if(request.method=='POST'):
        form= MyForm(request.POST)
        if(form.is_valid()):
            print("form validation successfull")
            name=form.cleaned_data['sname']
            password=form.cleaned_data['spass']
            email=form.cleaned_data['semail']
            # print(name)
            # print(password)
            # print(email)
            #return render(request,'success.html',{'name':name})
            #return HttpResponseRedirect('success')
            return HttpResponseRedirect('/myform/success')
        return render(request,'myform.html',{'form':form})
    else:
        form = MyForm()
        return render(request,'myform.html',{'form':form})



def stdForm(request):
    form = StudentReg() 
    return render(request,'studentReg.html',{'form':form})

def blogFormSubmit(request):
    if(request.method=='POST'):
        form=BlogForm(request.POST)
        if(form.is_valid()):
            title = form.cleaned_data['title']
            blogAuthor = form.cleaned_data['author']
            post = form.cleaned_data['post']
            #fb=FoodBlogModel(blog_title=title,author=blogAuthor,blogpost=post)#new record creation 
            #fb.save()

            #fb=FoodBlogModel(id=1,blog_title=title,author=blogAuthor,blogpost=post)#update
           # fb=FoodBlogModel(id=1,blog_title=title) #updation
           # fb = FoodBlogModel.objects.get(id=2) #get object
           # fb.blog_title='Keshar Pista Shake' #update
            #fb.save()
            fb = FoodBlogModel.objects.get(id=2) #get object
            fb.delete()
        return render(request,'blogform.html',{'form':form})
    else:
        form =BlogForm()
        return render(request,'blogform.html',{'form':form})