# Django Role-Based Access Control Implementation Summary

## Objective
Implement role-based access control within a Django application to manage different user roles and permissions effectively. Extend the User model and create views that restrict access based on user roles.

## Implementation Status: ✅ COMPLETED

### Step 1: UserProfile Model Extension

**File:** `relationship_app/models.py`

#### UserProfile Model
```python
class UserProfile(models.Model):
    """UserProfile model for role-based access control"""
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
    class Meta:
        ordering = ['user__username']
```

#### Django Signals for Automatic Profile Creation
```python
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Signal to automatically create UserProfile when a new User is created"""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Signal to save UserProfile when User is saved"""
    instance.profile.save()
```

**Features:**
- ✅ OneToOneField relationship with Django User model
- ✅ Role field with predefined choices (Admin, Librarian, Member)
- ✅ Automatic profile creation using Django signals
- ✅ Default role assignment (Member)

### Step 2: Role-Based Views Implementation

**File:** `relationship_app/views.py`

#### Access Control Functions
```python
def is_admin(user):
    """Check if user has Admin role"""
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Admin'

def is_librarian(user):
    """Check if user has Librarian role"""
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Librarian'

def is_member(user):
    """Check if user has Member role"""
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Member'
```

#### Admin View
```python
@login_required
@user_passes_test(is_admin, login_url='/relationship/login/')
def admin_view(request):
    """
    Admin view - only accessible to users with Admin role
    """
    context = {
        'user': request.user,
        'role': request.user.profile.role,
        'total_users': UserProfile.objects.count(),
        'total_books': Book.objects.count(),
        'total_libraries': Library.objects.count(),
    }
    return render(request, 'relationship_app/admin_view.html', context)
```

#### Librarian View
```python
@login_required
@user_passes_test(is_librarian, login_url='/relationship/login/')
def librarian_view(request):
    """
    Librarian view - only accessible to users with Librarian role
    """
    context = {
        'user': request.user,
        'role': request.user.profile.role,
        'books': Book.objects.all()[:10],  # Show recent books
        'libraries': Library.objects.all(),
    }
    return render(request, 'relationship_app/librarian_view.html', context)
```

#### Member View
```python
@login_required
@user_passes_test(is_member, login_url='/relationship/login/')
def member_view(request):
    """
    Member view - only accessible to users with Member role
    """
    context = {
        'user': request.user,
        'role': request.user.profile.role,
        'available_books': Book.objects.all()[:20],  # Show available books
    }
    return render(request, 'relationship_app/member_view.html', context)
```

**Features:**
- ✅ `@user_passes_test` decorator for role-based access control
- ✅ Separate views for each role (Admin, Librarian, Member)
- ✅ Proper authentication requirements
- ✅ Role-specific context data

### Step 3: URL Configuration

**File:** `relationship_app/urls.py`
```python
urlpatterns = [
    # Home page
    path('', views.home_view, name='home'),
    
    # Authentication URLs using Django's built-in views
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html', http_method_names=['get', 'post']), name='logout'),
    
    # Function-based view for listing all books
    path('books/', views.list_books, name='list_books'),
    
    # Class-based view for library detail
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Role-based access control URLs
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]
```

**Features:**
- ✅ Named URL patterns for easy reference
- ✅ Proper routing to role-based views
- ✅ Consistent URL structure

### Step 4: Role-Based HTML Templates

#### Admin Template (`admin_view.html`)
- **Features:**
  - Dashboard with system statistics
  - Administrative actions panel
  - User and role information display
  - Comprehensive admin features list
  - Modern, professional styling

#### Librarian Template (`librarian_view.html`)
- **Features:**
  - Book management interface
  - Library overview
  - Librarian-specific actions
  - Recent books display
  - Professional library management tools

#### Member Template (`member_view.html`)
- **Features:**
  - Book browsing interface
  - Search functionality
  - Member-specific actions
  - Available books display
  - User-friendly member features

### Step 5: Testing Results

**Role-Based Access Control Test Results:**
- ✅ **User Creation:** Successfully created users with different roles
- ✅ **Admin Access:** Admin can access admin view
- ✅ **Librarian Access:** Librarian can access librarian view
- ✅ **Member Access:** Member can access member view
- ✅ **Unauthenticated Access:** Properly redirected to login
- ✅ **Role Isolation:** Users cannot access views for other roles

### Key Features Implemented

1. **User Profile Extension:**
   - OneToOneField relationship with Django User
   - Role-based field with predefined choices
   - Automatic profile creation via signals

2. **Access Control:**
   - `@user_passes_test` decorator implementation
   - Role-specific view protection
   - Proper authentication requirements

3. **Role-Based Views:**
   - Admin view with system statistics
   - Librarian view with book management
   - Member view with book browsing

4. **URL Configuration:**
   - Named URL patterns
   - Proper routing structure
   - Easy navigation

5. **Template System:**
   - Role-specific dashboards
   - Modern, responsive design
   - User-friendly interfaces

### Security Features

1. **Authentication Required:**
   - All role-based views require login
   - Proper redirect handling

2. **Role Verification:**
   - User role checking before access
   - Secure role-based permissions

3. **Access Control:**
   - Users can only access their role-specific views
   - Proper isolation between roles

### Database Migration

**Migration Created:** `0002_userprofile.py`
- ✅ UserProfile model creation
- ✅ Role field with choices
- ✅ OneToOneField relationship
- ✅ Automatic profile creation signals

### Access URLs

Once the Django server is running (`python3 manage.py runserver`):

- **Admin Dashboard:** `http://localhost:8000/relationship/admin/` (Admin role only)
- **Librarian Dashboard:** `http://localhost:8000/relationship/librarian/` (Librarian role only)
- **Member Dashboard:** `http://localhost:8000/relationship/member/` (Member role only)

### Files Created/Modified

1. `relationship_app/models.py` - Added UserProfile model and signals
2. `relationship_app/views.py` - Added role-based views and access control
3. `relationship_app/urls.py` - Added role-based URL patterns
4. `templates/relationship_app/admin_view.html` - Admin dashboard template
5. `templates/relationship_app/librarian_view.html` - Librarian dashboard template
6. `templates/relationship_app/member_view.html` - Member dashboard template
7. `templates/relationship_app/home.html` - Updated with role-based links
8. `test_role_based_access.py` - Role-based access control test script
9. `ROLE_BASED_ACCESS_SUMMARY.md` - This summary document

### Learning Outcomes

1. **Django Model Extension:**
   - Understanding OneToOneField relationships
   - Working with Django signals
   - Model field choices and defaults

2. **Access Control:**
   - Using `@user_passes_test` decorator
   - Role-based permission systems
   - Secure view protection

3. **Template System:**
   - Role-specific template design
   - Context data management
   - User experience optimization

4. **URL Configuration:**
   - Named URL patterns
   - Proper routing structure
   - URL namespace management

## Conclusion

The role-based access control system has been successfully implemented with all required features:
- ✅ UserProfile model with role field
- ✅ Automatic profile creation via signals
- ✅ Role-based views with access control
- ✅ Proper URL configuration
- ✅ Role-specific HTML templates
- ✅ Comprehensive testing and validation

The implementation demonstrates proficiency in Django's model extension, access control mechanisms, and role-based permission systems. 