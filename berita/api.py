from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from berita.serializers import KategoritSerializer, ArtikelSerializer, BiodataSerializer
from berita.models import Kategori, Artikel
from django.contrib.auth.models import User
from pengguna.models import Biodata


@api_view(['GET'])
def api_author_list(request):
    biodata = Biodata.objects.all()
    serializer = BiodataSerializer(biodata, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_kategori_list(request):
    kategori = Kategori.objects.all()
    serializer = KategoritSerializer(kategori, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_kategori_detail(request, id_kategori):
    kategori = Kategori.objects.get(id=id_kategori)
    try:
        serializer = KategoritSerializer(kategori, many=False)
        return Response(serializer.data)
    
    except:
        return Response({'message:data kategori tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND )
    

@api_view(['GET'])
def api_artikel_list(request):
    artikel = Artikel.objects.all()
    serializer = ArtikelSerializer(artikel, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_artikel_detail(request, id_artikel):
    artikel = Artikel.objects.get(id=id_artikel)
    try:
        serializer = ArtikelSerializer(artikel, many=False)
        return Response(serializer.data)
    
    except:
        return Response({'message:data artikel tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND )    