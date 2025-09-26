from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.contrib.auth.models import User

# class CustomUserCreationForm(UserCreationForm):
#     role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'role', 'password1', 'password2')



class RegisterForm(AuthenticationForm):
    email = forms.EmailField(required=True)  # Adding email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'address', 'contact', 'established_year']


# class FarmerDetailForm(forms.ModelForm):
#     class Meta:
#         model = FarmerDetail
#         fields = ('phone','pincode','village','taluk','district','state','country')



# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name', 'image']


# class CustomLoginForm(UserCreationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(attrs={
#              "class": "w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500",
#              "style": "width: 100%;",
#             'placeholder': 'Username'
#         })
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={
#             "class": "w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500",
#             "style": "width: 100%;",
#             'placeholder': 'Password'
#         })
#     )



class CustomLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-lg form-control-solid",
            "placeholder": "Enter username",
            "required": True
    })
)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control form-control-lg form-control-solid w-100 mb-3",
            "placeholder": "Password",
            "autocomplete": "current-password"
        })
    )




# class UserCreditForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['credit']
#         labels = {'credit': 'Add Credit'}

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         if commit:
#             user.save()
#         return user
        

# class AgriProductForm(forms.ModelForm):


#     crop_name = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )


#     actual_production = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )

#     project_production = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
    
#     projection_timeline = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
    
#     cultivation_land_value = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
    
     
#     cost_per_unit = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )

#     project_cost_per_unit = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )



    
#     class Meta:
#         model = AgriProduct
#         fields = [
#             'category',
#             'crop_name',
#             'actual_production',
#             'project_production',
#             'projection_timeline',
#             'cultivation_land_value',
#             'cost_per_unit',
#             'project_cost_per_unit',
#             'image',
#         ]


# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name', 'image', 'description']


     
                  



# class AgriAssetForm(forms.ModelForm):

#     land_owner = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )

#     land_location = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )


#     google_map_location = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )

#     width = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )

#     length = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )

#     size = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
    

#     class Meta:
#         model = AgriAsset
#         fields = ['land_owner', 'land_location', 'google_map_location', 'width', 'length', 'size', 'cultivation_method','owner_type']


# class TOTPVerifyForm(forms.Form):
#     token = forms.CharField(label="Enter TOTP", max_length=6)


# class ContactForm(forms.ModelForm):


#     name = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )

#     phone = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )

#     email = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )

#     referral = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )



#     class Meta:
#         model = Contact
#         fields = ['user','name', 'phone', 'email', 'referral' ]


