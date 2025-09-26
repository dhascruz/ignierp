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
from django.contrib import messages

@login_required
def farmer_success(request):
    
    #user_id = request.session.get('user_id')
    user_id = request.user.id
    return render(request, 'farmer_success.html',  {'user_id': user_id})



@login_required
def products(request):
    id=1
    #profile = Farmer.objects.get(id=1)
    user_id = request.user.id
    

    #return render(request, 'profile.html', {'profile': profile})
    return render(request, 'products.html',  {'user_id': user_id})


@login_required
def farmer_asset_list(request):
    #farmers = FarmerDetail.objects.all()
    #return render(request, 'farmer_profile_list.html', {'farmers': farmers})
        assets = AgriAsset.objects.all()
        user_id = request.user.id
        return render(request, 'asset_list.html', {'assets': assets,'user_id': user_id })



@login_required
def farmer_product_list(request):
        #agri_products = AgriProduct.objects.filter(user=request.user)
    agri_products=get_all_products_with_category_images()
    #cat_image= get_category_image_url(3)
    user_id = request.user.id


    return render(request, 'agri_product_list.html', {'agri_products': agri_products,'user_id': user_id})

    #    return render(request, 'asset_list.html', {'assets': assets,'user_id': user_id })    





    #return render(request, 'agri_product_list.html', {'agri_products': agri_products,'user_id': user_id})

    #    return render(request, 'asset_list.html', {'assets': assets,'user_id': user_id })    



@login_required
def projection(request):
    id=1
    #profile = Farmer.objects.get(id=1)
    

    #return render(request, 'profile.html', {'profile': profile})
    return render(request, 'projection.html')


@login_required
def my_contacts(request):
    id=1
    #profile = Farmer.objects.get(id=1)
    

    #return render(request, 'profile.html', {'profile': profile})
    return render(request, 'my_contacts.html')



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




###school crud start


def school_list(request):
    schools = School.objects.all()

    return render(request, 'school_list.html', {'schools': schools})

def school_create(request):
    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school_list')
    else:
        form = SchoolForm()
    return render(request, 'school_form.html', {'form': form})

def school_edit(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == "POST":
        form = SchoolForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            return redirect('school_list')
    else:
        form = SchoolForm(instance=school)
    return render(request, 'school_form.html', {'form': form})

def school_delete(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == "POST":
        school.delete()
        return redirect('school_list')
    return render(request, 'school_confirm_delete.html', {'school': school})


def school_view(request, pk):
    school = get_object_or_404(School, pk=pk)
    return render(request, 'school_view.html', {'school': school})


###category admin start
@login_required
def farmer_list(request):
    
    farmer_users = CustomUser.objects.filter(role='farmer')
    return render(request, 'farmer_list.html', {'farmer_users': farmer_users})


### add credit farmer
@login_required
def edit_user_credit(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    
    if request.method == 'POST':
        form = UserCreditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('farmer_list')  # redirect to user list or detail page
    else:
        form = UserCreditForm(instance=user)
    
    return render(request, 'edit_user_credit.html', {'form': form, 'user': user})



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







# List view to show all land assets


##admin asset  startin

### agri asset start
@login_required
def asset_list(request):
    assets = AgriAsset.objects.all()
    user_id = request.user.id
    return render(request, 'asset_list.html', {'assets': assets,'user_id': user_id })

@login_required
def asset_create(request):
    user_id = request.user.id

    if request.method == 'POST':
        form = AgriAssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = AgriAssetForm()
    return render(request, 'asset_form.html', {'form': form,'user_id': user_id })

@login_required
def asset_edit(request, id):
    user_id = request.user.id
    asset = get_object_or_404(AgriAsset, id=id)
    if request.method == 'POST':
        form = AgriAssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('/farmer_asset_list')
    else:
        form = AgriAssetForm(instance=asset)
    return render(request, 'asset_form.html', {'form': form,'user_id': user_id })

@login_required
def asset_delete(request, id):
    user_id = request.user.id
    asset = get_object_or_404(AgriAsset, id=id)
    if request.method == 'POST':
        asset.delete()
        return redirect('/farmer_asset_list')
    return render(request, 'asset_confirm_delete.html', {'asset': asset,'user_id': user_id })


@login_required
def admin_add_agri_product(request):
    user_id = request.user.id
    if request.method == 'POST':
        form = AgriProductForm(request.POST, request.FILES)
        if form.is_valid():
            
            try:
                agri_product = form.save(commit=False)
                agri_product.user = request.user
                agri_product.save()
                #form.save( )
                return redirect('/farmer_product_list')
            except Exception as e:
                # Handle any errors that occur during saving
                return render(request, 'agri_product_form.html', {
                    'form': form,
                    'error_message': f'An error occurred: {str(e)}'
                })
            
    else:
        form = AgriProductForm()

    return render(request, 'agri_product_form.html', {'form': form,'user_id': user_id})


@login_required
def admin_agri_product_update(request, pk):
    user_id = request.user.id
    

    product = get_object_or_404(AgriProduct, pk=pk)
    if request.method == 'POST':
        form = AgriProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/farmer_product_list')
    else:
        form = AgriProductForm(instance=product)
    return render(request, 'agri_product_form.html', {'form': form,'user_id': user_id})
    #return render(request, 'agri_product_form.html', {'user_id': user_id})


@login_required
def admin_agri_product_delete(request, pk):
    user_id = request.user.id
    product = get_object_or_404(AgriProduct, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/farmer_product_list')
    return render(request, 'agri_product_delete.html', {'product': product,'user_id': user_id})



@login_required
def agri_product_list(request):
    #agri_products = AgriProduct.objects.filter(user=request.user)
    agri_products=get_all_products_with_category_images()
    #cat_image= get_category_image_url(3)
    user_id = request.user.id


    return render(request, 'agri_product_list.html', {'agri_products': agri_products,'user_id': user_id})



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
    


### agri asset end
def farmer_contact_list(request):
    user_id = request.user.id

    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts,'user_id': user_id})

def farmer_add_contact(request):
    user_id = request.user.id

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form,'user_id': user_id})

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
    return render(request, 'contact_form.html', {'form': form,'user_id': user_id})

def farmer_delete_contact(request, pk):
    user_id = request.user.id

    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'contact': contact,'user_id': user_id})




### credit list on the admin side-- start
# List all users
# @login_required
# def user_list(request):
#     users = CustomUser.objects.all()
#     return render(request, 'credits/user_list.html', {'users': users})

# Show and manage credits for a specific user
@login_required
def user_credits(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    credits = Credit.objects.filter(user_id=user_id)
    print(f"User ID: {user_id}") 
    
    return render(request, 'user_credits.html', {'user': user, 'credits': credits,'user_id': user_id})

# Add new credit for the user
@login_required
def add_credit(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            credit = form.save(commit=False)
            credit.user = user  # Associate credit with selected user
            credit.save()
            return redirect('user_credits', user_id=user.id)
    else:
        form = CreditForm()
    return render(request, 'credit_form.html', {'form': form, 'user': user})

# Edit an existing credit for a user
@login_required
def edit_credit(request, user_id, credit_id):
    credit = get_object_or_404(Credit, pk=credit_id, user_id=user_id)
    if request.method == 'POST':
        form = CreditForm(request.POST, instance=credit)
        if form.is_valid():
            form.save()
            return redirect('user_credits', user_id=user_id)
    else:
        form = CreditForm(instance=credit)
    return render(request, 'credit_form.html', {'form': form, 'user': credit.user})

### credit list on the admin side-- end