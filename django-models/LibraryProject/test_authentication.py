#!/usr/bin/env python3
"""
Test script to verify the authentication functionality
"""
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

def test_authentication():
    """Test the authentication views and functionality"""
    client = Client()
    
    print("Testing Authentication System...")
    print("=" * 50)
    
    # Test 1: Home page (should work without authentication)
    print("\n1. Testing Home Page (no auth required)...")
    try:
        response = client.get('/relationship/', HTTP_HOST='localhost')
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Home page accessible without authentication")
        else:
            print("❌ Home page has an issue")
    except Exception as e:
        print(f"❌ Error testing home page: {e}")
    
    # Test 2: Login page
    print("\n2. Testing Login Page...")
    try:
        response = client.get('/relationship/login/', HTTP_HOST='localhost')
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Login page accessible")
        else:
            print("❌ Login page has an issue")
    except Exception as e:
        print(f"❌ Error testing login page: {e}")
    
    # Test 3: Register page
    print("\n3. Testing Register Page...")
    try:
        response = client.get('/relationship/register/', HTTP_HOST='localhost')
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Register page accessible")
        else:
            print("❌ Register page has an issue")
    except Exception as e:
        print(f"❌ Error testing register page: {e}")
    
    # Test 4: Protected pages (should redirect to login)
    print("\n4. Testing Protected Pages (should redirect to login)...")
    try:
        response = client.get('/relationship/books/', HTTP_HOST='localhost')
        print(f"Books page Status Code: {response.status_code}")
        if response.status_code == 302:  # Redirect
            print("✅ Books page properly redirects to login when not authenticated")
        else:
            print("❌ Books page should redirect to login")
    except Exception as e:
        print(f"❌ Error testing books page: {e}")
    
    # Test 5: User registration
    print("\n5. Testing User Registration...")
    try:
        # Create a test user
        test_username = 'testuser'
        test_password = 'testpass123'
        
        # Check if user already exists
        if User.objects.filter(username=test_username).exists():
            print("Test user already exists, skipping registration test")
        else:
            # Test registration
            response = client.post('/relationship/register/', {
                'username': test_username,
                'password1': test_password,
                'password2': test_password,
            }, HTTP_HOST='localhost')
            print(f"Registration Status Code: {response.status_code}")
            if response.status_code == 302:  # Redirect after successful registration
                print("✅ User registration successful")
            else:
                print("❌ User registration failed")
    except Exception as e:
        print(f"❌ Error testing user registration: {e}")
    
    # Test 6: User login
    print("\n6. Testing User Login...")
    try:
        # Try to login with the test user
        response = client.post('/relationship/login/', {
            'username': test_username,
            'password': test_password,
        }, HTTP_HOST='localhost')
        print(f"Login Status Code: {response.status_code}")
        if response.status_code == 302:  # Redirect after successful login
            print("✅ User login successful")
        else:
            print("❌ User login failed")
    except Exception as e:
        print(f"❌ Error testing user login: {e}")
    
    # Test 7: Access protected pages after login
    print("\n7. Testing Protected Pages After Login...")
    try:
        # Login first
        client.login(username=test_username, password=test_password)
        
        # Try to access books page
        response = client.get('/relationship/books/', HTTP_HOST='localhost')
        print(f"Books page after login Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Books page accessible after login")
        else:
            print("❌ Books page should be accessible after login")
    except Exception as e:
        print(f"❌ Error testing protected pages after login: {e}")
    
    # Test 8: Logout
    print("\n8. Testing User Logout...")
    try:
        response = client.get('/relationship/logout/', HTTP_HOST='localhost')
        print(f"Logout Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Logout successful")
        else:
            print("❌ Logout failed")
    except Exception as e:
        print(f"❌ Error testing logout: {e}")
    
    print("\n" + "=" * 50)
    print("Authentication Testing Complete!")
    
    # Clean up test user
    try:
        if User.objects.filter(username=test_username).exists():
            User.objects.filter(username=test_username).delete()
            print(f"Cleaned up test user: {test_username}")
    except Exception as e:
        print(f"Error cleaning up test user: {e}")

if __name__ == "__main__":
    test_authentication() 