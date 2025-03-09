from django import forms 

class RegisterForm(forms.Form):
    team_name = forms.CharField(
        label="Team Name",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "w-full border px-2 py-1 rounded border-green-800 bg-slate-900 focus:outline-none focus:outline-green-700"}),
    )
    username = forms.CharField(
        label="Username",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "w-full border px-2 py-1 rounded border-green-800 bg-slate-900 focus:outline-none focus:outline-green-700"}),
    )

    password = forms.CharField(
        label="Password",
        max_length=100,
        widget=forms.PasswordInput(attrs={"class": "w-full border px-2 py-1 rounded border-green-800 bg-slate-900 focus:outline-none focus:outline-green-700"}),
    )

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "w-full border px-2 py-1 rounded border-green-800 bg-slate-900 focus:outline-none focus:outline-green-700"}),
    )

    password = forms.CharField(
        label="Password",
        max_length=100,
        widget=forms.PasswordInput(attrs={"class": "w-full border px-2 py-1 rounded border-green-800 bg-slate-900 focus:outline-none focus:outline-green-700"}),
    )

class SubmitFlagForm(forms.Form):

    flag = forms.CharField(
        label="Flag",
        max_length=256,
        widget=forms.TextInput(attrs={"class": "w-full border mr-2 text-sm px-2 py-1 rounded bg-slate-800 border-slate-700", "placeholder": "Enter flag here"}),
    )

