from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class UserCreateForm(FlaskForm):
    userid = StringField('유저아이디', validators=[DataRequired(), Length(min=3, max=25)])
    username = StringField('닉네임',validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', message='비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    phone = StringField('전화번호', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    address = StringField('주소', validators=[DataRequired()]) # 추가 고민 필요 주소를 얼마나 쪼갤지