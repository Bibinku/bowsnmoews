from django.urls import path
from Petend import views

urlpatterns = [
    path('Indexpage/',views.Indexpage,name="Indexpage"),
    path('addcategory/',views.addcategory,name="addcategory"),
    path('savecategory/',views.savecategory,name="savecategory"),
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('editcategory/<int:Cid>/',views.editcategory,name="editcategory"),
    path('updatecategory/<int:Cid>/',views.updatecategory,name="updatecategory"),
    path('deletecategory/<int:Cid>/',views.deletecategory,name="deletecategory"),
    path('addbread/',views.addbread,name="addbread"),
    path('savebread/',views.savebread,name="savebread"),
    path('displaybread/',views.displaybread,name="displaybread"),
    path('editbread/<int:Bid>/', views.editbread, name="editbread"),
    path('deletebread/<int:Bid>/', views.deletebread, name="deletebread"),
    path('updatebread/<int:Bid>/', views.updatebread, name="updatebread"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admin/', views.admin, name="admin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('displaycontact/', views.displaycontact, name="displaycontact"),
    path('deletecontact/<int:CONid>/', views.deletecontact, name="deletecontact"),
    path('addfood/', views.addfood, name="addfood"),
    path('savefood/', views.savefood, name="savefood"),
    path('displayfood/', views.displayfood, name="displayfood"),
    path('editfood/<int:Fid>/', views.editfood, name="editfood"),
    path('deletefood/<int:Fid>/', views.deletefood, name="deletefood"),
    path('updatefood/<int:Fid>/', views.updatefood, name="updatefood"),
    path('addaccessories/', views.addaccessories, name="addaccessories"),
    path('saveaccessories/', views.saveaccessories, name="saveaccessories"),
    path('displayaccessories/', views.displayaccessories, name="displayaccessories"),
    path('editaccessories/<int:Aid>/', views.editaccessories, name="editaccessories"),
    path('deleteaccessories/<int:Aid>/', views.deleteaccessories, name="deleteaccessories"),
    path('updateaccessories/<int:Aid>/', views.updateaccessories, name="updateaccessories"),
    path('addservice/', views.addservice, name="addservice"),
    path('saveservice/', views.saveservice, name="saveservice"),
    path('displayservice/', views.displayservice, name="displayservice"),
    path('editservice/<int:Sid>/', views.editservice, name="editservice"),
    path('deleteservice/<int:Sid>/', views.deleteservice, name="deleteservice"),
    path('updateservice/<int:Sid>/', views.updateservice, name="updateservice"),
    path('addservice1/', views.addservice1, name="addservice1"),
    path('saveservice1/', views.saveservice1, name="saveservice1"),
    path('displayservice1/', views.displayservice1, name="displayservice1"),
    path('editservice1/<int:S1id>/', views.editservice1, name="editservice1"),
    path('deleteservice1/<int:S1id>/', views.deleteservice1, name="deleteservice1"),
    path('updateservice1/<int:S1id>/', views.updateservice1, name="updateservice1"),
    path('displaybookslot/', views.displaybookslot, name="displaybookslot"),
    path('deletebookslot/<int:Bookid>/', views.deletebookslot, name="deletebookslot"),
    path('displayfeedback/', views.displayfeedback, name="displayfeedback"),
    path('deletefeedback/<int:fid>/', views.deletefeedback, name="deletefeedback"),


    path('displayorder/', views.displayorder, name="displayorder"),
    path('deleteorder/<int:Oid>/', views.deleteorder, name="deleteorder"),








]
