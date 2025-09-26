from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import *
from .models import *
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import logging
from django.shortcuts import redirect
logger = logging.getLogger(__name__)

def redirect_to_login(request):
    return redirect('login')

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

@login_required
def dashboard(request):
    if request.user.role == 'admin':
        return redirect('/admin-dashboard')
    elif request.user.role == 'farmer':
        return redirect('/farmer-dashboard')
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

@login_required
def farmer_success(request):
    
    #user_id = request.session.get('user_id')
    user_id = request.user.id
    return render(request, 'farmer/farmer_success.html',  {'user_id': user_id})

@login_required
def products(request):
    id=1
    #profile = Farmer.objects.get(id=1)
    user_id = request.user.id
    

    #return render(request, 'profile.html', {'profile': profile})
    return render(request, 'farmer/products.html',  {'user_id': user_id})


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

def farmer_contact_list(request):
    #farmers = FarmerDetail.objects.all()
    #return render(request, 'farmer_profile_list.html', {'farmers': farmers})
    return render(request, 'farmer/farmer_contact22_list.html')

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