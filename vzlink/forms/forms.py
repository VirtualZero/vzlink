from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    IntegerField
)
from wtforms.validators import (
    DataRequired, 
    Regexp,
    ValidationError,
    Length,
    email
)
from flask import request


class URL_Form(FlaskForm):
    url = StringField(
        None,
        [
            DataRequired(),
            Regexp(
                'https{0,1}://.*\..+',
                message='Please enter a valid domain or URL.'
            )
        ]
    )


class ContactForm(FlaskForm):
    def validate_math(form, field):
        if field.data > 18 or \
           field.data < 0 or \
           (int(request.form['rand_num1']) +
                int(request.form['rand_num2'])) != field.data:

            raise ValidationError(
                'The answer to the math problem is incorrect.'
            )

    contact_first_name = StringField(
        "First Name *",
        [
            DataRequired(),
            Length(
                max=100,
                message="First name cannot exceed 100 characters."
            )
        ]
    )

    contact_last_name = StringField(
        "Last Name *",
        [
            DataRequired(),
            Length(
                max=100,
                message="Last name cannot exceed 100 characters."
            )
        ]
    )

    contact_email = StringField(
        "Email *",
        [
            DataRequired(),
            email(),
            Length(
                max=150,
                message="Email address cannot exceed 150 characters."
            )
        ]
    )

    contact_phone = StringField(
        "Phone",
        [
            Length(
                max=14,
                message="Phone number cannot exceed 16 characters."
            )
        ]
    )

    message = TextAreaField(
        "What's on your mind?",
        [
            DataRequired(),
            Length(
                max=500,
                message="Message cannot exceed 500 characters."
            )
        ]
    )

    math_result = IntegerField(
        "Please solve the math problem.",
        [
            DataRequired(
                message="This field is required and must be an integer."
            ),
            validate_math
        ]
    )


""" class LoginForm(FlaskForm):
    def valid_user(form, field):
        user = User.query.filter_by(
            email=field.data
        ).first()

        if not user:
            raise ValidationError(
                'Incorrect email address.'
            )

        if not user.email_confirmed:
            flash('Please confirm you email first.')
            raise ValidationError(
                'unconfirmed_email'
            )


    def valid_pw(form, field):
        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if not user:
            pass

        else:
            validated_pw = bcrypt.check_password_hash(
                user.pw_hash, 
                form.password.data
            )

            if not validated_pw:
                raise ValidationError(
                    'Incorrect password.'
                )


    email = StringField(
        'Email', 
        [
            email(), 
            DataRequired(
                message='This field is required.'
            ),
            Length(
                max=100
            ),
            valid_user
        ]
    )

    password = PasswordField(
        'Password', 
        [
            DataRequired(
                message='This field is required.'
            ), 
            Length(
                min=8,
                max=128
            ),
            valid_pw
        ]
    )


class CreateAccountForm(FlaskForm):
    def unique_user(form, field):
        existing_user = User.query.filter_by(
            email=field.data
        ).first()

        if existing_user:
            raise ValidationError(
                'That email address is taken.'
            )


    username = StringField(
        'Username', 
        [
            DataRequired(
                message='This field is required.'
            ),
            Length(max=20)    
        ]
    )

    email = StringField(
        'Email', 
        [
            DataRequired(
                message='This field is required.'
            ), 
            email(),
            Length(max=100),
            unique_user
        ]
    )

    password = PasswordField(
        'Password', 
        [
            DataRequired(
                message='This field is required.'
            ), 
            Length(
                min=8,
                max=128
            )
        ]
    )

    confirm_password = PasswordField(
        'Confirm Password', 
        [
            DataRequired(
                message='This field is required.'
            ), 
            Length(
                min=8,
                max=128
            ), 
            EqualTo(
                'password', 
                message='Passwords must match.'
            )
        ]
    )


class Reset_Confirm_Email_Form(FlaskForm):
    def unique_user(form, field):
        existing_user = User.query.filter_by(
            email=field.data
        ).first()

        if existing_user:
            raise ValidationError(
                'That email address is taken.'
            )

    
    def valid_pw(form, field):
        user = User.query.filter_by(
            email=form.old_email.data
        ).first()

        validated_pw = bcrypt.check_password_hash(
            user.pw_hash, 
            form.password.data
        )

        if not validated_pw:
            raise ValidationError(
                'Incorrect password.'
            )


    email = StringField(
        'New Email Address', 
        [
            email(), 
            DataRequired(
                message='This field is required.'
            ),
            unique_user,
            Length(
                max=100
            )
        ]
    )

    old_email = HiddenField(
        "old_email"
    )

    password = PasswordField(
        'Password', 
        [
            DataRequired(
                message='This field is required.'
            ), 
            Length(
                min=8,
                max=128
            ),
            valid_pw
        ]
    )


class ForgotPasswordForm(FlaskForm):
    def valid_user(form, field):
        user = User.query.filter_by(
            email=field.data
        ).first()

        if not user:
            raise ValidationError(
                'Incorrect email address.'
            )

        if not user.email_confirmed:
            flash('Please confirm you email first.')
            raise ValidationError(
                'unconfirmed_email'
            )
            
    forgot_password_email = StringField(
        "Your Email Address",
        [
            DataRequired(
                message='This field is required.'
            ),
            email(),
            Length(
                max=100,
                message="Email cannot exceed 150 characters."
            ),
            valid_user
        ]
    )


class ResetPasswordForm(FlaskForm):
    reset_password = PasswordField(
        "New Password",
        [
            DataRequired(
                message='This field is required.'
            ),
            Length(
                min=8,
                max=128
            )
        ]
    )

    confirm_reset_password = PasswordField(
        "Confirm New Password",
        [
            DataRequired(
                message='This field is required.'
            ),
            Length(
                min=8,
                max=128
            ),
            EqualTo(
                'reset_password',
                message="Passwords must match."
            )
        ]
    )

    email = HiddenField(
        "email"
    ) """
