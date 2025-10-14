"""schoolerp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path, include

from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.utils.translation import gettext_lazy as _

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls
from two_factor.urls import urlpatterns as tf_urls

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
 #   path('admin/', admin.site.urls),
    path('', include('eschool.urls')),
    # path('i18n/', include('django.conf.urls.i18n')),

    # path('', include(tf_urls)),
    #  path('', include(tf_twilio_urls)),
    #  path('', include('user_sessions.urls', 'user_sessions')),
     path('admin/', admin.site.urls),
    path("api/", include("users.urls")),
    path("users/", include("users.web_urls")), # only HTML route
    path("courses/", include("users.course_urls")), # only HTML route
    path("teachers/", include("teachers.urls")), # only HTML route
    #path("api/teachers/", include("teachers.api_urls")), # only API route
    path('blog/', include('blog.urls')),
    #path('ckeditor/', include('ckeditor_uploader.urls')),

    

]



# Add internationalization URL patterns
# urlpatterns += i18n_patterns(
#     path('', include('eschool.urls')),
# )





if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]



if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = [
#     # path(
#     #     '',
#     #     HomeView.as_view(),
#     #     name='home',
#     # ),
#     # path(
#     #     'account/logout/',
#     #     LogoutView.as_view(),
#     #     name='logout',
#     # ),
#     # # path(
#     # #     'secret/',
#     # #     ExampleSecretView.as_view(),
#     # #     name='secret',
#     # # ),
#     # path(
#     #     'account/register/',
#     #     RegistrationView.as_view(),
#     #     name='registration',
#     # ),
#     # path(
#     #     'account/register/done/',
#     #     RegistrationCompleteView.as_view(),
#     #     name='registration_complete',
#     # ),
#     #path('', include(tf_urls)),
#     path('', include(tf_twilio_urls)),
#     path('', include('user_sessions.urls', 'user_sessions')),
#     path('admin/', admin.site.urls),
# ]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ]
