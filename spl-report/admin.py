from django.contrib import admin
from .models import pyt,user_n,aptitude,category,answers,question,gds,interviewer
# Register your models here.
#admin.site.register(user)
admin.site.register(interviewer)
admin.site.register(answers)
admin.site.register(aptitude)
admin.site.register(user_n)
admin.site.register(question)
admin.site.register(category)
#admin.site.register(resume)
#admin.site.register(essay)
#admin.site.register(pt)
admin.site.register(gds)
admin.site.register(pyt)