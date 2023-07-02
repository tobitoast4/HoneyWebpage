from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, ValidationError


class RegisterForm(FlaskForm):
    firstname = StringField(validators=[InputRequired(), Length(min=1, max=99)], render_kw={"class": "form-control"})
    lastname = StringField(validators=[InputRequired(), Length(min=1, max=99)], render_kw={"class": "form-control"})
    email = StringField(validators=[InputRequired()], render_kw={"placeholder": "max.musterfrau@gmail.com", "class": "form-control"})
    phone = StringField(render_kw={"class": "form-control"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=99)], render_kw={"class": "form-control"})
    password_repeat = PasswordField(validators=[InputRequired(), Length(min=4, max=99)], render_kw={"class": "form-control"})
    street = StringField(validators=[InputRequired(), Length(min=1, max=99)], render_kw={"class": "form-control"})
    house_number = IntegerField(validators=[InputRequired(), NumberRange(min=1)], render_kw={"class": "form-control"})
    postal_code = IntegerField(validators=[InputRequired(), NumberRange(min=1)], render_kw={"class": "form-control"})
    city = StringField(validators=[InputRequired(), Length(min=1, max=99)], render_kw={"class": "form-control"})
    country = StringField(validators=[InputRequired(), Length(min=1, max=99)], render_kw={"class": "form-control"})
    state = StringField(render_kw={"class": "form-control"})
    submit = SubmitField("Register", render_kw={"style": "display: block; border-color:#d18c09; background-color: #d18c09; color: white",
                                                "class": "btn btn-outline-primary btn-rounded",
                                                "onclick": "return Validate()"})


class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired()], render_kw={"class": "form-control"})
    password = PasswordField(validators=[InputRequired(), Length(min=1, max=99)], render_kw={"class": "form-control"})
    submit = SubmitField("Login", render_kw={"style": "display: block; border-color:#d18c09; background-color: #d18c09; color: white",
                                             "class": "btn btn-outline-primary btn-rounded"})


class BuyNowForm(FlaskForm):
    agb = BooleanField(validators=[InputRequired()], render_kw={"class": "form-check-input", "type": "checkbox"})
    privacy = BooleanField(validators=[InputRequired()], render_kw={"class": "form-check-input", "type": "checkbox"})
    submit = SubmitField("Zur Kasse", render_kw={"style": "display: block; background-color: #d18c09",
                                                 "class": "btn btn-primary btn-rounded"})
