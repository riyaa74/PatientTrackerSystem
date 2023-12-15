# PatientTrackerSystem
---

## Running our Project
```
Please run the PatientTrackerDjango folder in code editor
Make your own virtual environment and Install the requirements.txt file 
```
py manage.py makemigrations
py manage.py migrate
python manage.py runserver

http://127.0.0.1:8000/

Steps followed for testing:

1. Installed pytest
pip install pytest-django

2. Added to the path if not there already
3. from the root directory: pytest --ds=hospitalmanagement.settings hospital/test