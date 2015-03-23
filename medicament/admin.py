from django.contrib import admin
from medicament.models import Doc_type, Period, Hosp, Role, Document, Comment, Doc_Hosp
# Register your models here.

admin.site.register(Doc_type)
admin.site.register(Period)
admin.site.register(Hosp)
admin.site.register(Role)
admin.site.register(Doc_Hosp)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class DocumentAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    


admin.site.register(Document, DocumentAdmin)
    




