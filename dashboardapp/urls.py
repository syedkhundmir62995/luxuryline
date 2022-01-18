from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard, name= 'dashboardpage'),
    path('AddMaterial',views.material,name='materialpage'),
    path('AddScale',views.scale,name='scalepage'),
    path('AddSupplier',views.supplier,name = 'supplierpage'),
    path('EditMaterial/<str:id>',views.editmaterial,name = 'editmaterialpage'),
    path('ViewMaterial',views.viewmaterial,name = 'viewmaterialpage'),
    path('DeleteMaterial/<str:id>',views.deletematerial,name = 'deletematerialpage'),

]
