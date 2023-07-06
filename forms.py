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


class BuyForm(FlaskForm):
    firstname = StringField(render_kw={"id": "alt_address_firstname", "class": "form-control"})
    lastname = StringField(render_kw={"id": "alt_address_lastname", "class": "form-control"})
    email = StringField(render_kw={"id": "alt_address_email", "class": "form-control"})
    phone = StringField(render_kw={"id": "alt_address_phone", "class": "form-control"})
    street = StringField(render_kw={"id": "alt_address_street", "class": "form-control"})
    house_number = IntegerField(render_kw={"id": "alt_address_house_number", "class": "form-control"})
    postal_code = IntegerField(render_kw={"id": "alt_address_postal_code", "class": "form-control"})
    city = StringField(render_kw={"id": "alt_address_city", "class": "form-control"})
    country = StringField(render_kw={"id": "alt_address_country", "class": "form-control"})
    state = StringField(render_kw={"id": "alt_address_state", "class": "form-control"})
    use_alt_delivery_address = StringField(validators=[InputRequired()], render_kw={"id": "use_alt_delivery_address", "style": "display: none", "value": "false"})
    payment_method = StringField(validators=[InputRequired()], render_kw={"id": "payment_method_field", "style": "display: none"})
    products_as_dict = StringField(validators=[InputRequired()], render_kw={"id": "products_field", "style": "display: none"})
    submit = SubmitField("Bestellung bestätigen und abschließen",
                         render_kw={"style": "display: none; border-color:#d18c09; background-color: #d18c09; color: white",
                                    "class": "btn btn-outline-primary btn-rounded btn-block", "id": "button_confirm_order"})
