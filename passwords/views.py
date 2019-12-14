from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AddPasswordForm,SearchForm
from .models import AddPasswordModel
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse
# Create your views here.

def add_password(request):
    if request.method=='POST':
        form=AddPasswordForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('search_passwords'))

    else:
        form=AddPasswordForm()
        return render(request, 'passwords/add.html', {'form':form})

def display_password(request,id):
    password=AddPasswordModel.objects.get(id=id)
    return render(request, 'passwords/display.html', {'required_password':password})

def delete_password(request,id):
    AddPasswordModel.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('search_passwords'))


def search_view(request):
        ctx = {}
        url_parameter = request.GET.get("q")

        if url_parameter:
            passwords = AddPasswordModel.objects.filter(name__icontains=url_parameter)
        else:
            passwords = AddPasswordModel.objects.all()

        ctx["passwords"] = passwords
        #all_passwords=AddPasswordModel.objects.all()
        #ctx["all_passwords"] = all_passwords

        if request.is_ajax():
            html = render_to_string(
                template_name="passwords/password-results-partial.html",  context={"passwords": passwords}
            )

            data_dict = {"html_from_view": html}

            return JsonResponse(data=data_dict, safe=False)

        return render(request, "passwords/view.html", context=ctx)
