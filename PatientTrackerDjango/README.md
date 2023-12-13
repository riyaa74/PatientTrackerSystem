
# Hospital Management

### Admin
- Signup 
- Admin can create, view , approve or delete a doctor.
- Admin can create, view , approve or delete patient.
- Can Generate/Download Invoice pdf 
- Can view/book/approve Appointment requested by patien.

### Doctor
- Can signup(if signup, then needs to be aproved by admin).
- Can only view their patient details (symptoms, name, mobile ) assigned to that doctor by admin.
- Can see the patient list for discharged patients.
- Can view their Appointments.
- Can delete their Appointment, when doctor attended their appointment.

### Patient
- Create create account in hospital which needs to be aproved by admin.
- Can see the details of the doctor assigned to him/her
- Can view their booked appointment status (pending/confirmed by admin).
- Can book appointments.(approval required by admin)
- Can view/download Invoice pdf after being discharged by admin

---

## Running our Project
```
Make your own virtual environment and Install the requirements.txt file 
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver

http://127.0.0.1:8000/
```

```
## Drawbacks/LoopHoles
- There should be at least one doctor in hospital before admitting patient. So first add doctor.
- On update page of doctor/patient you must have to update password.



