from rest_framework import serializers

from apps.music_store.models import Album, Track


class AlbumSerializer(serializers.ModelSerializer):
    """Serializer for Music Albums

    """
    # all tracks related to the album
    tracks = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Track.objects.all()
    )

    class Meta:
        model = Album
        fields = (
            'id',
            'author',
            'title',
            'image',
            'price',
            'tracks',
        )


class TrackSerializer(serializers.ModelSerializer):
    """Serializer for Music Tracks
    """
    # free_version gets data from full_version inside model
    free_version = serializers.ReadOnlyField()

    class Meta:
        model = Track
        fields = (
            'id',
            'author',
            'title',
            'album',
            'price',
            'full_version',
            'free_version',
        )
