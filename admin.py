from django.contrib import admin
from home.models import Home
from home.models import Contact
from home.models import Mentalhealth
from home.models import Heartdiseases
from home.models import Covid
from home.models import Immunization

# Register your models here.
admin.site.register(Home)
admin.site.register(Mentalhealth)
admin.site.register(Heartdiseases)
admin.site.register(Covid)
admin.site.register(Immunization)
admin.site.register(Contact)