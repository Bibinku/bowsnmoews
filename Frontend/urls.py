from django.urls import path
from Frontend import views


urlpatterns=[
   path('',views.homepage,name="homepage"),
   path('aboutpage',views.aboutpage,name="aboutpage"),

   path('servicepage',views.servicepage,name="servicepage"),
   path('contactpage',views.contactpage,name="contactpage"),
   path('breadpage',views.breadpage,name="breadpage"),
   path('savecontact',views.savecontact,name="savecontact"),
   path('accessoriespage',views.accessoriespage,name="accessoriespage"),
   path('foodpage',views.foodpage,name="foodpage"),
   path('servicepage',views.servicepage,name="servicepage"),

   path('cartdetails',views.cartdetails,name="cartdetails"),
   path('signuppage',views.signuppage,name="signuppage"),
   path('signinpage',views.signinpage,name="signinpage"),
   path('save_user/', views.save_user, name="save_user"),
   path('userlogin/', views.userlogin, name="userlogin"),
   path('userlogout/', views.userlogout, name="userlogout"),
   path('savebookslot/', views.savebookslot, name="savebookslot"),
   path('singleitem/<int:Fid>/', views.singleitem, name="singleitem"),
   path('savecart/', views.savecart, name="savecart"),
   path('singlepageacc/<int:Aid>/', views.singlepageacc, name="singlepageacc"),
   path('Deletecart/<int:cartid>/', views.Deletecart, name="Deletecart"),
   path('singlepet/<int:Pid>/', views.singlepet, name="singlepet"),
   path('checkoutpage/', views.checkoutpage, name="checkoutpage"),
   path('saveorder/', views.saveorder, name="saveorder"),
   path('feedbacknotification/', views.feedbacknotification, name="feedbacknotification"),
   path('savefeedback/', views.savefeedback, name="savefeedback"),
   path('singleservice/<int:Sid>/', views.singleservice, name="singleservice"),
   path('bookings/<int:Bid>/', views.bookings, name="bookings"),
   path('booking_pdf/<int:booking_id>/', views.booking_pdf, name="booking_pdf"),

   path('paymentpage/', views.paymentpage, name="paymentpage"),
   path('send_login_confirmation_email/<user_email>', views.send_login_confirmation_email, name="send_login_confirmation_email"),



]