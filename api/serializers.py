from rest_framework import serializers
from dashboard.models import Xodim, Davomat

class XodimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodim
        fields = '__all__'

class DavomatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = '__all__'
