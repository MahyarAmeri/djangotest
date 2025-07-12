from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import loginForm, massageForm
from django.contrib.auth import authenticate, login, logout
from .models import massage, CountView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from .models import DoorClick
from .serializers import UserSerializer, DoorClickSerializer


def testtt(request):
    pass
def registerUser(request):
    if request.method == 'POST':
        print("ok")
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            Us = User.objects.create_user(username=username, password=password)
            Token.objects.create(user=Us)
            print("ok")
            login(request, Us)
            return redirect('Connect:chat')

    form = loginForm(request.POST)
    return render(request, 'Connect/register.html', {'form': form})

def loginUser(request):
    coun = CountView.objects.get(id=1)
    coun.count +=1
    coun.save()
    if request.method == 'POST':
        print("ok")
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            Us = authenticate(username=username, password=password)
            login(request, Us)
            print("ok")
            return redirect('Connect:chat')

    form = loginForm(request.POST)
    return render(request, 'Connect/login.html', {'form': form, 'coun': coun})


def logoutUser(request):
    logout(request)
    return redirect('Connect:login')


def chat(request):
    if not request.user.is_authenticated:
        return redirect('Connect:login')

    form = massageForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            message = form.cleaned_data['message']
            receiver = form.cleaned_data['receiver']
            sender = request.user
            ms = massage.objects.create(message=message, receiver=receiver, sender=sender)
            return redirect('Connect:chat')

    us = request.user
    massages = massage.objects.filter(receiver=us).order_by('-id')
    massages2 = massage.objects.filter(sender =us).order_by('-id')
    return render(request, 'Connect/chat.html', {'user':request.user, 'massages': massages,'massages2':massages2,'form': form})


class testView(APIView):
    def get(self, request):
        return Response(data='hi')



# class CustomLoginView(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         token = Token.objects.get(key=response.data['token'])
#         return Response({
#             'token': token.key,
#             'username': token.user.username
#         })
#
# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request):
#         request.user.auth_token.delete()
#         return Response({'success': 'Logged out successfully.'})


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        resp = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=resp.data['token'])
        return Response({'token': token.key, 'username': token.user.username, 'is_admin': token.user.is_superuser})

class DoorClickView(APIView):
    def post(self, request):
        DoorClick.objects.create(user=request.user)
        return Response({'status': 'ok'})

class UserListView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        users = User.objects.all()
        return Response(UserSerializer(users, many=True).data)

class UserClicksView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, user_id):
        clicks = DoorClick.objects.filter(user__id=user_id)
        return Response(DoorClickSerializer(clicks, many=True).data)

class CreateUserView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        from django.contrib.auth.models import User
        u = User.objects.create_user(username=request.data['username'], password=request.data['password'])
        return Response({'id': u.id, 'username': u.username})