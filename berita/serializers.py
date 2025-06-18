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
    author = UserSerializer()
    kategori = KategoritSerializer()
    class Meta:
        model = Artikel
        fields = ['id', 'judul', 'isi', 'kategori', 'author', 'thumbnail', 'slug']