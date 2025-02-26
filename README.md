### VECHICLE RENTAL SYSTEM
The Vehicle Rental System is a web application that allows users to browse, filter, and rent vehicles online. It provides real-time availability updates and an intuitive user experience.

## Features
* User Interface:
    * Dynamic vehicle listing with Bootstrap-based cards.
    * Image carousel for each vehicle.
    * Real-time filters for search refinement.

* Filters & Search:
    * Search by vehicle name.
    * Filter by vehicle type (Car, Bike, Bus, Scooter).
    * Filter by company (Maruti, Audi, Tesla, etc.).
    * Filter by fuel type (Petrol, Electric).
    * Price range filter.

* Booking System:
    * View vehicle details.
    * Redirect to the order page.


## Technologies used
* Frontend: HTML, CSS (Bootstrap), JavaScript
* Backend: Django (Python)
* Database: SQLite 



## folder structure
```
vehicle-rental-system/
│-- requirements.txt
│-- db.sqlite3 (if using SQLite)
│-- main/ (Django App)
│   │-- static/ (CSS, JS, Images)
│   │-- templates/ (HTML Templates)
│   │-- views.py
│   │-- models.py
│   │-- urls.py
|   |-- manage.py
│-- README.md
```

## Setup Instructions

Follow these steps to get the project up and running locally:

### 1. Clone the Repository

Start by cloning the repository to your local machine using the following command:

```bash
git clone https://github.com/red445992/VehicleRental.git
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
```
* And activate the env
```bash
.\venv\Scripts\activate

```

### 3. install dependencies
```bash
pip install -r requirements.txt
```
### 4. apply database migrations
```bash
 python manage.py migrate
```
### 5.Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```
### 6. run the development server
```bash
python manage.py runserver
```


## Future enhancements
* online payement gateway(Esewa)
* customer feedback
* chat system 