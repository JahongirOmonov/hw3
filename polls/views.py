from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import BemorSerializer
from rest_framework.response import Response
from .models import BemorModel
from django.shortcuts import get_object_or_404


# Create your views here.

class YangiKasal(APIView):
    def post(self, request, *args, **kwargs):
        if str(request.user) != "AnonymousUser":
            if request.user.roles == 2:
                serialzier = BemorSerializer(data=request.data)
                if serialzier.is_valid():
                    serialzier.save()
                    return Response(serialzier.data)
                return Response(serialzier.errors)
        return Response({"msg":"Faqat lor duxtur yarata oladi"})
    

class KasallarRoyhati(APIView):
    def get(self, request, *args, **kwargs):
        # print(self.request.user)
        # print(request.user, type(request.user), str(request.user))
        # print(request.user.roles, type(request.user.roles))
        if str(request.user) != "AnonymousUser":
            print(self.request.user.roles)
            x = BemorModel.objects.filter(status=True)
            serializer=BemorSerializer(x, many=True)
            return Response(serializer.data)
        return Response({'msg':'Chiqib ket'})
    
class OzgarganKasallar(APIView):
    def patch(self, request, *args, **kwargs):
        if str(request.user) != "AnonymousUser":
            if request.user.roles == 3:
                x= get_object_or_404(BemorModel, id=kwargs['forid'])
                serializer=BemorSerializer(x, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
        return Response("Faqat tish duxtur davolay oladi")