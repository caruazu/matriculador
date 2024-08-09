from django.http import JsonResponse

def estudante(request):
    if request.method == 'GET': estudante = {
        'id':1,
        'nome':'Gustavo'
    }
    return JsonResponse(estudante);