# from typing_extensions import Required

from django import forms
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from suppliers.forms import MaterialForm, SupplierForm, EditMaterialForm
from suppliers.models import Material, Scale, Supplier, MaterialTransaction
from django.core.paginator import Paginator, EmptyPage


def dashboard(request):
    return render(request,'dashboardapp/dashboard.html')

def material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        print("Form Data:",form)
        print("Request Data:",request.POST)
        
        if form.is_valid():
            mid = request.POST['mid'].upper()
            material = request.POST['material'].capitalize()
            quantity = request.POST['quantity']
            scale = request.POST['scale'].capitalize()
            supplier = request.POST['supplier'].capitalize()
            color = request.POST['color'].capitalize()
            lastupdated = request.POST['lastupdated']
            if Material.objects.filter(mid = mid).exists():
                messages.error(request,"MID Already Exist")
                return redirect('materialpage')
            else:
                obj = Material(mid = mid,material = material,quantity = quantity, scaleid_id = scale,color = color,date = lastupdated,suupplierid_id = supplier)
                print("$$$")           
                obj.save()

                obj2 = MaterialTransaction(mid = mid, material = material, quantity = quantity, scaleid_id = scale,date = lastupdated, color = color , suupplierid_id = supplier)
                print("***")
                obj2.save()
                messages.success(request,"New Material Added")
                return redirect("viewmaterialpage")
        else:
            messages.error(request,"Form not Valid")
            mid = request.POST['mid']
            material = request.POST['material']
            quantity = form.cleaned_data['quantity']
            # scale = form.cleaned_data['scale']
            scale = request.POST['scale']
            color = request.POST['color']
            
            lastupdated = request.POST['lastupdated']
            ## Mid should be unique
            if Material.objects.filter(mid = mid).exists():
                print("MID Exist")
                messages.error(request,"MID Already Exist")
                return redirect("materialpage")
            ## Material should be unique
            elif Material.objects.filter(material = material).exists():
                print("Material Exist")
                messages.error(request,"Material Already Exist")
                return redirect("materialpage")
            return redirect("materialpage")
    else:
        form = MaterialForm()
        data = Scale.objects.all()
        supplier_data = Supplier.objects.all()
        return render(request,'dashboardapp/AddMaterial.html',{'form':form,'data':data,'supplier_data':supplier_data})



def scale(request):
    if request.method == 'POST':
        newscale = request.POST['newscale'].capitalize()
        print(newscale)
        if Scale.objects.filter(scale = newscale).exists():
            messages.error(request,"Scale Already Exist")
            return redirect('scalepage')
        else:
            obj = Scale(scale = newscale)
            obj.save()
            messages.success(request,"New Scale Successfully Added")
            return redirect('scalepage')

    else:
        return render(request,'dashboardapp/scale.html')

def supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        # print(form)
        if form.is_valid():
            sname = form.cleaned_data['suppliername'].capitalize()
            saddress = form.cleaned_data['supplieraddress']
            svat = form.cleaned_data['vat']
            obj = Supplier(supplier_name = sname,supplier_address = saddress,vat = svat)
            obj.save()
            messages.success(request,"New Supplier Added")
            return redirect('supplierpage')

        else:
            messages.error(request,"Invalid Data Entered!!")
            return redirect('supplierpage')

    form = SupplierForm()
    return render(request,'dashboardapp/supplier.html',context={'form':form})



def editmaterial(request,id):
    query_data = Material.objects.get(uid = id)
    if request.method == 'POST':
        form = EditMaterialForm(request.POST)
        print(request.POST)
        if form.is_valid():
            # edit_material = request.POST['material']
            edit_quantity = request.POST['quantity']
            # edit_scale = request.POST['scale']
            # edit_color = request.POST['color']
            edit_lastupdated = request.POST['lastupdated']
            # edit_supplier = request.POST['supplier']

            # query_data.material = edit_material
            query_data.quantity = edit_quantity
            # query_data.scaleid_id = edit_scale
            # query_data.color = edit_color
            query_data.date = edit_lastupdated
            # query_data.suupplierid_id = edit_supplier
            query_data.save()
            messages.success(request,"Material Edited")

            query = Material.objects.get(uid = id)
            #Saving this edited transaction into MaterialTransaction Table
            obj2 = MaterialTransaction(mid = query.mid, material = query.material, quantity = query.quantity, color = query.color, date = query.date ,scaleid_id = query.scaleid_id, suupplierid_id = query.suupplierid_id)
            obj2.save()
            return redirect('viewmaterialpage')
        

        else:
            messages.error(request,'Error! Try again')
            return redirect('viewmaterialpage')

    form = EditMaterialForm()
    material_data = Material.objects.get(uid = id)
    #Create a table wj=hich stores all transaction wrt mid and you extract top three latest records wrt date
    return render(request, 'dashboardapp/EditMaterial.html',context={'form':form,'obj':material_data})


def viewmaterial(request):
    material_data = Material.objects.all().select_related('scaleid','suupplierid').order_by('-last_updated')
    # for obj in material_data:
    #     print(obj.mid,' ',obj.scaleid.scale,' ',obj.suupplierid.supplier_name)
    
    p = Paginator(material_data,5)
    page_num = request.GET.get('page',1)
    # page_obj = p.get_page(page_num)
    try:
        page_obj = p.get_page(page_num)
    
    except EmptyPage:
        page_obj = p.get_page(1)
    
   


    return render(request,'dashboardapp/viewmaterial.html',{'material_data':page_obj})



def deletematerial(request,id):
    query_data = Material.objects.get(uid = id)
    if request.method == 'POST':
        query_data.delete()
        messages.success(request,"Material Deleted")
        return redirect('viewmaterialpage')
    else:

        return render(request,'dashboardapp/deletematerial.html',{'obj':query_data})



def view(request,mid,uid):
    #Accept a uid for each material
    #Fetch data stored in db 
    #data should be fetch according to updated time
    #I suggest you to keep auto_now so that django itself keeps track of updated date time
    #Make a datetime field, so that even a second difference is taken into account
    #Fetch only top 3 records from the db
    query_data = MaterialTransaction.objects.filter(mid = mid).order_by('-last_updated')
    query_info = Material.objects.get(uid = uid)

    p = Paginator(query_data,5)
    page_num = request.GET.get('page',1)

    try:
        page_obj = p.page(page_num)
    except EmptyPage:
        page_obj = p.page(1)
    
    return render(request,'dashboardapp/viewpage.html',{'items':page_obj,'query_info':query_info})




def salesdashboard(request):
    return render(request,'dashboardapp/salesdashboard.html')