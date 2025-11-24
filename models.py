# this file is for the database models
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

# event table
class Event(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    title= db.Column(db.String(150))
    description= db.Column(db.Text)
    start_time= db.Column(db.DateTime)
    end_time= db.Column(db.DateTime)
    allocations= db.relationship("EventResourceAllocation",backref="event",lazy=True)

# resource table
class Resource(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(120))
    type= db.Column(db.String(120))
    allocations= db.relationship("EventResourceAllocation",backref="resource",lazy=True)

# allocation table
class EventResourceAllocation(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    event_id= db.Column(db.Integer,db.ForeignKey("event.id"))
    resource_id= db.Column(db.Integer,db.ForeignKey("resource.id"))
