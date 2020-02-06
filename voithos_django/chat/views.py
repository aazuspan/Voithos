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
        response = Voithos().respond(request_dict)
        context = {'input': request_dict['input_text'], 'output': response}
        return JsonResponse(context)

    cmd_names = []
    for cmd in Voithos().cmd_handler.cmd_list:
        cmd_names.append(cmd.name)
    context = {'cmd_names': cmd_names}

    return render(request, 'chat/index.html', context=context)


# TODO: Create and pass About template
def about(request):
    return HttpResponse('<h1> ABOUT </h1>')


# TODO: Create and pass Documentation template
def documentation(request):
    return HttpResponse('<h1> DOCUMENTATION </h1>')
