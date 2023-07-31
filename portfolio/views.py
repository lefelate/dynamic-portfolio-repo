from django.shortcuts import redirect, render
from django.contrib import messages
from portfolio.models import Contact, Blogs, Internship
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def internshipdetails(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'please login to access this page')
        return redirect('/auth/login/')
    
    if request.method == 'POST':
        
        fname = request.POST.get('fullname')
        fusn = request.POST.get('usn')
        femail = request.POST.get('email')
        fcollege_name = request.POST.get('cname')
        f_offer = request.POST.get('offer')
        fstartdate = request.POST.get('startdate')
        fenddate = request.POST.get('enddate')
        fproject_report = request.POST.get('projReport')
        
        # converting the input to upper case
        fname=fname.upper()
        fusn=fusn.upper()
        fcollege_name=fcollege_name.upper()
        f_offer=f_offer.upper()
        fproject_report=fproject_report.upper()
        
        # check if the usn exist in the database
        check1=Internship.objects.filter(usn=fusn)
        check2=Internship.objects.filter(email=femail)
        
        if check1 or check2:
            messages.warning(request, 'your details already exists')
            return redirect('/internshipdtails')
               
        
        query = Internship(fullname=fname, usn=fusn, email=femail, college_name=fcollege_name,
                           offer_status=f_offer, start_date=fstartdate, end_date=fenddate,
                           proj_report=fproject_report)
        query.save()
        messages.success(request,'Form is submitted successfully!')
        return redirect('/internshipdetails')
        
        
    return render(request, 'intern.html')

def contact(request):
    if request.method == "POST":
        get_name = request.POST.get('name')
        get_email = request.POST.get('email')
        get_phone_num = request.POST.get('phone num')
        get_description =request.POST.get('desc')
        query = Contact(name=get_name,email=get_email,phonenumber=get_phone_num,description=get_description)
        query.save()
        messages.success(request, 'Thanks for contacting us, we will get back to you soon')        
        return redirect('/contact')
    
    
    return render(request, 'contact.html')

def handleblog(request):
    posts = Blogs.objects.all()
    context = {"posts":posts}
    
    return render(request, 'blog.html',context)

