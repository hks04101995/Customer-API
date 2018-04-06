from rest_framework import serializers
from .models import ResPartner

class customerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResPartner
        fields = ('url','id','name','email',)
