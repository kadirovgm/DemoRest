# это как forms в django (отдать и принимать JSON!!!)
# принимает на вход данные и сириализирует их
# GET (по сути конвертация данных из базы в формат JSON)
# если приходит запрос POST, он преобразует JSON в удобный формат для записи в таблицы БД

from rest_framework import serializers
from cars.models import Car

class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


