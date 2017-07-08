from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^about/$', views.about,name='about'),
    url(r'^goPremium/$', views.goPremium, name='goPremium'),
    url(r'^get-premium/$', views.get_premium, name='get-premium'),
    url(r'^change-password/$', views.change_password, name='change-password'),
    url(r'^user-account/$', views.userAccount, name='user-account'),
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'resetPassword/password_reset.html', 'email_template_name':'resetPassword/password_reset_email.html',
                                                          'subject_template_name':'resetPassword/password_reset_subject.txt'}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'resetPassword/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name': 'resetPassword/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name': 'resetPassword/password_reset_complete.html'}, name='password_reset_complete'),
]