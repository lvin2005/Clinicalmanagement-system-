from django.shortcuts import render
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            form = ContactForm()
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})
