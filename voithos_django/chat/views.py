from django.shortcuts import render
from django.http import JsonResponse
from Voithos.Voithos import Voithos


# TODO: Refactor to allow Voithos to persist between calls so that chat history could be preserved
def chat(request):
    """
    Handle the chat page. If a GET request is received with input text, pass it to Voithos and return the Json response
    """
    if request.GET.get('input_text'):
        user_input = request.GET.get('input_text')
        response = Voithos().respond(user_input)
        return JsonResponse({'output': response})

    return render(request, 'chat/index.html')
