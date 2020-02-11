from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from Voithos.Voithos import Voithos


# TODO: Refactor to allow Voithos to persist between calls so that chat history could be preserved
def chat(request):
    """
    Handle the chat page. If a GET request is received with input text, pass it to Voithos and return the Json response
    """
    if request.GET.get('input_text'):
        request_dict = request.GET.dict()
        response, response_delay = Voithos().respond(request_dict)
        return JsonResponse({'output': response, 'delay': response_delay})

    return render(request, 'chat/index.html')


# TODO: Create and pass About template
def about(request):
    return HttpResponse('<h1> ABOUT </h1>')


# TODO: Create and pass Documentation template
def documentation(request):
    return HttpResponse('<h1> DOCUMENTATION </h1>')
