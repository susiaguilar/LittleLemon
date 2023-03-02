from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics,viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import userSerializer,menuSerializer,bookingSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes



@api_view()

@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})
#token = Token.objects.create(User='susan')
#print(token.key)

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

#class bookingView(APIView):
 #   def get(self, request):
  #      items = Booking.objects.all()
   #     serializer = bookingSerializer(items, many=True)
    #    return Response(seralizer.data) #return JSON
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def post(self, request):
        serializer = menuSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data" : "serializer.data"})

class menuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [permissions.IsAuthenticated] 

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
#class UserViewSet(viewsets.ModelViewSet):
 #  queryset = User.objects.all()
  # serializer_class = UserSerializer
#   permission_classes = [permissions.IsAuthenticated]
   