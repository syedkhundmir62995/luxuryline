from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.dashboard, name= 'dashboardpage'),
    path('AddMaterial',views.material,name='materialpage'),
    path('AddScale',views.scale,name='scalepage'),
    path('AddSupplier',views.supplier,name = 'supplierpage'),
    path('EditMaterial/<str:id>',views.editmaterial,name = 'editmaterialpage'),
    path('ViewMaterial',views.viewmaterial,name = 'viewmaterialpage'),
    path('DeleteMaterial/<str:id>',views.deletematerial,name = 'deletematerialpage'),
    path('View/<str:mid>/<str:uid>',views.view,name = 'viewpage'),
    path('SalesDashboard',views.salesdashboard,name = 'salesdashboardpage'),
    path('AddQuotation',views.addquotation,name = 'addquotationpage'),
    path('ViewQuotation',views.viewquotation,name = 'viewquotationpage'),
    path('AddNewQuotation',views.addnewquotation,name = 'addnewquotationpage'),
    path('ViewQuotationNumber/<int:quotation_number>',views.viewquotationnumber,name = 'viewquotationnumberpage'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

