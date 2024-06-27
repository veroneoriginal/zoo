from django.shortcuts import render


# данные запроса
def index_view(request):
    return render(request, 'mainapp/index.html')
