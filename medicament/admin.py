from django.contrib import admin
from medicament.models import Doc_type, Period, Hosp, Role, Row, Document, TabDocument, Comment
# Register your models here.

admin.site.register(Doc_type)
admin.site.register(Period)
admin.site.register(Hosp)
admin.site.register(Role)
admin.site.register(Row)

#class PhotoInline(admin.TabularInline):     
class TabDocumentInline(admin.TabularInline):
    model = TabDocument
    extra = 0
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class DocumentAdmin(admin.ModelAdmin):
    inlines = [TabDocumentInline, CommentInline]
    


admin.site.register(Document, DocumentAdmin)
    




