from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('contact/', views.contact_us,name="contact"),
    path('about/', views.about_us,name="about"),

    # -------------------------product one----------------------------------
    path('product/productone/one'   , views.ProductOneView.as_view() , name="p1p1"),
    path('product/productone/two'   , views.ProductTwoView.as_view() , name="p1p2"),
    path('product/productone/three' , views.ProductThreeView.as_view() , name="p1p3"),
    path('product/productone/four'  , views.ProductFourView.as_view() , name="p1p4"),
    # ---------------------------product one end----------------------------

    # -------------------------product two----------------------------------
    path('product/producttwo/one'   , views.product2_product1 , name="p2p1"),
    path('product/producttwo/two'   , views.product2_product2 , name="p2p2"),
    path('product/producttwo/three' , views.product2_product3 , name="p2p3"),
    path('product/producttwo/four'  , views.product2_product4 , name="p2p4"),
    # ---------------------------product two end----------------------------

    # -------------------------product three -------------------------------
    path('product/productthree/one'   , views.product3_product1 , name="p3p1"),
    path('product/productthree/two'   , views.product3_product2 , name="p3p2"),
    path('product/productthree/three' , views.product3_product3 , name="p3p3"),
    path('product/productthree/four'  , views.product3_product4 , name="p3p4"),
    # ---------------------------product three end---------------------------

    # -------------------------product four----------------------------------
    path('product/productfour/one'   , views.product4_product1 , name="p4p1"),
    path('product/productfour/two'   , views.product4_product2 , name="p4p2"),
    path('product/productfour/three' , views.product4_product3 , name="p4p3"),
    path('product/productfour/four'  , views.product4_product4 , name="p4p4"),
    # ---------------------------product four end----------------------------

    # path('about/', views.about_us,name="aboutthree
]