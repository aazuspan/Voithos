from django.shortcuts import render
from django.http import JsonResponse


def chat(request):
    """
    Handle the chat page. If a GET request is received with input text,
    """
    if request.GET.get('input_text'):
        user_input = request.GET.get('input_text')
        # TODO: Pass user input to Voithos and return Voithos response
        return JsonResponse({'output': user_input})

    return render(request, 'chat/index.html')
