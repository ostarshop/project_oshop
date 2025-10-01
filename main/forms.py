from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields.simple import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class UserCreateForm(FlaskForm):
    userid = StringField('유저아이디', validators=[DataRequired('아이디를 입력해주세요'), Length(min=3, max=25)])
    username = StringField('닉네임',validators=[DataRequired('닉네임을 입력해주세요'), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired('비밀번호를 입력해주세요'), EqualTo('password2', message='비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired('비밀번호를 다시 입렵해수세요')])
    phone = StringField('전화번호', validators=[DataRequired('000-0000-0000')])
    email = EmailField('이메일', validators=[DataRequired('이메일을 입력해주세요'), Email()])
    address = StringField('주소', validators=[DataRequired('주소를 입력해주세요')]) # 추가 고민 필요 주소를 얼마나 쪼갤지
    image = FileField('프로필사진', validators=[FileAllowed(['jpg', 'jpeg', 'png','gif'])])


class UserLoginForm(FlaskForm):
    userid = StringField('사용자 이름', validators=[DataRequired('아이디를 입력해주세요'), Length(min=3, max=25)])
    password = PasswordField('', validators=[DataRequired('비밀번호를 입력해주세요')])