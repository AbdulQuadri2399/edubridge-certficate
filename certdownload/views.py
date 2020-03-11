from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Candidate
# Create your views here.
def index(request):
    return render(request, 'certdownload/index.html')

def download(request):
    try:
        candidate = Candidate.objects.get(email=request.POST['email'])
    except (KeyError, Candidate.DoesNotExist):
        return render(request, 'certdownload/index.html', {'error_message': "seems like you didn't take the program or maybe you entered an incorrect email.", })
    else:
        cand_name = candidate.name
        cert_url = "https://res.cloudinary.com/mycloudinaryspace/image/upload/l_text:Satisfy_120_bold:"
        cert_url += cand_name
        cert_url += ",g_center,x_20,y_-170/v1583666291/certificate.pdf"
        return HttpResponseRedirect(cert_url)