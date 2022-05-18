from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name',
                    'date_of_birth', 'date_of_death']


class BookAdmin(admin.ModelAdmin):
    pass


class BookInstanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
admin.site.register(BookInstance, BookInstanceAdmin)

