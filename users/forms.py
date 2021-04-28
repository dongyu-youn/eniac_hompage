from django import forms
from . import models

class LoginForm(forms.Form):

    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))

   

    def clean(self):
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")   
        password = self.cleaned_data.get("password")
        try:        
            user = models.User.objects.get(email=email)            
            if user.check_password(password):
                return self.cleaned_data
            else:
                print(user.check_password(password))
                self.add_error("password", forms.ValidationError("Password is wrong"))           
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does not exist")

class SignUpForm(forms.Form):

    name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    aniac_code = forms.CharField(widget=forms.PasswordInput)
    grade = forms.ChoiceField(choices=models.User._meta.get_field('grade').choices)
    fav_pro_genre = forms.ChoiceField(choices=models.User._meta.get_field('fav_pro_genre').choices)
    major = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Major'}))
    entered_eniac = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'entered 2021-> 31'}))
    profile_image = forms.ImageField()
    nickname = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Enter Free'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'it\'s your ID'}))
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = models.User
        fields = ("fav_pro_genre","grade","profile_image")

    def clean_aniac_code(self):
        aniac_code = self.cleaned_data.get("aniac_code")
        if(aniac_code == "4123"):
            return aniac_code
        else:
            raise forms.ValidationError("Does not match the Aniac code")
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User already exists with that email")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self):
        fav_pro_genre = self.cleaned_data.get("fav_pro_genre")
        nickname = self.cleaned_data.get("nickname")
        major = self.cleaned_data.get("major")
        grade = self.cleaned_data.get("grade")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        name = self.cleaned_data.get("name")
        entered_eniac = self.cleaned_data.get("entered_eniac") 
        profile_image = self.cleaned_data.get("profile_image")
        user = models.User.objects.create_user(email, email, password)
        user.fav_pro_genre = fav_pro_genre
        user.nickname = nickname
        user.major = major
        user.grade = grade
        user.name = name
        user.profile_image = profile_image
        user.entered_eniac = entered_eniac

        
        user.save()

    # class Meta:
    #     model = models.User
    #     fields = ("first_name", "last_name", "email")
                    
    # password = forms.CharField(widget=forms.PasswordInput)
    # password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    # def clean_password1(self):
    #     password = self.cleaned_data.get("password")
    #     password1 = self.cleaned_data.get("password1")
    #     if password != password1:
    #         raise forms.ValidationError("Password confirmation does not match")
    #     else:
    #         return password
    
    # def save(self, *args, **kwargs):
    #     user = super().save(commit=False)
    #     email = self.cleaned_data.get("email")
    #     password = self.cleaned_data.get("password")
    #     user.username = email
    #     print(user.username)
    #     user.set_password(password)
    #     user.save()