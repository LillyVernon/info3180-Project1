"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os 
from app import app
from flask import render_template, request, redirect, url_for, session, abort, send_from_directory
from .forms import MyForm
from flask import Flask, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from app import db
from app.models import Property
import base64



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


''' @app.route('/property', methods=['POST', 'GET'])
def property():
    form=MyForm()
    if request.method == 'POST' and form.validate_on_submit():
        photo=request.files['photo']
        filename=secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File Saved', 'success')
        return redirect(url_for('home'))
    return render_template('property.html',form=form) '''


@app.route('/property', methods=['POST', 'GET'])
def property():
    form=MyForm()
    if request.method == 'POST' and form.validate_on_submit():
        #photo=request.files['photo']
        photo=form.photo.data
        filename=secure_filename(photo.filename)
        typevalue=dict(form.propertyType.choices).get(form.propertyType.data)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        property=Property(request.form['title'],request.form['description'], request.form['rooms'],
        request.form['bathroom'],request.form['price'],
        request.form['propertyType'], request.form['location'], filename)
        #photo1=request.file['photo'].read()
        db.session.add(property)
        db.session.commit()
        flash('Propery was sucessfully added', 'success')
        return redirect(url_for('properties'))
    flash_errors(form)
    return render_template('property.html',form=form)


@app.route('/property/<propertyid>', methods=['get'])
def individualproperty(propertyid):
    query=db.session.query(Property).filter_by(id=propertyid)
    if request.method=='get':
        print(request.form['button'])
    return render_template('individualproperty.html',query=query)

''' @app.route('/properties')
def property():
 property = db.session.query(Property).all()
 return render_template('show_users.html',property=property) '''



def get_uploaded_images():
    lst=[]
    rootdir=os.getcwd()
    for subdir, dirs, files in os.walk(rootdir + '/uploads/'):
        for file in files:
            lst.append(file)
    return lst

@app.route("/uploads/<filename>")
def get_image(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)

@app.route('/properties')
def properties():
    #items=get_uploaded_images()
    items=db.session.query(Property).all()
    return render_template("properties.html", items=items)




@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['ADMIN_USERNAME'] or request.form['password'] != app.config['ADMIN_PASSWORD']:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            
            flash('You were logged in', 'success')
            return redirect(url_for('property'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out', 'success')
    return redirect(url_for('home'))


###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
