from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms import  BooleanField, StringField, IntegerField
from wtforms import DateField
from wtforms import PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    Fname= StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)] )
    Lname= StringField('Last Name', validators=[Length(min=2, max=20)] )
    email=StringField('Email',validators=[DataRequired(), Email() ])
    password= PasswordField('Password' , validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password' , validators=[DataRequired(), EqualTo('password')])
    role= SelectField("Role", choices=[('Professor'),('Student')] )
    submit= SubmitField('Register')
class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(), Email() ])
    password= PasswordField('Password' , validators=[DataRequired()])
    remember= BooleanField('Remember Me')
    submit= SubmitField('Sign In')

class CreatClassroom_JoinClassroom(FlaskForm):
    ClassName= StringField('Class Name', validators=[DataRequired(), Length(min=2, max=20)] )
    ClassDiscriptio=StringField('Class Discription', validators=[DataRequired(), Length(min=10)] )
    Type= SelectField("Class Type", choices=[('Private'),('Open')] )
    NumberOfStudents=IntegerField('Size of the Class', validators=[DataRequired()])
    password= PasswordField('Password' , validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password' , validators=[DataRequired(), EqualTo('password')])
    submit= SubmitField('Create Classroom')
    JClassName=StringField('Class Name', validators=[DataRequired(), Length(min=2, max=20)] )
    Jpassword= PasswordField('Code ("Blank if there is no code")' , validators=[])
    Jsubmit= SubmitField('Join Classroom')

class MakeAnnouncement(FlaskForm):
    AnnouncementTitle= StringField('Announcement Title', validators=[DataRequired(), Length(min=2, max=30)] )
    AnnouncementContent= StringField('Announcement Content', validators=[DataRequired(), Length(min=10, max=200)] )
    submit = SubmitField('Post')

class updateUserAccount(FlaskForm):
    Fname= StringField('Update First Name To', validators=[DataRequired(), Length(min=2, max=20)] )
    Lname= StringField('Last Name To', validators=[Length(min=2, max=20)] )
    email=StringField('Update Email To',validators=[DataRequired(), Email() ])
    NewPassword= PasswordField('Update Password To' , validators=[DataRequired()])
    confirm_New_password=PasswordField('Confirm Updated Password' , validators=[DataRequired(), EqualTo('NewPassword')])
    submit= SubmitField('Update')
