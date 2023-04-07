from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.urls import reverse         #igual al template tag url, importamos reverse para retornar a la misma página de contacto despues de enviar el mensaje
from .forms import ContactForm         #importamos ContactForms del archivo forms.py 

# Create your views here.
def contact(request):
    contact_form=ContactForm
    if request.method=='POST':
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            content=request.POST.get('content','')
            #formatamos el correo
            email=EmailMessage(
                'La Caffettiera: Nuevo mensaje',
                'De {} <{}> \n\n Escribió: \n\n {}'.format(name,email,content),
                'no-contestar@inbox.mailtrap.io',
                ["danbuitrago1@hotmail.com"],
                reply_to=[email]
            )
            #enviamos el mensaje
            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?fail')
            #mensaje enviado
            
    return render(request, 'contact/contact.html',{'form':contact_form})