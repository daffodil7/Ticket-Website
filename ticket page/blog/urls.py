from django.urls import path, re_path
from blog import views

app_name = 'blog'
urlpatterns = [
    # Example: /blog/
    path('',views.PostLV.as_view(),name='index'),
    
    # Example: /blog/post/ (same as /blog/)
    path('post/',views.PostLV.as_view(),name='post_list'),
    
    # Example: /blog/post/django-example/
    re_path(r'^post/(?P<slug>[-\w]+)/$',views.PostDV.as_view(),name='post_detail'),
    
    # Example: /blog/archive/
    path('archive/',views.PostAV.as_view(),name='post_archive'),
    
    # Example: /blog/archive/2022/
    path('archive/<int:year>/',views.PostYAV.as_view(),name='post_year_archive'),
    
    # Example: /blog/archive/2022/sep/
    path('archive/<int:year>/<str:month>/',views.PostMAV.as_view(),name='post_month_archive'),

    # Example: /blog/archive/2022/sep/16/
    path('archive/<int:year>/<str:month>/<int:day>/',views.PostDAV.as_view(),name='post_day_archive'),
    
    # Example: /blog/archive/today/
    path('archive/today/',views.PostTAV.as_view(),name='post_today_archive'),
    
    # tag cloud 페이지 추가
    path('tag/',views.TagCloudLV.as_view(),name='tag_cloud'),
    
    # tagged object list 추가
    path('tag/<str:tag>/',views.TaggedObjectLV.as_view(), name='tagged_object_list'),
    
    path('search/',views.SearchFormView.as_view(), name='search'),
    
    path('add/',views.PostCreateView.as_view(),name='add'),
    path('change/',views.PostChangeLV.as_view(),name='change'),
    path('<int:pk>/update/',views.PostUpdateView.as_view(),name='update'),
    path('<int:pk>/delete/',views.PostDeleteView.as_view(),name='delete'),
]
