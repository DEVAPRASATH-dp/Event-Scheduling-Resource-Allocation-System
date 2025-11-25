# Event Scheduling & Resource Allocation System

A simple, clean, and lightweight Flask web application that helps organisations manage events and shared resources without conflicts.  


---

## Features

### Event Management
- Add new events
- Edit existing events
- Delete events
- Event fields:
  - Title  
  - Description  
  - Start Time  
  - End Time  
- Automatic validation ensures **end time must be after start time**
- Events shown in a **clean, structured table**
- Dates shown as **DD/MM/YYYY**
- Time shown in **12-hour format (AM/PM)**

---

### Resource Management
- Add / Edit / Delete resources
- Resource fields:
  - Resource Name  
  - Resource Type (Room, Instructor, Equipment, etc.)
- Displayed in a **modern table UI**

---

### Resource Allocation
- Allocate a resource to an event
- Allocation table contains:
  - Event Name  
  - Resource Name  
  - Status  
  - Edit / Delete actions  
- UI clearly shows what is allocated and to which event

---

### Conflict Detection Logic
The system prevents:
- Double-booking of the same resource
- Time overlaps
- Same start and end time
- Nested overlaps
- Partial overlap between two events

If a conflict exists, the user sees a clear error message.

---

### Resource Utilisation Report
Pick a date range → System calculates:
- Total hours used by each resource
- Upcoming bookings
- Event durations

---

## Tech Stack

| Component | Technology |
|----------|------------|
| Backend  | Flask (Python) |
| Database | SQLite + SQLAlchemy ORM |
| Frontend | HTML, CSS, Jinja2 Templates |
| Styling  | Custom CSS |

---

## Project Structure

```
Event-Scheduling-Resource-Allocation-System/
│
├── app.py
├── config.py
├── models.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── events.html
│   ├── add_event.html
│   ├── edit_event.html
│   ├── resources.html
│   ├── add_resource.html
│   ├── edit_resource.html
│   ├── allocate.html
│   └── report.html
│
└── static/
    └── styles.css
```
---

## How to Use the Application

### ✔ Create Resources
Examples:
- Projector  
- Classroom  
- Trainer  

### ✔ Create Events
Provide:
- Title  
- Description  
- Start Time & End Time  

### ✔ Allocate Resources
Choose:
- Event  
- Resource  
- The system checks for conflicts

### ✔ View Reports
Select a date range to see:
- Utilisation hours  
- Future bookings  

---

## Purpose of This Project
This assignment tests:
- Flask fundamentals  
- Backend logic  
- Database relationships  
- Conflict detection  
- UI design  
- End-to-end project building  

---

## Demo video and Screenshots
Drive Link - https://drive.google.com/drive/folders/15qomVfBNgTlw2HHivUeljlSVKV5bIkpQ?usp=sharing


