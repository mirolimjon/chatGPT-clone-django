from django.shortcuts import render
from django.http import JsonResponse
from .openai_service import generate_text
from .models import Chat
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def chatView(request):
    user = request.user
    chats = Chat.objects.filter(user=user)
    Chat.objects.filter(id__in = Chat.objects.filter(user=user).order_by('-id').values('pk')[10:]).delete()
    if request.method == "POST":
        message = request.POST.get('message')
        response = generate_text(message)
        new_chat = Chat.objects.create(
            user = user,
            message=message,
            response=response
        )
        new_chat.save()
        return JsonResponse({
            'message': message,
            'response': response,
        })
    return render(request, 'chat.html', {'chats': chats})
