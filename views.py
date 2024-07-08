from django.shortcuts import render, HttpResponse
from home.models import Home,Contact
from home.models import Mentalhealth,Heartdiseases,Covid,Immunization
# Create your views here.
def first(request):
    return render(request,'index.html')

def bloglist(request):
    return render(request,'bloglist.html')

def home(request):
    homes = Home.objects.all()
    context = {'homes': homes}
    return render(request,'bloghome.html',context)

def mentalhealth(request):
    mentalhealths = Mentalhealth.objects.all()
    context = {'mentalhealths': mentalhealths}
    return render(request, 'blogmentalhealth.html', context)

def heartdiseases(request):
    heartdiseasess = Heartdiseases.objects.all()
    context = {'heartdiseasess': heartdiseasess}
    return render(request, 'blogheartdiseases.html', context)

def covid(request):
    covids = Covid.objects.all()
    context = {'covids': covids}
    return render(request,'blogcovid.html', context)

def immunization(request):
    immunizations = Immunization.objects.all()
    context = {'immunizations': immunizations}
    return render(request, 'blogimmunization.html', context)

def search(request):
    return render(request,'search.html')

def blogpost(request,slug):
    home = Home.objects.filter(slug=slug).first()
    context = {'home': home}
    return render(request,'blogpost.html',context)

def mentalpost(request,slug):
    mentalhealth = Mentalhealth.objects.filter(slug=slug).first()
    context = {'mentalhealth': mentalhealth}
    return render(request, 'mentalpost.html', context)

def heartpost(request,slug):
    heartdiseases = Heartdiseases.objects.filter(slug=slug).first()
    context = {'heartdiseases': heartdiseases}
    return render(request, 'heartpost.html', context)

def covidpost(request,slug):
    covid = Covid.objects.filter(slug=slug).first()
    context = {'covid': covid}
    return render(request, 'covidpost.html', context)

def immunizationpost(request,slug):
    immunization = Immunization.objects.filter(slug=slug).first()
    context = {'immunization': immunization}
    return render(request, 'immunizationpost.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        instance = Contact(name=name, email=email)
        instance.save()
    return render(request,'contact.html')
