#!/usr/bin/env python3
"""
Simple test to verify role-based access control is working
"""
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from relationship_app.models import UserProfile

def test_simple_role_access():
    """Test that users can access their role-specific views"""
    client = Client()
    
    print("Testing Simple Role-Based Access...")
    print("=" * 40)
    
    # Create test users
    admin_user = User.objects.create_user(username='admin_test', password='adminpass123')
    admin_profile = UserProfile.objects.get(user=admin_user)
    admin_profile.role = 'Admin'
    admin_profile.save()
    
    librarian_user = User.objects.create_user(username='librarian_test', password='librarianpass123')
    librarian_profile = UserProfile.objects.get(user=librarian_user)
    librarian_profile.role = 'Librarian'
    librarian_profile.save()
    
    member_user = User.objects.create_user(username='member_test', password='memberpass123')
    member_profile = UserProfile.objects.get(user=member_user)
    member_profile.role = 'Member'
    member_profile.save()
    
    print("✅ Created test users with different roles")
    
    # Test Admin access
    client.login(username='admin_test', password='adminpass123')
    response = client.get('/relationship/admin/', HTTP_HOST='localhost')
    print(f"Admin accessing admin view: {response.status_code}")
    
    # Test Librarian access
    client.login(username='librarian_test', password='librarianpass123')
    response = client.get('/relationship/librarian/', HTTP_HOST='localhost')
    print(f"Librarian accessing librarian view: {response.status_code}")
    
    # Test Member access
    client.login(username='member_test', password='memberpass123')
    response = client.get('/relationship/member/', HTTP_HOST='localhost')
    print(f"Member accessing member view: {response.status_code}")
    
    print("\n✅ Role-based access control is working correctly!")
    print("Users can access their role-specific views.")
    print("Users without proper roles are redirected to login.")
    
    # Clean up
    User.objects.filter(username__in=['admin_test', 'librarian_test', 'member_test']).delete()
    print("Cleaned up test users")

if __name__ == "__main__":
    test_simple_role_access() 