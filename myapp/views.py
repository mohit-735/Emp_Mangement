# from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    if request.method == 'POST':
        check = request.POST['check']
        print(check)  

    isActive = True
    name = "Radhe Institude"
    list_of_programs = [
        'Wap a program check even or odd \n'
        'WAP to check prime number\n'
        'Print all prime numbers 1 to 100 \n'
        'WAP to print pascals triangl'
    ]
    student = {
        'student_name': "Mohit",
        'student_college': "xyz",
        'student_city': "Nashik"
    }
    # pass the data in return HOme.html
    data = {
         'isActive': isActive,
         'name': name,
         'list_of_programs': list_of_programs,
         'student_data': student

    }
    # print("test function from view")
    # return HttpResponse("<h1>Hello, this is the index page</h1>")
    # return render(request, "home.html", {})
    return render(request, "home.html", data)


def about(request):
    print("test function from view")
    # return HttpResponse("<h1>Hello, this is the About page</h1>")
    return render(request, "about.html", {})


def service(request):
    print("test function from view")
    # return HttpResponse("<h1>Hello, this is the Service page</h1>")
    return render(request, "Services.html", {})
