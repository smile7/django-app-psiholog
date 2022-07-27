from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Deinosti, Step, Gallery, Certificate, Phase, Contact

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Deinosti)
admin.site.register(Step)
admin.site.register(Gallery)
admin.site.register(Certificate)
admin.site.register(Phase)
admin.site.register(Post, PostAdmin)
admin.site.register(Contact)
