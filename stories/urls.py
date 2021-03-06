from django.urls import path, include
from .views import *
# from api.urls import urlpatterns as api_urls


app_name = 'stories'

urlpatterns = [
    path('',index, name='index'), #home
    # path('about/',about, name='about'),
    path('about/',AboutView.as_view(), name='about'),
    # path('contact/',ContactView.as_view(), name='contact'),
    path('contact/',ContactView.as_view(), name='contact'),
    # path('contact/',contact, name='contact'),
    path('create_story/',create_story, name='create_story'),
    path('email_subscribers/',email_subscribers, name='email_subscribers'),
    # path('recipes/',recipes, name='recipes'),
    path('recipes/',RecipeView.as_view(), name='recipes'),
    # path('single/<int:pk>/',single, name='single'), #int is the integer / pk is the primary key
    path('single/<int:pk>/',SingleRecipeView.as_view(), name='single'), 
    path('stories/',stories, name='stories'),
#   path('user_profile/<int:pk>',user_profile, name='user_profile')
    path('user-profile/<int:pk>/',UserProfileView.as_view(), name='user-profile'),
    path('user-edit/<int:pk>/',UserEditView.as_view(), name='user-edit'),
    path('subscribe/', SubscriberView.as_view(), name='subscribe'),
    path("api/", include('stories.api.urls')),
]

# urlpatterns += api_urls
