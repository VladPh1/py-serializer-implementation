import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serialized_car = CarSerializer(instance=car).data
    bytes_car = json.dumps(serialized_car)
    return bytes_car


def deserialize_car_object(json: bytes) -> Car:
    data_dict = json.loads(json)
    deserialize_car = CarSerializer(data=data_dict)
    deserialize_car.is_valid(raise_exception=True)
    deserialize_car.save()
    return deserialize_car
