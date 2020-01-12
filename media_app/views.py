from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect, reverse
from .models import MyModel



def upload_image(request):
    if request.method == 'POST':
        my_image = request.FILES.get('my_image')
        title = request.POST.get('form_title')
        image_type = request.POST.get('image_type')
        upload = MyModel(
            my_image = my_image,
            title = title,
        )
        upload.save()
        
        return redirect(reverse('index'))

    else:
        images = MyModel.objects.all()
        context = {
            'images':images,
        }
        return render(request, 'index.html', context)






   