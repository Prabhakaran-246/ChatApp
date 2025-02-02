from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

def room(request,room):
    username=request.GET["username"]
    roomdetails=Room.objects.get(name=room)
    return render(request,"room.html",{"roomname":room,"username":username,"room_details":roomdetails})

def checkroom(request):
    room=request.POST["room_name"]
    username=request.POST["username"]

    if Room.objects.filter(name=room).exists():
        return redirect("/"+room+"/?username="+username)
    else:
        new_room=Room.objects.create(name=room)
        new_room.save()
        return redirect("/"+room+"/?username="+username)

def send(request):
    message=request.POST["message"]
    user_name=request.POST["username"]
    roomid=request.POST["room_id"]

    new_message=Message.objects.create(value=message,room=roomid,user=user_name)
    new_message.save()
    return HttpResponse("Message sent Successfully..")

def getMessages(request,room):

    roomdetails=Room.objects.get(name=room)

    message=Message.objects.filter(room=roomdetails.id)
    print("loaded")
    return JsonResponse({"messages":list(message.values())})
