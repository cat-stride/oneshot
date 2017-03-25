from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .. import db
from ..models import User
from ..mail import send_mail
from .forms import LoginForm, RegistrationForm


@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.endpoint == 'index':
        return render_template('auth/unconfirmed.html')

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(mail=form.mail.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/signin.html', form=form)

@auth.route('/signout')
@login_required
def signout():
    logout_user()
    flash("You've been logged out.")
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()

        user.mail = form.mail.data,
        user.username = form.username.data,
        user.password = form.password.data
        user.wechat_id = form.wechat_id.data
        user.register_source = 'web'
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_mail(user.mail, 'Confirm Your Account',
                   'auth/mail/confirm', user=user, token=token)
        flash('A confirmation mail has been sent.')
        return redirect(url_for('auth.signin'))
    return render_template('auth/register.html', form=form)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('Confirmation accomplished.')
    else:
        flash('Oops... Seems like the confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))

@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_mail(current_user.mail, 'Confirm Your Account',
               'auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation mail has been sent.')
    return redirect(url_for('main.index'))
