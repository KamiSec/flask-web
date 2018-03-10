from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Regexp
from ..models import Role, User
from wtforms.validators import ValidationError
from flask_pagedown.fields import PageDownField


class EditProfileForm(FlaskForm):
    name = StringField('真实姓名', validators=[Length(0,64)])
    location = StringField('所在地', validators=[Length(0,64)])
    about_me = TextAreaField('说说')
    submit = SubmitField('确定')


class EditPrifileAdminForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Length(1,64), Email()])
    username = StringField('用户名', validators=[
        DataRequired(), Length(1,64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          '用户名必须由字母、数字组成')])
    confirmed = BooleanField('激活',render_kw={'data-toggle':"switch"})
    role = SelectField('角色',coerce=int,render_kw={'data-toggle':"select"})
    name = StringField('真实姓名', validators=[Length(0,64)])
    location = StringField('所在地', validators=[Length(0,64)])
    about_me = TextAreaField('说说')
    submit = SubmitField('确认')

    def __init__(self, user, *args, **kwargs):
        super(EditPrifileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [
            (role.id, role.name) for role in Role.query.order_by(Role.name).all()
        ]
        self.user = user

    def vaildate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')


class PostForm(FlaskForm):
    body = PageDownField('你的心情怎么样？',validators=[DataRequired()])
    submit = SubmitField('发表')



class CommentForm(FlaskForm):
    body = PageDownField('',validators=[DataRequired()])
    submit = SubmitField('提交')