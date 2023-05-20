
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,PasswordChangeForm,ForgotPassword,MySetPasswordForm


urlpatterns = [

    path('',views.ProductView.as_view(),name='ProductView'),
    # path('product-detail/', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>',views.ProductDetailsView.as_view(),name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    path('topwear/', views.topWear, name='topwear'),
    path('topwear/<slug:data>', views.topWear, name='topweardata'),
    path('bottomwear/', views.bottomWear, name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottomWear, name='bottomweardata'),
    path('smartwatch/', views.smartwatch, name='smartwatch'),
    path('smartwatch/<slug:data>', views.smartwatch, name='smartwatchdata'),


    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # ---------change password -----
    path('changepassword/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class= PasswordChangeForm, success_url= '/passwordchangedone/' ), name='passwordchange'),
    # ----------change password done--------
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),

    # ----------reset password --------
    path('reset-password/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=ForgotPassword),name='password_reset'),

    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64><token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),

    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),




    path('checkout/', views.checkout, name='checkout'),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)