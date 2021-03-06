from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired('不能为空'), Length(1,64),
                                          Email()])
    password = PasswordField(
        '密码', validators=[DataRequired('不能为空')]
    )
    remember_me = BooleanField('记住我',render_kw={'data-toggle':"switch"})
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    email = StringField('邮箱',validators=[DataRequired('不能为空'), Length(1,64), Email()])

    username = StringField('用户名', validators=[DataRequired(), Length(1,64), Regexp(
        '^[A-Za-z][A-Za-z0-9_.]*$',0,'用户名必须由字母数字组成'
    )])

    password = PasswordField('密码', validators=[DataRequired('不能为空'),
                                               EqualTo('password2',message='两次密码必须相同')])
    password2 = PasswordField('确认密码', validators=[DataRequired('不能为空'),])

    submit = SubmitField('注册')



class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('旧密码', validators=[DataRequired()])
    password = PasswordField('新密码', validators=[DataRequired('不能为空'),
                                               EqualTo('password2',message='两次密码必须相同')])
    password2 = PasswordField('确认密码', validators=[DataRequired('不能为空'),])

    submit = SubmitField('更新密码')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('邮箱',validators=[DataRequired('不能为空'), Length(1,64), Email()])
    submit = SubmitField('找回密码')
    

class PasswordResetForm(FlaskForm):
    email = StringField('邮箱',validators=[DataRequired('不能为空'), Length(1,64), Email()])
    password = PasswordField('新密码', validators=[DataRequired('不能为空'),
                                                EqualTo('password2', message='两次密码必须相同')])
    password2 = PasswordField('确认密码', validators=[DataRequired('不能为空'), ])
    submit = SubmitField('重置密码')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('Email不存在')

class ChangeEmailForm(FlaskForm):
    email = StringField('New Email', validators=[DataRequired('不能为空'), Length(1,64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('确定')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')