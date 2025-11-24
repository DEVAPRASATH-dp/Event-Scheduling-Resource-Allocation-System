# Event-Scheduling-Resource-Allocation-System

This is a small Flask web application built for managing events and shared resources inside an organisation.
It helps schedule workshops, meetings, classes and assign resources like rooms, instructors, or equipment without conflicts.

The app focuses on being simple, clean, and easy to use.

Features
Event Management

Add new events

Edit and delete events

Includes event title, description, start time and end time

Shows events in a clean table format

Time is displayed in day/month/year + 12-hour format

Resource Management

Add different types of resources

Edit and delete resources

Resource type can be room, instructor, equipment, etc.

Structured table view for better readability

Resource Allocation

Allocate a resource to an event

Edit or delete allocations

Allocation table shows:

Event Name

Resource Name

Status (Allocated)

Actions

Conflict Detection

The system prevents:

Double-booking of a resource

Overlapping event timings

Cases like:

same start/end time

nested events

partial overlaps

A warning is shown if a conflict occurs.

Resource Utilisation Report

Users can:

Select a date range

View the total number of hours each resource is used

View upcoming bookings

Technology Used

Python (Flask framework)

SQLite (default lightweight database)

HTML, CSS, Jinja2

Bootstrap-like custom UI styling

Project Structure
Event-Scheduling-Resource-Allocation-System/
│
├── app.py
├── requirements.txt
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

How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Start Flask server
python app.py

3️⃣ Open in browser
http://127.0.0.1:5000/

How to Use the System
1. Create Resources

Add all required resources first:

Rooms

Instructors

Equipment

2. Create Events

Add events with:

Title

Description

Start & End times

3. Allocate Resources

Choose an event → choose a resource → allocate.
If the time overlaps with another booked event, the system will warn you.

4. View Reports

Select a date range to see:

Total hours used

Upcoming allocations

Purpose of the Project

This project was created as part of a hiring test.
It demonstrates:

Understanding of Flask

Backend logic with validation

Database relationships

UI building

Conflict detection logic

Ability to build a full working web application independently

Possible Future Enhancements

User login system

Calendar view for events

Filtering and search

Multiple resource allocation at once

Notification system