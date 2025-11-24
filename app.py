from flask import Flask,render_template,request,redirect,flash
from datetime import datetime
from models import db,Event,Resource,EventResourceAllocation
from config import Config

app=Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# db create
with app.app_context():
    db.create_all()

# home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

# view the events
@app.route("/events")
@app.route("/event")
def events():
    all_events=Event.query.all()
    return render_template("events.html",events=all_events)

# add event
@app.route("/add_event",methods=["GET","POST"])
@app.route("/add event",methods=["GET","POST"])
def add_event():    
    if request.method == "POST":
        title=request.form["title"]
        desc=request.form["description"]
        start=datetime.fromisoformat(request.form["start"])
        end=datetime.fromisoformat(request.form["end"])

        if end <= start:
            flash("End time must be after start time")
            return redirect("/add_event")
        new_event=Event(
            title=title,
            description=desc,
            start_time=start,
            end_time=end
        )
        db.session.add(new_event)
        db.session.commit()
        flash("Event added successfully")
        return redirect("/events")
    return render_template("add_event.html")

# view all resource
@app.route("/resources")
def resources():
    all_resources=Resource.query.all()
    return render_template("resources.html",resources=all_resources)

# add resource
@app.route("/add_resource",methods=["GET","POST"])
@app.route("/add resource",methods=["GET","POST"])
def add_resource():
    if request.method == "POST":
        name=request.form["name"]
        rtype=request.form["type"]
        new_resource=Resource(name=name, type=rtype)
        db.session.add(new_resource)
        db.session.commit()
        flash("Resource added successfully")
        return redirect("/resources")
    return render_template("add_resource.html")

# allocate resources to event 
@app.route("/allocate",methods=["GET","POST"])
def allocate():
    events=Event.query.all()
    resources=Resource.query.all()
    if request.method == "POST":
        event_id=request.form["event"]
        resource_id=request.form["resource"]
        event=Event.query.get(event_id)
        resource=Resource.query.get(resource_id)

        # conflict detection
        existing_allocs=EventResourceAllocation.query.filter_by(resource_id=resource_id).all()
        for alloc in existing_allocs:
            other_event=Event.query.get(alloc.event_id)

            if event.start_time < other_event.end_time and event.end_time > other_event.start_time:
                flash("Resource already booked for this time.")
                return redirect("/allocate")

        new_alloc=EventResourceAllocation(event_id=event_id,resource_id=resource_id)
        db.session.add(new_alloc)
        db.session.commit()
        flash("Resource allocated successfully")
        return redirect("/allocate")
    return render_template("allocate.html",events=events,resources=resources)

# resource utilisation report 
@app.route("/report",methods=["GET","POST"])
def report():
    resources=Resource.query.all()
    data=[]
    if request.method == "POST":
        start=datetime.fromisoformat(request.form["start"])
        end=datetime.fromisoformat(request.form["end"])
        for r in resources:
            total_hours=0
            upcoming=[]
            for alloc in r.allocations:
                ev=Event.query.get(alloc.event_id)

                if ev.start_time >= start and ev.end_time <= end:
                    duration=(ev.end_time - ev.start_time).total_seconds()/3600
                    total_hours +=duration

                if ev.start_time > datetime.now():
                    upcoming.append(ev)
            data.append({
                "resource":r,
                "hours":total_hours,
                "upcoming":upcoming
            })
    return render_template("report.html",data=data,resources=resources)

# delete event
@app.route("/delete_event/<int:event_id>")
def delete_event(event_id):
    event=Event.query.get_or_404(event_id)
    for alloc in event.allocations:
        db.session.delete(alloc)
    db.session.delete(event)
    db.session.commit()
    flash("Event deleted successfully")
    return redirect("/events")

# delete resource
@app.route("/delete_resource/<int:resource_id>")
def delete_resource(resource_id):
    resource=Resource.query.get_or_404(resource_id)
    for alloc in resource.allocations:
        db.session.delete(alloc)
    db.session.delete(resource)
    db.session.commit()
    flash("Resource deleted successfully")
    return redirect("/resources")

# edit events
@app.route("/edit_event/<int:event_id>",methods=["GET","POST"])
def edit_event(event_id):
    event=Event.query.get_or_404(event_id)
    if request.method == "POST":
        title=request.form["title"]
        desc=request.form["description"]
        start=datetime.fromisoformat(request.form["start"])
        end=datetime.fromisoformat(request.form["end"])
        if end <= start:
            flash("End time must be after start time")
            return redirect(f"/edit_event/{event_id}")
        for alloc in event.allocations:
            resource_id=alloc.resource_id
            existing_allocs=EventResourceAllocation.query.filter_by(resource_id=resource_id).all()
            for ea in existing_allocs:
                if ea.event_id == event.id:
                    continue 
                other_event=Event.query.get(ea.event_id)
                if start < other_event.end_time and end > other_event.start_time:
                    flash(
                        f"Cannot update. Resource '{alloc.resource.name}'"
                        f"is already allocated to event '{other_event.title}' during this time."
                    )
                    return redirect(f"/edit_event/{event_id}")
        event.title=title
        event.description=desc
        event.start_time=start
        event.end_time=end
        db.session.commit()
        flash("Event updated successfully")
        return redirect("/events")
    return render_template("edit_event.html",event=event)

# edit resources
@app.route("/edit_resource/<int:resource_id>",methods=["GET","POST"])
def edit_resource(resource_id):
    resource=Resource.query.get_or_404(resource_id)
    if request.method == "POST":
        name=request.form["name"]
        rtype=request.form["type"]
        resource.name=name
        resource.type=rtype
        db.session.commit()
        flash("Resource updated successfully")
        return redirect("/resources")
    return render_template("edit_resource.html",resource=resource)


if __name__ == "__main__":
    app.run(debug=True)
