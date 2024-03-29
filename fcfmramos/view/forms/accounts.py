import re

from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    ValidationError,
    SelectField,
)
from wtforms.validators import DataRequired, Email, Length


EMAIL = "Correo institucional"
INVALID_EMAIL = "Correo inválido"
PLACEHOLDER_EMAIL = {"placeholder": "nombre.apellido@ug.uchile.cl"}


def validate_email_domain(form, field):
    pattern = r"@[\w.]*uchile\.cl$"
    if not re.search(pattern, field.data):
        raise ValidationError(
            "El correo debe terminar en @*.uchile.cl o @uchile.cl"
        )


class LoginForm(FlaskForm):
    email = StringField(
        EMAIL,
        render_kw=PLACEHOLDER_EMAIL,
        validators=[DataRequired(), Email(INVALID_EMAIL)],
    )
    password = PasswordField(
        "Contraseña", validators=[DataRequired(), Length(min=8)]
    )
    submit = SubmitField("Ingresar")


class SignupForm(FlaskForm):
    email = StringField(
        EMAIL,
        render_kw=PLACEHOLDER_EMAIL,
        validators=[
            DataRequired(),
            Email(INVALID_EMAIL),
            validate_email_domain,
        ],
    )
    username = StringField(
        "Nombre de usuario", validators=[DataRequired(), Length(min=4, max=24)]
    )
    departamento = SelectField(
        "Departamento",
        coerce=int,
        validators=[DataRequired()],
    )
    password = PasswordField(
        "Contraseña", validators=[DataRequired(), Length(min=8)]
    )
    submit = SubmitField("Crear cuenta")


class RecoverPasswordForm(FlaskForm):
    email = StringField(
        EMAIL,
        render_kw=PLACEHOLDER_EMAIL,
        validators=[
            DataRequired(),
            Email(INVALID_EMAIL),
            validate_email_domain,
        ],
    )
    submit = SubmitField("Enviar")
