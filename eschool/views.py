from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import *
from .models import *
from .utils import *
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
import logging
from users.services import get_cohort_counts, get_course_categories, get_course_teachers_students, get_courses_by_category, get_enrolled_users
from django.conf import settings
from django.shortcuts import redirect, resolve_url
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

#from django.views.generic import FormView, TemplateView


#from django_otp.mixins import OTPRequiredMixin
#from .forms import TOTPVerifyForm
import io

import qrcode
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.conf import settings
from io import BytesIO
from base64 import b64encode
from .utils import generate_totp_qr_code
from django.contrib import messages



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

logger = logging.getLogger(__name__)

def redirect_to_login(request):
    return redirect('login')


### code start eschool


# Registration view
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Home view (restricted to logged-in users)

# @login_required
# def home(request):
#     # accounting_links = AccountingLinks.objects.all()
#     # accounting_links_cnt = AccountingLinks.objects.all().count()

#     context = {
#         # 'accounting_links': accounting_links,
#         # 'accounting_links_cnt': accounting_links_cnt,
#         'user': request.user,
#         # other context variables can be added here if needed
#     }

#     return render(request, 'home.html', context)

def home(request):
    category_list = get_course_categories()  # Your function that returns a list of categories
    #print(category_list)

    # Pagination
    page = request.GET.get('page', 1)  # Current page number from query parameter
    paginator = Paginator(category_list, 10)  # Show 10 categories per page

    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)

    return render(request, "home.html", {"categories": categories}) 

@login_required
def quick_links(request):
    accounting_links = AccountingLinks.objects.all()
    accounting_links_cnt = AccountingLinks.objects.all().count()
    
    context = {
        'accounting_links': accounting_links,
        'accounting_links_cnt': accounting_links_cnt,
        
        # other context variables can be added here if needed
    }
    

    return render(request, 'quick_links.html', context)




# Logout view
def logout_view(request):
    logout(request)
    return redirect('/login')


### code end eschool






def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            if user.role == 'farmer':
                return redirect('register_farmer_detail', user_id=user.id)
            else:
                login(request, user)
                return redirect('dashboard')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': user_form})

def register_farmer_detail(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
        form = FarmerDetailForm(request.POST)
        if form.is_valid():
            farmer_detail = form.save(commit=False)
            farmer_detail.user = user
            farmer_detail.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = FarmerDetailForm()
    return render(request, 'register_farmer_detail.html', {'form': form})

def admin_check(user):
    return user.role == 'admin'

def farmer_check(user):
    return user.role == 'farmer'

def outlet_check(user):
    return user.role == 'outlet'



@login_required
def dashboard(request):
    if request.user.role == 'admin':
        return redirect('/admin-dashboard')
    elif request.user.role == 'farmer':
        return redirect('/farmer-dashboard')
    elif request.user.role == 'outlet':
        return redirect('/outlet-dashboard')
    else:
        return redirect('login')

@login_required
@user_passes_test(admin_check)
def admin_dashboard(request):
    customusers = CustomUser.objects.all();
    return render(request, 'index.html', {'customusers': customusers})

@login_required
@user_passes_test(admin_check)
def adminhome(request):
    return render(request, 'index.html')


@login_required
@user_passes_test(outlet_check)
def outlet_dashboard(request):
    #outlet_detail = FarmerDetail.objects.get(user=request.user)
    logger.info("dhas")
    user_id = request.user.id
    request.session['user_id'] = user_id
    logger.info(user_id)
    agri_products=get_all_products_with_category_images()

    return render(request, 'outlet/index.html',  {'user_id': user_id, 'agri_products':agri_products})

@login_required
@user_passes_test(farmer_check)
def farmer_dashboard(request):
    farmer_detail = FarmerDetail.objects.get(user=request.user)
    logger.info("dhas")
    user_id = request.user.id
    request.session['user_id'] = user_id
    logger.info(user_id)
    agri_products=get_all_products_with_category_images()
    return render(request, 'farmer/index.html',  {'user_id': user_id, 'agri_products':agri_products})




@login_required
@user_passes_test(farmer_check)
def personal_information(request, user_id):
    #user = get_object_or_404(CustomUser, id=user_id)
    
    farmer = get_object_or_404(FarmerDetail, user_id=user_id)
    

    if request.method == 'POST':
        'phone','pincode','village','taluk','district','state','country'
        user_id=user_id
        phone  = request.POST.get('phone')
        pincode  = request.POST.get('pincode')
        village  = request.POST.get('village')
        taluk  = request.POST.get('taluk')
        district  = request.POST.get('district')
        state  = request.POST.get('state')
        country  = request.POST.get('country')
        
        farmer = FarmerDetail.objects.get(user_id=user_id)
        farmer_exists = FarmerDetail.objects.filter(user_id=user_id).exists()
        
        logger.info(farmer)

        if phone and pincode :
            if(farmer_exists):

                
            # Step 1: Fetch the FarmerDetail record where id = 1
                    farmer = FarmerDetail.objects.get(user_id=user_id)
        
                    # Step 2: Update the fields you want to change
                    farmer.phone = phone  
                    farmer.pincode = pincode
                    farmer.village = village
                    farmer.taluk = taluk
                    farmer.district = district
                    farmer.state = state
                    farmer.country = country
                    

                        # Step 3: Save the changes to the database
                    farmer.save()

                
                    return redirect('farmer_success')  # Redirect to a success page or other desired page
            else:
                FarmerDetail.objects.create(user_id=user_id,phone = phone,pincode = pincode,village = village,taluk = taluk,district = district,state = state,country = country)    
                return redirect('farmer_success')  # Redirect to a success page or other desired page
        else:
            return HttpResponse("Missing fields", status=400)

    return render(request, 'farmer/personal_information.html', { 'user_id': user_id, 'farmer': farmer})


def farmer_success(request):
    
    #user_id = request.session.get('user_id')
    user_id = request.user.id
    return render(request, 'farmer/farmer_success.html',  {'user_id': user_id})


##function start on otp

@login_required
def enable_two_factor(request):
    curuser=request.user
    qr_code_base64 = generate_totp_qr_code(request.user)
    if request.method == "POST":
        # Generate QR code for the user
        qr_code_base64 = generate_totp_qr_code(request.user)
        return render(request, 'farmer/enable_2fa.html', {
            'qr_code': qr_code_base64
        })
    #return redirect('dashboard')
    return render(request, 'farmer/enable_2fa.html', {
            'qr_code': qr_code_base64,
            'user': curuser
        })


@login_required
def disable_two_factor(request):
    # Disable two-factor authentication
    TOTPDevice.objects.filter(user=request.user).delete()
    request.user.two_factor_enabled = False
    request.user.save()
    return redirect('dashboard')


def verify_totp(request):
    if request.method == "POST":
        form = TOTPVerifyForm(request.POST)
        if form.is_valid():
            device = TOTPDevice.objects.get(user=request.user, confirmed=False)
            
            # Verify the TOTP token entered by the user
            if device.verify_token(form.cleaned_data['token']):
                # If the token is valid, confirm the device and enable 2FA
                device.confirmed = True
                device.save()
                
                # Mark that the user has enabled 2FA
                request.user.two_factor_enabled = True
                request.user.save()
                messages.success(request, "You are Succesfully verified.")
                return redirect('farmer_dashboard')  # Redirect to the dashboard after successful validation
            else:
                form.add_error('token', 'Invalid TOTP token. Please try again.')
    else:
        form = TOTPVerifyForm()

    return render(request, 'farmer/verify_totp.html', {'form': form})




##function end on otp


@login_required
def credit(request):
    
    #profile = Farmer.objects.get(id=1)
    user_id = request.user.id
    

    #return render(request, 'profile.html', {'profile': profile})
    return render(request, 'farmer/credit.html',  {'user_id': user_id})


def coin_with_credit(request):
    # Load the coin image (ensure the image path is correct)
    image_path = 'static/assets/images/coin.png'  # Adjust path as necessary
    image = Image.open(image_path)
    font = ImageFont.truetype("/static/assets/fonts/la-solid-900.ttf", size=24)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Define the text and font
    text = "50"
    font = ImageFont.load_default()  # Load a default font or use a custom font

    # Get image dimensions
    image_width, image_height = image.size

    # Calculate the position to center the text at the top
    #text_width, text_height = draw.textsize(text, font=font)
    position = ((image_width - 10) // 2, 10)  # 10 pixels from the top

    # Add the text to the image
    draw.text(position, text, font=font, fill="white")  # Change the fill color as needed

    # Save the image to a bytes buffer
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)

    # Return the image as an HTTP response
    return HttpResponse(buffer, content_type='image/png')



@login_required
def products(request):
    id=1
    #profile = Farmer.objects.get(id=1)
    user_id = request.user.id
    

    #return render(request, 'profile.html', {'profile': profile})
    return render(request, 'farmer/products.html',  {'user_id': user_id})







    #    return render(request, 'asset_list.html', {'assets': assets,'user_id': user_id })    





    #return render(request, 'agri_product_list.html', {'agri_products': agri_products,'user_id': user_id})

    #    return render(request, 'asset_list.html', {'assets': assets,'user_id': user_id })    



@login_required
def projection(request):
    id=1
    #profile = Farmer.objects.get(id=1)
    

    #return render(request, 'profile.html', {'profile': profile})
    return render(request, 'farmer/projection.html')


@login_required
def my_contacts(request):
    id=1
    #profile = Farmer.objects.get(id=1)
    

    #return render(request, 'profile.html', {'profile': profile})
    return render(request, 'farmer/my_contacts.html')





# def product_list(request):
#     products = AgriculturalProduct.objects.filter(user=request.user)
#     return render(request, 'farmer/products.html', {'products': products})

# def product_create(request):
#     if request.method == 'POST':
#         form = AgriculturalProductForm(request.POST)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.user = request.user
#             product.save()
#             return redirect('product_list')
#     else:
#         form = AgriculturalProductForm()
#     return render(request, 'farmer/products_form.html', {'form': form})

# def product_update(request, pk):
#     product = get_object_or_404(AgriculturalProduct, pk=pk, user=request.user)
#     if request.method == 'POST':
#         form = AgriculturalProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')
#     else:
#         form = AgriculturalProductForm(instance=product)
#     return render(request, 'farmer/products_form.html', {'form': form})

# def product_delete(request, pk):
#     product = get_object_or_404(AgriculturalProduct, pk=pk, user=request.user)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('product_list')
#     return render(request, 'farmer/products_confirm_delete.html', {'product': product})


@login_required
@user_passes_test(farmer_check)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_agri_product')
    else:
        form = CategoryForm()

    return render(request, 'category_form.html', {'form': form})

@login_required
@user_passes_test(farmer_check)
def add_agri_product(request):
    user_id = request.user.id
    if request.method == 'POST':
        form = AgriProductForm(request.POST, request.FILES)
        if form.is_valid():
            
            try:
                agri_product = form.save(commit=False)
                agri_product.user = request.user
                agri_product.save()
                #form.save( )
                return redirect('agri_product_list')
            except Exception as e:
                # Handle any errors that occur during saving
                return render(request, 'farmer/agri_product_form.html', {
                    'form': form,
                    'error_message': f'An error occurred: {str(e)}'
                })
            
    else:
        form = AgriProductForm()

    return render(request, 'farmer/agri_product_form.html', {'form': form,'user_id': user_id})



def agri_product_update(request, pk):
    user_id = request.user.id
    product = get_object_or_404(AgriProduct, pk=pk, user=request.user)
    if request.method == 'POST':
        form = AgriProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('agri_product_list')
    else:
        form = AgriProductForm(instance=product)
    return render(request, 'farmer/agri_product_form.html', {'form': form,'user_id': user_id})


def agri_product_delete(request, pk):
    user_id = request.user.id
    product = get_object_or_404(AgriProduct, pk=pk, user=request.user)
    if request.method == 'POST':
        product.delete()
        return redirect('agri_product_list')
    return render(request, 'farmer/agri_product_delete.html', {'product': product,'user_id': user_id})




@login_required
@user_passes_test(farmer_check)
def agri_product_list(request):
    #agri_products = AgriProduct.objects.filter(user=request.user)
    agri_products=get_all_products_with_category_images()
    #cat_image= get_category_image_url(3)
    user_id = request.user.id


    return render(request, 'farmer/agri_product_list.html', {'agri_products': agri_products,'user_id': user_id})



def get_all_products_with_category_images():
    # Query all products and annotate with the category image URL
    products = AgriProduct.objects.all().select_related('category').annotate(
        category_image_url=F('image')
    )

    # Create a list to store products with their corresponding category image URLs
    product_list = [
        {
            'id': product.id,
            'crop_name': product.crop_name,
            'actual_production': product.actual_production,
            'project_production': product.project_production,
            'cost_per_unit': product.cost_per_unit,
            'project_cost_per_unit': product.project_cost_per_unit,
            'category_image_url': get_category_image_url(product.category_id)
        }
        for product in products
    ]

    return product_list






def get_category_image_url(category_id):
    # Retrieve the category object based on the given ID
    category = get_object_or_404(Category, id=category_id)
    
    # Check if the category has an image
    if category.image:
        return category.image.url  # Return the URL of the image
    else:
        return None  # or a default image URL if preferred



###category admin start
@login_required

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

@login_required

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

@login_required

def category_edit(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

@login_required

def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})


###category admin end





###category admin start
@login_required

def farmer_list(request):
    
    farmer_users = CustomUser.objects.filter(role='farmer')
    return render(request, 'farmer_list.html', {'farmer_users': farmer_users})

@login_required
@user_passes_test(farmer_check)
def Farmer_create(request):
    if request.method == 'POST':
        form = FarmerDetail(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Farmer_list')
    else:
        form = FarmerDetailForm()
    return render(request, 'farmer/Farmer_form.html', {'form': form})

# def Farmer_edit(request, id):
#     Farmer = get_object_or_404(Farmer, id=id)
#     if request.method == 'POST':
#         form = FarmerForm(request.POST, request.FILES, instance=Farmer)
#         if form.is_valid():
#             form.save()
#             return redirect('Farmer_list')
#     else:
#         form = FarmerForm(instance=Farmer)
#     return render(request, 'products/Farmer_form.html', {'form': form})

# def Farmer_delete(request, id):
#     Farmer = get_object_or_404(Farmer, id=id)
#     if request.method == 'POST':
#         Farmer.delete()
#         return redirect('Farmer_list')
#     return render(request, 'products/Farmer_confirm_delete.html', {'Farmer': Farmer})


###category admin end





###farmer profile list start

def farmer_profile_list(request):
    #farmers = FarmerDetail.objects.all()
    #return render(request, 'farmer_profile_list.html', {'farmers': farmers})
    return render(request, 'farmer_profile_list.html')

# def Farmer_create(request):
#     if request.method == 'POST':
#         form = FarmerForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('Farmer_list')
#     else:
#         form = FarmerForm()
#     return render(request, 'products/Farmer_form.html', {'form': form})

# def Farmer_edit(request, id):
#     Farmer = get_object_or_404(Farmer, id=id)
#     if request.method == 'POST':
#         form = FarmerForm(request.POST, request.FILES, instance=Farmer)
#         if form.is_valid():
#             form.save()
#             return redirect('Farmer_list')
#     else:
#         form = FarmerForm(instance=Farmer)
#     return render(request, 'products/Farmer_form.html', {'form': form})

# def Farmer_delete(request, id):
#     Farmer = get_object_or_404(Farmer, id=id)
#     if request.method == 'POST':
#         Farmer.delete()
#         return redirect('Farmer_list')
#     return render(request, 'products/Farmer_confirm_delete.html', {'Farmer': Farmer})


###farmer profile list end


###farmer contact list start


# def Farmer_create(request):
#     if request.method == 'POST':
#         form = FarmerForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('Farmer_list')
#     else:
#         form = FarmerForm()
#     return render(request, 'products/Farmer_form.html', {'form': form})

# def Farmer_edit(request, id):
#     Farmer = get_object_or_404(Farmer, id=id)
#     if request.method == 'POST':
#         form = FarmerForm(request.POST, request.FILES, instance=Farmer)
#         if form.is_valid():
#             form.save()
#             return redirect('Farmer_list')
#     else:
#         form = FarmerForm(instance=Farmer)
#     return render(request, 'products/Farmer_form.html', {'form': form})

# def Farmer_delete(request, id):
#     Farmer = get_object_or_404(Farmer, id=id)
#     if request.method == 'POST':
#         Farmer.delete()
#         return redirect('Farmer_list')
#     return render(request, 'products/Farmer_confirm_delete.html', {'Farmer': Farmer})


###farmer contat list end

login_required
def user_list(request):
    user_id = request.user.id

    customusers = CustomUser.objects.all();
    return render(request, 'user_list.html', {'customusers': customusers,'user_id': user_id})

    #return render(request, 'user_form.html', {'form': form,'user_id': user_id })


login_required
def user_create(request):
    user_id = request.user.id

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_form.html', {'form': form,'user_id': user_id })

@login_required

def user_edit(request, id):
    user_id = request.user.id
    user = get_object_or_404(CustomUser, id=id)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm(instance=user)
    return render(request, 'user_form.html', {'form': form,'user_id': user_id })

@login_required

def user_delete(request, id):
    user_id = request.user.id
    user = get_object_or_404(CustomUser, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user,'user_id': user_id })






### agri asset start
@login_required
@user_passes_test(farmer_check)
def asset_list(request):
    assets = AgriAsset.objects.all()
    user_id = request.user.id
    return render(request, 'farmer/asset_list.html', {'assets': assets,'user_id': user_id })

@login_required
@user_passes_test(farmer_check)
def asset_create(request):
    user_id = request.user.id

    if request.method == 'POST':
        form = AgriAssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = AgriAssetForm()
    return render(request, 'farmer/asset_form.html', {'form': form,'user_id': user_id })

@login_required
@user_passes_test(farmer_check)
def asset_edit(request, id):
    user_id = request.user.id
    asset = get_object_or_404(AgriAsset, id=id)
    if request.method == 'POST':
        form = AgriAssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = AgriAssetForm(instance=asset)
    return render(request, 'farmer/asset_form.html', {'form': form,'user_id': user_id })

@login_required
@user_passes_test(farmer_check)
def asset_delete(request, id):
    user_id = request.user.id
    asset = get_object_or_404(AgriAsset, id=id)
    if request.method == 'POST':
        asset.delete()
        return redirect('asset_list')
    return render(request, 'farmer/asset_confirm_delete.html', {'asset': asset,'user_id': user_id })



# List view to show all land assets



### agri asset end
def farmer_contact_list(request):
    user_id = request.user.id

    contacts = Contact.objects.all()
    return render(request, 'farmer/contact_list.html', {'contacts': contacts,'user_id': user_id})

def farmer_add_contact(request):
    user_id = request.user.id

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'farmer/contact_form.html', {'form': form,'user_id': user_id})

def farmer_edit_contact(request, pk):
    user_id = request.user.id

    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'farmer/contact_form.html', {'form': form,'user_id': user_id})

def farmer_delete_contact(request, pk):
    user_id = request.user.id

    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'farmer/contact_confirm_delete.html', {'contact': contact,'user_id': user_id})






# @method_decorator(never_cache, name='dispatch')
# class ExampleSecretView(OTPRequiredMixin, TemplateView):
#     template_name = 'secret.html'


