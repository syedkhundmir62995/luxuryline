# from typing_extensions import Required

from django import forms
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from suppliers.forms import MaterialForm, SupplierForm
from suppliers.models import Material, Scale, Supplier
from django.core.paginator import Paginator, EmptyPage


def dashboard(request):
    return render(request,'dashboardapp/dashboard.html')

def material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        print("Form Data:",form)
        print("Request Data:",request.POST)
        
        if form.is_valid():
            mid = request.POST['mid']
            material = request.POST['material']
            quantity = request.POST['quantity']
            scale = request.POST['scale']
            supplier = request.POST['supplier']
            color = request.POST['color']
            lastupdated = request.POST['lastupdated']
            if Material.objects.filter(mid = mid).exists():
                messages.error(request,"MID Already Exist")
                return redirect('materialpage')
            else:
                obj = Material(mid = mid,material = material,quantity = quantity, scaleid_id = scale,color = color,date = lastupdated,suupplierid_id = supplier)
                print("$$$")           
                obj.save()
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
        newscale = request.POST['newscale']
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
            sname = form.cleaned_data['suppliername']
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
        form = MaterialForm(request.POST)
        print(request.POST)
        if form.is_valid():
            edit_material = request.POST['material']
            edit_quantity = request.POST['quantity']
            edit_scale = request.POST['scale']
            edit_color = request.POST['color']
            edit_lastupdated = request.POST['lastupdated']
            edit_supplier = request.POST['supplier']

            query_data.material = edit_material
            query_data.quantity = edit_quantity
            query_data.scaleid_id = edit_scale
            query_data.color = edit_color
            query_data.date = edit_lastupdated
            query_data.suupplierid_id = edit_supplier
            query_data.save()
            messages.success(request,"Material Edited")
            return redirect('viewmaterialpage')
        

        else:
            messages.error('Error! Try again')
            return redirect('viewmaterialpage')

    form = MaterialForm()
    scale_data = Scale.objects.all()
    supplier_data = Supplier.objects.all()
    material_data = Material.objects.get(uid = id)
    return render(request, 'dashboardapp/EditMaterial.html',context={'form':form,'data':scale_data,'supplier_data':supplier_data,'obj':material_data})


def viewmaterial(request):
    material_data = Material.objects.all().select_related('scaleid','suupplierid')
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