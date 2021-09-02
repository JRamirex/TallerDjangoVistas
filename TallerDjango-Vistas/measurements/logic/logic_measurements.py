from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(num:int):
    measurement = Measurement.objects.get(pk=num)
    return measurement

def delete_measurement(num:int):
    borrable = Measurement.objects.get(pk=num)
    borrable.delete()

def update_measurement(num:int, new:int):
    updated = get_measurement(num)
    updated.value =new
    updated.save()
    return updated