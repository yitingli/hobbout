from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import TingUser
from mediabox.models import MediaImage


class TingUserLoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'id': 'password'}))


class TingUserCreateForm(forms.ModelForm):

    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'duplicate_email': _("A user with that email already exists."),
        'short_password': _("The password must be at least 3 characters.")
    }

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'id': 'email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'id': 'password'}))

    class Meta:
        model = TingUser
        fields = ('email', 'username')

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            TingUser.objects.get(email=email)
        except TingUser.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['duplicate_email'])

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            TingUser.objects.get(username=username)
        except TingUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 3:
            raise forms.ValidationError(
                self.error_messages['short_password'])
        return password

    def save(self, commit=True):
        user = super(TingUserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.set_registration_complete()
        if commit:
            user.save()
        return user


class TingUserUpdateForm(forms.ModelForm):

    image = forms.ImageField(required=False)
    brief_description =  forms.CharField(widget=forms.Textarea)

    class Meta:
        model = TingUser
        fields = ('image', 'email', 'username', 'brief_description', 'birth_date', 'first_name', 'last_name', 'description')

    def __init__(self, *args, **kwargs):
        self.user = kwargs['initial']['user']
        super(TingUserUpdateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super(TingUserUpdateForm, self).save(commit=False)
        if commit:
            image = self.cleaned_data['image']
            if image:
                avatar = MediaImage(image=image, owner=user)
                avatar.save()
                user.avatar = avatar
            user.save()
        return user


class TingUserPasswordChangeForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
        'password_incorrect': _("Your old password was entered incorrectly. "
                                "Please enter it again."),
    }

    old_password = forms.CharField(label=_("Old password"),
                                   widget=forms.PasswordInput)
    new_password1 = forms.CharField(label=_("New password"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=_("New password confirmation"),
                                    widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user = kwargs['initial']['user']
        super(TingUserPasswordChangeForm, self).__init__(*args, **kwargs)

    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'])
        return old_password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user
