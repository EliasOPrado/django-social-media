from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

@login_required
def image_create(request):
    if request.method == 'POST'
        # form sent.
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            # the form data is valid.
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            # Add the current user to the item.
            new_item.user = request.user 
            new_item.save()
            messages.success(request, 'Image added succesfuly!')

            # redirect to new item detail view.
            return redirect(new_item.get_absolute_url())

        else:
            # create the form with data provided from-
            # bookmarklet through http GET.
            form = ImageCreateForm(request.GET)
        context = {'section':'images', 'form':form}
        return render(request, 'images/create.html', context)

