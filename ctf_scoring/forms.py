from django import forms 

class RegisterForm(forms.Form):
    team_name = forms.CharField(
        label="Team Name",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "w-full border px-2 py-1 rounded border-gray-300 focus:outline-indigo-500"}),
    )
    username = forms.CharField(
        label="Username",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "w-full border px-2 py-1 rounded border-gray-300 focus:outline-indigo-500"}),
    )

    password = forms.CharField(
        label="Password",
        max_length=100,
        widget=forms.PasswordInput(attrs={"class": "w-full border px-2 py-1 rounded border-gray-300 focus:outline-indigo-500"}),
    )

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "w-full border px-2 py-1 rounded border-gray-300 focus:outline-indigo-500"}),
    )

    password = forms.CharField(
        label="Password",
        max_length=100,
        widget=forms.PasswordInput(attrs={"class": "w-full border px-2 py-1 rounded border-gray-300 focus:outline-indigo-500"}),
    )

class SubmitFlagForm(forms.Form):

    flag = forms.CharField(
        label="Flag",
        max_length=256,
        widget=forms.TextInput(attrs={"class": "w-full border mr-2 text-sm px-2 py-1 rounded border-gray-300 focus:outline-indigo-500", "placeholder": "Enter flag here"}),
    )

