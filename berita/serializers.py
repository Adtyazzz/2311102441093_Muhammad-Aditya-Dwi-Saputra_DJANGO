from rest_framework import serializers
from berita.models import Kategori, Artikel
from django.contrib.auth.models import User
from pengguna.models import Biodata

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class BiodataSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Biodata
        fields = ['user', 'alamat', 'telpon', 'foto']

class KategoritSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id', 'nama']

class ArtikelSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    kategori = serializers.PrimaryKeyRelatedField(queryset=Kategori.objects.all()) 

    kategori_detail = KategoritSerializer(source='kategori', read_only=True)
    author_detail = UserSerializer(source='author', read_only=True)
    class Meta:
        model = Artikel
        fields = ['id', 'judul', 'isi', 'kategori', 'author', 'thumbnail', 'slug', 'kategori_detail', 'author_detail']
        read_only_fields = ('kategori_detail', 'author_detail')
