from django.contrib import admin
from .models import categories, product, Added_by, event
# Register your models here.
admin.site.register(categories)
admin.site.register(product)
admin.site.register(Added_by)
admin.site.register(event)