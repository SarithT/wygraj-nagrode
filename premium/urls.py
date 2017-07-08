from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$',views.premium, name='premium'),
    url(r'^about/$',views.aboutPremium, name='aboutPremium'),
    url(r'^howItWorks/$', views.howItWorks, name='howItWorks'),
    url(r'^dowcipy/$',views.dowcipy,name='dowcipy'),
    url(r'^tapety/$', views.tapety,name='tapety'),
    url(r'^charge-points/',views.chargePoints,name='chargePoints'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^exchangePoints/', views.exchangePointsToVouchers, name='exchangePoints'),
    url(r'^vouchers/$', views.vouchers, name='vouchers'),
    url(r'^ranking/$', views.ranking, name='ranking'),
    url(r'^prizes/$', views.prizes, name='prizes'),
    url(r'^get-code/$', views.getCode, name='getCode'),
]