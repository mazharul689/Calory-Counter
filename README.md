# Calorie Counter (Django Web Application)

A robust, level-4 specification Calorie Counter web application built using Python and Django. This app allows users to create personal profiles, dynamically calculate their daily Basal Metabolic Rate (BMR) using standard demographic formulas, log daily food consumption, and track remaining metrics via an interactive, responsive user dashboard.

---

## Features

- **User Authentication**: Secure signup with matching password validation and login session management.
- **Dynamic BMR Calculation**: Computes personalized daily caloric targets based on real-time body metric data utilizing gender-specific formulas.
  - **Male formula**: $66.47 + (13.75 \times \text{weight}) + (5.003 \times \text{height}) - (6.755 \times \text{age})$
  - **Female formula**: $655.1 + (9.563 \times \text{weight}) + (1.850 \times \text{height}) - (4.676 \times \text{age})$
- **Real-Time Dashboard Tracking**: High-visibility metric cards outlining target limits, current total consumption, and live dynamically styled budget variances.
- **Consumption History Logs**: Tabular history tracker equipped with smooth layout row highlighting using Bootstrap 5 classes.
- **Bulletproof Fallback System**: Safely handles initialization states for newly registered users lacking existing profile records or consumption logs.

---

## Technical Stack

- **Backend Framework**: Django (Python)
- **Database Layer**: SQLite / Object-Relational Mapping (ORM)
- **Frontend Framework**: Bootstrap 5
- **Template Engine**: Native Django Template Language (DTL)

---

## Project Structure & Data Models

The project structure adheres to standard architecture conventions (`Name_ID_CaloryCounter` containing a core operational app module).

### 1. `UserModel`
Extended using Django's standard authentication framework components:
- Standard username, email, password fields.

### 2. `ProfileModel`
Maps one-to-one to the authenticated application user:
- `user`: `OneToOneField` linking directly to the primary user entity.
- `firstName` & `lastName`: User identification character fields (`max_length=200`).
- `gender`: Character selector restricted via choice validation configurations (`Male` / `Female`).
- `age`: Basic application tracking integer configuration.
- `height` & `weight`: Highly accurate numerical measurements capturing user dimensions (`In CM` & `In KG`).
- `bmr`: Persistent value populated dynamically upon profile modifications.

### 3. `CaloryConsumptionModel`
Contains all active daily dietary entries:
- `user`: Foreign Key establishing relational constraints with the parent User model instance.
- `itemName`: Identifier text tag characterizing the input meal item.
- `calory`: Precision floating-point record tracking metric unit values.

---

## Quick Installation & Local Deployment

Follow these quick steps to launch the application workspace locally.

## 🚦 Installation

### Clone Repository

```bash
git clone https://github.com/mazharul689/Calory-Counter.git
cd Calory-Counter
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Development Server

```bash
python manage.py runserver
```
---
