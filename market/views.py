from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from market.forms import PublishItemForm
from market.models import Item


def publish_item(request):
    if request.method == 'GET':
        # create form to render and return it
        form = PublishItemForm()
        return render(request, 'publish_item.html', {'form': form})

    elif request.method == 'POST':
        # check if the form is valid
        form = PublishItemForm(request.POST)

        if form.is_valid():
            template = 'home.html'
            try:
                Item.publish(**form.cleaned_data)
                template = 'home.html'
                context = {'title': 'Success',
                           'message': 'Great! Your account was created, now please check your email to '
                                      'activate your account.'}
            except Exception as e:
                template = 'publish_item.html'
                context = {'title': 'Error',
                           'message': 'Error %s.' % (e)}

            return render(request, template, context)

        else:
            # show errors and redirect to form
            # messages.error(request, 'Invalid form data')
            response = redirect(reverse('publish_form'))

        return response
