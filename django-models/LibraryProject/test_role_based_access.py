#!/usr/bin/env python3
"""
Test script to verify role-based access control functionality
"""
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from relationship_app.models import UserProfile

def test_role_based_access():
    """Test the role-based access control system"""
    client = Client()
    
    print("Testing Role-Based Access Control...")
    print("=" * 50)
    
    # Test 1: Create users with different roles
    print("\n1. Creating test users with different roles...")
    
    # Create Admin user
    admin_user = User.objects.create_user(username='admin_user', password='adminpass123')
    admin_profile = UserProfile.objects.get(user=admin_user)
    admin_profile.role = 'Admin'
    admin_profile.save()
    print(f"✅ Created Admin user: {admin_user.username}")
    
    # Create Librarian user
    librarian_user = User.objects.create_user(username='librarian_user', password='librarianpass123')
    librarian_profile = UserProfile.objects.get(user=librarian_user)
    librarian_profile.role = 'Librarian'
    librarian_profile.save()
    print(f"✅ Created Librarian user: {librarian_user.username}")
    
    # Create Member user
    member_user = User.objects.create_user(username='member_user', password='memberpass123')
    member_profile = UserProfile.objects.get(user=member_user)
    member_profile.role = 'Member'
    member_profile.save()
    print(f"✅ Created Member user: {member_user.username}")
    
    # Test 2: Test Admin access
    print("\n2. Testing Admin access...")
    try:
        # Login as admin
        client.login(username='admin_user', password='adminpass123')
        
        # Try to access admin view
        response = client.get('/relationship/admin/', HTTP_HOST='localhost')
        print(f"Admin view Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Admin can access admin view")
        else:
            print("❌ Admin cannot access admin view")
            
        # Try to access librarian view (should be denied)
        response = client.get('/relationship/librarian/', HTTP_HOST='localhost')
        print(f"Librarian view from Admin Status Code: {response.status_code}")
        if response.status_code == 403:
            print("✅ Admin correctly denied access to librarian view")
        else:
            print("❌ Admin incorrectly allowed access to librarian view")
            
    except Exception as e:
        print(f"❌ Error testing admin access: {e}")
    
    # Test 3: Test Librarian access
    print("\n3. Testing Librarian access...")
    try:
        # Login as librarian
        client.login(username='librarian_user', password='librarianpass123')
        
        # Try to access librarian view
        response = client.get('/relationship/librarian/', HTTP_HOST='localhost')
        print(f"Librarian view Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Librarian can access librarian view")
        else:
            print("❌ Librarian cannot access librarian view")
            
        # Try to access admin view (should be denied)
        response = client.get('/relationship/admin/', HTTP_HOST='localhost')
        print(f"Admin view from Librarian Status Code: {response.status_code}")
        if response.status_code == 403:
            print("✅ Librarian correctly denied access to admin view")
        else:
            print("❌ Librarian incorrectly allowed access to admin view")
            
    except Exception as e:
        print(f"❌ Error testing librarian access: {e}")
    
    # Test 4: Test Member access
    print("\n4. Testing Member access...")
    try:
        # Login as member
        client.login(username='member_user', password='memberpass123')
        
        # Try to access member view
        response = client.get('/relationship/member/', HTTP_HOST='localhost')
        print(f"Member view Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Member can access member view")
        else:
            print("❌ Member cannot access member view")
            
        # Try to access admin view (should be denied)
        response = client.get('/relationship/admin/', HTTP_HOST='localhost')
        print(f"Admin view from Member Status Code: {response.status_code}")
        if response.status_code == 403:
            print("✅ Member correctly denied access to admin view")
        else:
            print("❌ Member incorrectly allowed access to admin view")
            
    except Exception as e:
        print(f"❌ Error testing member access: {e}")
    
    # Test 5: Test unauthenticated access
    print("\n5. Testing unauthenticated access...")
    try:
        # Logout
        client.logout()
        
        # Try to access role-based views without authentication
        views_to_test = ['/relationship/admin/', '/relationship/librarian/', '/relationship/member/']
        for view_url in views_to_test:
            response = client.get(view_url, HTTP_HOST='localhost')
            print(f"{view_url} Status Code: {response.status_code}")
            if response.status_code == 302:  # Redirect to login
                print(f"✅ Unauthenticated access correctly redirected for {view_url}")
            else:
                print(f"❌ Unauthenticated access not properly handled for {view_url}")
                
    except Exception as e:
        print(f"❌ Error testing unauthenticated access: {e}")
    
    print("\n" + "=" * 50)
    print("Role-Based Access Control Testing Complete!")
    
    # Clean up test users
    try:
        User.objects.filter(username__in=['admin_user', 'librarian_user', 'member_user']).delete()
        print("Cleaned up test users")
    except Exception as e:
        print(f"Error cleaning up test users: {e}")

if __name__ == "__main__":
    test_role_based_access() 