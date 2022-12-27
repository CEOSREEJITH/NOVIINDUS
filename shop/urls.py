from django.urls import path
from . import views
app_name='shop'
urlpatterns = [

    path('',views.allProdCat,name='allProdCat'),
    path('shop/login/shop/',views.allProdCat,name='allProdCat'),
    path('login/',views.LoginPage,name='login'),
    path('signup/',views.SignupPage,name='signup'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail'),
]