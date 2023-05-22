from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Optional, length
from .models import Category


def get_categories():
    categories = Category.query.all()
    return [(category.id, category.title) for category in categories]


class FeedbackForm(FlaskForm):
    title = StringField(
        'Название',
        validators=[DataRequired(message="Поле не должно быть пустым"),
                    length(max=255, message='Введите заголовок длиной до 255 символов')]
    )

    text = TextAreaField(
        'Текст',
        validators=[DataRequired(message="Поле не должно быть пустым")])
    category = SelectField("Категория", choices=get_categories(), validators=[Optional()])
    submit = SubmitField('Добавить')