# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 12:40:18 2023

@author: riyad
"""

import pytest
from django.contrib.auth.models import User
from hospital.models import Doctor, Patient, Appointment, PatientDischargeDetails

@pytest.mark.django_db
class TestDoctorModel:
    def test_get_name(self):
        user = User.objects.create(first_name='John', last_name='Doe')
        doctor = Doctor.objects.create(user=user, address='Test Address', mobile='1234567890', department='Cardiologist')
        assert doctor.get_name == 'John Doe'
        
    def test_get_id(self):
        user = User.objects.create(first_name='John', last_name='Doe')
        doctor = Doctor.objects.create(user=user, address='Test Address', mobile='1234567890', department='Cardiologist')
        assert doctor.get_id == user.id

    def test_str_method(self):
        user = User.objects.create(first_name='John', last_name='Doe')
        doctor = Doctor.objects.create(user=user, address='Test Address', mobile='1234567890', department='Cardiologist')
        assert str(doctor) == 'John (Cardiologist)'
        
@pytest.mark.django_db
class TestPatientModel:
    def test_get_name(self):
        user = User.objects.create(first_name='John', last_name='Doe')
        patient = Patient.objects.create(user=user, address='Test Address', mobile='1234567890', symptoms='Fever')
        assert patient.get_name == 'John Doe'
    
    def test_get_id(self):
        user = User.objects.create(first_name='John', last_name='Doe')
        patient = Patient.objects.create(user=user, address='Test Address', mobile='1234567890', symptoms='Fever')
        assert patient.get_id == user.id

    def test_str_method(self):
        user = User.objects.create(first_name='John', last_name='Doe')
        patient = Patient.objects.create(user=user, address='Test Address', mobile='1234567890', symptoms='Fever')
        assert str(patient) == 'John (Fever)'

    def test_patient_creation(self):
        user = User.objects.create(first_name='Jane', last_name='Smith')
        patient = Patient.objects.create(user=user, address='Another Address', mobile='9876543210', symptoms='Cough')
        assert patient.get_name == 'Jane Smith'
        assert patient.get_id == user.id
        assert str(patient) == 'Jane (Cough)'
        assert patient.admitDate is not None
        assert patient.status is False
    
    def test_patient_without_mobile(self):
        user = User.objects.create(first_name='John', last_name='Doe')
        patient = Patient.objects.create(user=user, address='Test Address', symptoms='Headache')
        assert patient.mobile == ''
        
    def test_patient_without_symptoms(self):
        user = User.objects.create(first_name='John', last_name='Doe')
        patient = Patient.objects.create(user=user, address='Test Address', mobile='1234567890')
        assert patient.symptoms == ''
        

