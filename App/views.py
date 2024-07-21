from django.shortcuts import render
from PIL import Image
from .models import Photo
from .forms import Photoform

def overlayphoto(request):
    if request.method == 'POST':
        form1 = Photoform(request.POST,request.FILES,prefix='form1')
        form2 = Photoform(request.POST,request.FILES,prefix='form2')
        print("forms initiated")
        if form1.is_valid and form2.is_valid :
            photo1 =form1.save()
            photo2 =form2.save()
            
            #the below code is a pillow functon
            image1 = Image.open(photo1.image.path).convert('RGBA')
            image2 = Image.open(photo2.image.path).convert('RGBA')
            
            #to resize the image
            image1 = image1.resize((800,800))
            image2 = image2.resize((800,800))

            #To adjust opacity of image 2 :
            image2.putalpha(128)

            #for blended image :
            blended = Image.alpha_composite(image1,image2)

            #save the image
            blendedpath = 'media/photos/blended.png'
            blended.save(blendedpath)

            return render(request,'App/result.html',{'path':blendedpath})
    
    #to Uplode image
    else:
        form1 = Photoform(prefix='form1')
        form2 = Photoform(prefix='form2')
    
    return render(request,'App/uplod.html',{"form1":form1,"form2":form2}) 




# Create your views here.
