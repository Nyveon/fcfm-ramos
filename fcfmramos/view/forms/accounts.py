from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, Length


def validate_email_domain(form, field):
    if not field.data.endswith("@ug.uchile.cl"):
        raise ValidationError("El correo debe terminar en @ug.uchile.cl")


class LoginForm(FlaskForm):
    email = StringField(
        "Correo (@ug.uchile.cl)", validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        "Contraseña", validators=[DataRequired(), Length(min=8)]
    )
    submit = SubmitField("Ingresar")


class SignupForm(FlaskForm):
    email = StringField(
        "Correo (@ug.uchile.cl)",
        validators=[DataRequired(), Email(), validate_email_domain],
    )
    password = PasswordField(
        "Contraseña", validators=[DataRequired(), Length(min=8)]
    )
    submit = SubmitField("Crear cuenta")


class RecoverPasswordForm(FlaskForm):
    email = StringField(
        "Correo (@ug.uchile.cl)",
        validators=[DataRequired(), Email(), validate_email_domain],
    )
    submit = SubmitField("Recuperar contraseña")