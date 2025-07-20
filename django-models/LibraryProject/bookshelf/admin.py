from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # List view customizations
    list_display = ['title', 'author', 'publication_year', 'get_age']
    search_fields = ['title', 'author']
    list_filter = ['author', 'publication_year']
    ordering = ['title']
    list_per_page = 25
    list_display_links = ['title']
    
    # Form customizations
    fields = ['title', 'author', 'publication_year']
    
    # Add custom method to display book age
    def get_age(self, obj):
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - obj.publication_year
    get_age.short_description = 'Age (Years)'
    get_age.admin_order_field = 'publication_year'
    
    # Customize the change list page
    list_editable = []  # Fields that can be edited directly in the list
    date_hierarchy = None  # Would be used if you had DateTimeField
    
    # Add actions
    actions = ['make_published_recently']
    
    def make_published_recently(self, request, queryset):
        # Custom action example
        count = queryset.filter(publication_year__gte=2020).count()
        self.message_user(request, f'{count} books were published recently.')
    make_published_recently.short_description = 'Mark as recently published'