
from wtforms import Form, StringField,FileField, TextAreaField, SubmitField, PasswordField, validators, FileField, IntegerField, DateField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Regexp
import logging

logger = logging.getLogger('gunicorn.info')
logger.setLevel('INFO')

class ResetPasswordForm(Form):
    logger.info('ResetPasswordForm class is processing')
    password = PasswordField('Password', [DataRequired(),validators.Length(min=6,max=25),
        EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Confirm Password',[DataRequired()])
    submit = SubmitField('Reset Password')

class RequestResetForm(Form):
    logger.info('RequestResetForm class is processing')
    email = StringField('Email', [DataRequired(), Email(), validators.Length(min=6, max=50)])
    submit = SubmitField('Request Password Reset')


# Register Form Class
class RegisterForm(Form):
    logger.info('RegisterForm class is processing')
    email = StringField('Email', [DataRequired(), Email(), validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),validators.Length(min=6,max=25),
        EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Confirm Password',[DataRequired()])
    paramit_key= PasswordField('Company Key',[DataRequired()])

# Register Form Class
class LoginForm(Form):
    logger.info('LoginForm class is processing')
    email = StringField('Email Address', [DataRequired(),Email()])
    password = PasswordField('Password', [DataRequired()])