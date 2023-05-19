from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse

# Create your views here.
def admin_index(request):
    all_products = product_sub_cat.objects.all()
    return render(request, 'admin_index.html', {'all_p':all_products})

def add_product(request):
    try:
        if request.method == "GET":
            return render(request, 'add_product.html')
        else:
            product_mst.objects.create(
                product_name = request.POST['name']
            )
            p_name_obj = product_mst.objects.get(product_name = request.POST['name'])
            product_sub_cat.objects.create(
                product_model = request.POST['model'],
                product_ram = request.POST['ram'],
                product_image = request.FILES['p_image'],
                product_price = request.POST['price'],
                p_name = p_name_obj
            )
            return redirect('admin_index')
    except:
        return redirect('admin_index')        

def edit_product(request, pk):
    if request.method == "GET":
        all_products = product_sub_cat.objects.get(id = pk)
        return render(request, 'edit_product.html', {'all_p':all_products})
    else:
        
        all_products = product_sub_cat.objects.get(id= pk)
        all_products.product_model = request.POST['model']
        all_products.product_ram = request.POST['ram']
        all_products.product_image = request.FILES['p_image']
        all_products.product_price = request.POST['price']
        all_products.save()
        return render(request, 'edit_product.html', {'all_p':all_products})

def product_manager(request):
    all_products = product_sub_cat.objects.all()
    return render(request, 'product_manager.html', {'all_p':all_products})

def searched_product(request):
    search_words = request.POST['search']
    filtered_products = product_sub_cat.objects.filter(p_name__product_name__icontains = search_words)
    return render(request, 'search_product.html', {'s_products': filtered_products})
    
def del_product(request):
    p_obj = product_sub_cat.objects.get(id = request.GET['pid'])
    p_obj.delete()
    
    all_products = list(product_sub_cat.objects.values())
    for i in range(len(all_products)):
        pro_obj = product_mst.objects.get(id = all_products[i]['p_name_id'])
        all_products[i]['product_name'] = pro_obj.product_name
    return JsonResponse({'updated_data':all_products})
