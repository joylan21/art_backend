from rest_framework import serializers
from .models import Author, Art, Category

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ArtSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Art
        fields = '__all__'

    def get_author(self, obj):
        return {
            'id' : obj.author.id,
            'name' : obj.author.name
        }
    
    def get_category(self, obj):
        return {
            'id' : obj.category.id,
            'name' : obj.category.name
        }

