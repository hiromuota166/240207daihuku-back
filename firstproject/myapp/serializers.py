# モデルのデータをJSON形式でクライアントに送信できるようにします。
from rest_framework import serializers
from .models import YourModel  # YourModelは実際のモデル名に置き換えてください

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        fields = '__all__'  # 必要なフィールドに限定することもできます

