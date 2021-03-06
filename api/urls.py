from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tags$', views.TagList.as_view(), name='tag-list'),
    url(r'^tags/(?P<pk>[0-9]+)$', views.TagDetail.as_view(), name='tag-detail'),

    url(r'^recipes$', views.RecipeList.as_view(), name='recipe-list'),

    url(r'^ingredients$', views.IngredientList.as_view(), name='ingredient-list'),
    url(r'^scheduleEntries$', views.ScheduleEntryList.as_view(), name='schedule-entry-list'),
    url(r'^$', views.BookList.as_view(), name='book-list'),

]
