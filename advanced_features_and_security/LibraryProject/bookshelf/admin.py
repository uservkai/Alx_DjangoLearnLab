from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year', 'author')
    
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                'date_of_birth', 'profile_photo'
            ),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields' :('date_of_birth', 'profile_photo'),}),
    )

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)
