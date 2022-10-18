from django.shortcuts import render
from .forms import SendMailForm
from .tasks import SendMailTask
from django.contrib import messages

# Create your views here.

def IndexView(request):

    if request.method == 'POST':
        form = SendMailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            SendMailTask.delay(email, message)
            messages.success(request, 'Your mail has been sent successfuly')

    form = SendMailForm()

    context = {
        'title': 'Mail App',
        'form': form,
    }

    return render(request, 'Mail/index.html', context)
