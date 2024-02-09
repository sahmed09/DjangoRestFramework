from django.shortcuts import get_object_or_404
from rest_framework import serializers
from gallery.models import *


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ['slug']


class AlbumItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumItems
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('album'):
            self.fields['album'] = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())

            album_name = data['album']['name']
            album = get_object_or_404(Album, name=album_name)

            data['album'] = album.id

        return super(AlbumItemsSerializer, self).to_internal_value(data)
