from django.urls import path 
from . import views


urlpatterns = [ path("", views.loginpage, name="loginpage"),
               path("Pledge-Returns-summary/", views.homepage, name="homepage"),
               path("Pledge-Returns-Monthly-summary/<int:yr>/", views.monthlysum, name="monthlysum"),
               path("Register/", views.registerpage, name="registerpage"),
               path("member-addpledge/", views.addpledge, name="addpledge"),
               path("Member-Returns-summary/", views.pledgesummary, name="pledgesummary"),
               path("member-search/", views.membersearch, name="membersearch"),
               path("Pledges-committment-records>", views.viewpledge, name="viewpledge"),
               path("Pledges-receipts/<str:nm>/<int:id>", views.addreceipt, name="addreceipt"),
               path("Pledges-receipts-records>", views.viewrecords, name="viewrecords"),
               path('update_receipt/', views.updateReceipt, name='update_receipt'),
               path('Import-File/', views.ImportingFiles, name='ImportingFiles'),
               path('Export-File/', views.ExportingFiles, name='ExportingFiles'),
              


               #files url
               path('ReceiptsData/', views.rctFiles, name='rctFiles'),
               path('ContactData/', views.memContact, name='ContactData'),
               path('Memberspledge/<int:yr>/', views.Memberspledge, name='Memberspledge'),
               path('Memberspayments/<int:yr>/', views.Memberspayments, name='Memberspayments'),
               #path('Membersbalances/<int:yr>/', views.Membersbalances, name='Membersbalances'),
               
                           
               ]
