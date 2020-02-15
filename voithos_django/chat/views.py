from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from Voithos.Voithos import Voithos


def chat(request):
    """
    Handle the chat page. If a GET request is received with input text, pass it to Voithos and return the Json response
    """
    if request.GET.get('input_text'):
        request_dict = request.GET.dict()
        response, response_delay = Voithos().respond(request_dict)
        return JsonResponse({'output': response, 'delay': response_delay})

    return render(request, 'chat/index.html')
