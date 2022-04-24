from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,TextAreaField, FileField, validators,SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed



class MyForm(FlaskForm):
    #select=[(1,'House'),(2,'Apartment')]
    select=[('House','House'),('Apartment','Apartment')]
    propertyType=SelectField(u'Property Type', choices = select, validators = [validators.DataRequired()])
    title = StringField('Property Title', validators=[DataRequired()])
    description= TextAreaField('Description', validators=[DataRequired()])
    rooms=IntegerField('No. of Rooms ', validators=[DataRequired()])
    bathroom=IntegerField('No. of Bathrooms', [validators.NumberRange(min=0, max=10)])
    price=IntegerField('Price', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])


