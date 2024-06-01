from django.contrib import admin
from .models import Patient, Appoinment, Hospital, Opd, Medicine, CheckupResult, MedicineStore

admin.site.register(Patient)
admin.site.register(Appoinment)
admin.site.register(Hospital)
admin.site.register(Opd)
admin.site.register(Medicine)
admin.site.register(CheckupResult)
admin.site.register(MedicineStore)