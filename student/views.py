from django.shortcuts import render, redirect
from .forms import StudentRegisterForm
from .models import StudentRegister


def student(request):
    if request.method == "POST":
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('http://127.0.0.1:8000/')
            except:
                pass
    else:
        form = StudentRegisterForm()
    return render(request, 'index.html', {'form': form})


def login(request):
    return render(request, 'login.html')


def login_process(request):
    email = request.GET.get('email')
    mobile_number = request.GET.get('number')
    print(email, mobile_number)

    x = StudentRegister.objects.get(email_id=email)
    if email==x.email_id and mobile_number==x.mobile_number:
        print(email,x.email_id, mobile_number, x.mobile_number)

        return render(request, 'show.html', {'student': x})


def edit(request, id):
    student = StudentRegister.objects.get(id=id)
    return render(request, 'edit.html', {'student': student})


def update_success(request):
    return render(request, 'update.html')


def update(request, id):
    student = StudentRegister.objects.get(id=id)
    form = StudentRegisterForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect("update_success")
    return render(request, 'edit.html', {'student': student})





