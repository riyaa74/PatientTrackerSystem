# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 14:48:10 2023

@author: riyad
"""
import pytest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from hospital.models import Doctor, Patient
from django.core.files.uploadedfile import SimpleUploadedFile
from hospital import forms, models

@pytest.mark.django_db
class TestHomeView(TestCase):
    def setUp(self):
        #Setting up the users
        self.doctor_user = User.objects.create_user(username='testdoctor', password='testpass')
        self.doctor_user.groups.create(name='DOCTOR')

        self.patient_user = User.objects.create_user(username='testpatient', password='testpass')
        self.patient_user.groups.create(name='PATIENT')

        self.admin_user = User.objects.create_user(username='testadmin', password='testpass')
        self.admin_user.groups.create(name='ADMIN')

    def test_authenticated_user_redirect(self):
        # Log in as doctor
        self.client.login(username='testdoctor', password='testpass')

        # MAking a GET request
        response = self.client.get(reverse(''))

        # Checking the response code
        self.assertEqual(response.status_code, 302)

        # Checking that the user is redirected to 'afterlogin'
        self.assertRedirects(response, reverse('afterlogin'))
        
        
    def test_unauthenticated_user_redirect(self):
        # Log in as doctor
        self.client.login(username='testuser', password='testpass')

        # MAking a GET request
        response = self.client.get(reverse(''))

        # Checking the response code
        self.assertEqual(response.status_code, 200)

        # Checking that the user is redirected to main page due to unmatched credentials
        self.assertTemplateUsed(response, 'hospital/index.html')

    def test_logout(self):
        # Log out any authenticated user
        self.client.logout()

        # Making a GET request to home_view
        response = self.client.get(reverse(''))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Checking that the correct template is rendered
        self.assertTemplateUsed(response, 'hospital/index.html')
        

    

    