from django.contrib import admin
from medicament.models import Doc_type, Period, Hosp, Region, Role, Document, Comment, Doc_Hosp, Doc1
# Register your models here.

admin.site.register(Doc_type)
admin.site.register(Period)
admin.site.register(Region)
admin.site.register(Hosp)
admin.site.register(Role)
admin.site.register(Doc_Hosp)
admin.site.register(Doc1)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class DocumentAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    


admin.site.register(Document, DocumentAdmin)
    




