# Patient Tracker System

### Admin
- Signup 
- Admin can create, view , approve or delete a doctor.
- Admin can create, view , approve or delete patient.
- Can Generate/Download Invoice pdf 
- Can view/book/approve Appointment requested by patient.

### Doctor
- Can signup(if signup, then needs to be aproved by admin).
- Can only view their patient details (symptoms, name, mobile ) assigned to that doctor by admin.
- Can see the patient list for discharged patients.
- Can view their Appointments.
- Can delete their Appointment.

### Patient
- Create account in hospital which needs to be aproved by admin.
- Can see the details of the doctor assigned to him/her.
- Can view their booked appointment status (pending/confirmed by admin).
- Can book appointments.(approval required by admin)
- Can view/download Invoice pdf after being discharged by admin.

---

## Running our Project
```
Make your own virtual environment and Install the requirements.txt file 
```
py manage.py makemigrations
py manage.py migrate
python manage.py runserver

http://127.0.0.1:8000/

## Steps followed for testing:

1. Installed pytest
pip install pytest-django

2. Added to the path if not there already
3. from the root directory: pytest --ds=hospitalmanagement.settings hospital/test

