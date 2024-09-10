from django.urls import path
from .views import Create_Article,Article_view,Update_article,Delete_article,Article_detail
from .views import Create_categorie,Update_categorie,Delete_categorie,View_categorie,Brouillon_view
from .views import categorieselement,commentaire,category_view

app_name = 'articles'
urlpatterns = [
    path('create-article/',Create_Article.as_view(),name='create_article'),
    path('',Article_view.as_view(),name='article_view'),
    path('article-detail/<int:pk>',Article_detail.as_view(),name='article_detail'),
    path('update-article/<int:pk>',Update_article.as_view(),name='update_article'),
    path('delete-article/<int:pk>',Delete_article.as_view(),name='delete_article'),
    path('brouillons/',Brouillon_view.as_view(),name='bouillons_view'),
    
    #les categories
    
    path('create-categorie/',Create_categorie.as_view(),name='create_categorie'),
    path('update-categorie/<int:pk>',Update_categorie.as_view(),name='update_categorie'),
    path('delete-categorie/<int:pk>',Delete_categorie.as_view(),name='delete_categorie'),
    path('view-categorie/',View_categorie.as_view(),name='view_categorie'),
    
    path('article-by-categorie/<str:categorie>',categorieselement,name='article_by_categorie'),
    path('commentaire/<int:pk>',commentaire,name='commentaire'),
    path('drop/',category_view,name='drop'),
]