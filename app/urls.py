from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("signin", views.sign_in, name="sign_in"),
    path("signup", views.sign_up, name="sign_up"),
    path("sign_in", views.login_form, name="login_form"),
    path("sign_up", views.sign_up_form, name="sign_up_form"),
    path("showcart", views.show_cart, name="show_cart"),
    path("deliver", views.deliverto, name="deliverto"),
    path("payment", views.paymentmethod, name="paymentmethod"),
    path("ordersuccess", views.order, name="order"),
    path("success", views.success, name="success"),
    path("signerror", views.sign_error, name="sign_error"),
    path("cameras", views.show_cameras, name="show_cameras"),
    path("showproduct/<id1>", views.show_product, name="show_product"),
    path("cart/<int:id2>", views.to_cart, name="to_cart"),
    path("addmsg", views.addedmsg, name="addedmsg"),
    path("accessories", views.show_accessories, name="show_accessories"),
    path("to_cart/<id4>,<id5>,<id>", views.usercart, name="usercart"),
    
  

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
