from django.shortcuts import render

def index(request):
    return render(request, 'echo_app/index.html')

def echo(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        return render(request, 'echo_app/index.html', {'message': message})
    else:
        return render(request, 'echo_app/index.html')