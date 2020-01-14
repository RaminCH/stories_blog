from django.shortcuts import render
from stories.models import *
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .forms import *
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin, UpdateView
from django.contrib.auth.models import User
from stories.forms import *

# Create your views here.

# def about(request):
#     context = {}
#     if request.method == 'GET':
#         context['content'] = AboutPage.objects.last()
#     return render(request, 'stories/about.html', context)

class AboutView(TemplateView):
    template_name = 'stories/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content'] = AboutPage.objects.last()
        return context

# def contact(request):
#     form = ContactForm()
#     context = {
#         'form': form
#     }
#     if request.method == "POST":
#         print(request.POST)
#         # print('Post sorgusu geldi!')
#         form = ContactForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             context['message'] = 'Your message sent successfully'
#         else:
#             context['form'] = form.errors
#     return render(request, 'stories/contact.html', context)

class ContactView(CreateView):
    model = Contact
    template_name = 'stories/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('stories:contact')


class SubscriberView(CreateView):
    model = Subscriber 
    form_class = SubscriberForm
    success_url = reverse_lazy('stories:index')
    http_method_names = ('post',)    

def create_story(request):
    return render(request, 'stories/create_story.html')

def email_subscribers(request):
    return render(request, 'stories/email-subscribers.html')

def index(request):
    return render(request, 'stories/index.html')

# def recipes(request):
#     page_number = request.GET.get('page', 1)
#     recipes = Recipe.objects.all()
#     p = Paginator(recipes, 1) # 1 means how many objects on the page
#     # if isinstance(page_number, int) and int(page_number) > p.num_pages:
#     #     page_number = p.num_pages

#     if not page_number.isdigit():
#         page_number = 1
#     elif int(page_number) > p.num_pages:
#         page.number = p.num_pages
#     recipe_list = p.page(page_number)  #p.page(1) # 1 shows 1-st page, if we put Number 2... shows others
#     # print('recipes', recipes)
#     context = {
#         'recipes': recipe_list  #recipes
#     }
#     return render(request, 'stories/recipes.html', context)

class RecipeView(ListView):
    model = Recipe
    template_name = 'stories/recipes.html'
    context_object_name = 'recipes'
    paginate_by = 1 #number of pages

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #     context['categories'] = Category.objects.all()
    #     return context // base_filters-de  @register.simple_tag
                                            # def get_categories():
                                            #     return Category.objects.all()
                                            #     oz uzerine goturur



# def single(request, pk):
#     recipe = Recipe.objects.get(id=pk)
#     context = {
#         'recipe_data':recipe,
#     }
#     return render(request, 'stories/single.html', context)

class SingleRecipeView(FormMixin, DetailView): # Single-nin class base-i
    model = Recipe
    template_name = "stories/single.html"
    context_object_name = "recipe_data"
    form_class = CommentForm

    # def get_queryset(self, request, *args, **kwargs):

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_count = obj.view_count + 1
        obj.save()
        return obj
    

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.replied_comment = request.POST.get('reply_comment')
        form = self.get_form()
        # form.save(commit=False)
        if form.is_valid():
            print('here')
            return self.form_valid(form)
        else:
            print('here 2')
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.recipe = self.object
        if not self.replied_comment is None and self.replied_comment.isdigit():
            r_comment = Comment.objects.get(id=int(self.replied_comment))
            comment.reply_comment = r_comment 
        comment.save()
        self.success_url = reverse_lazy('stories:single', kwargs=
        {'pk': self.object.id})
        return super().form_valid(form)




def stories(request):
    return render(request, 'stories/stories.html')

# def user_profile(request):
#     return render(request, 'stories/user_profile.html')

class UserProfileView(DetailView):
    model = User
    template_name = 'stories/user-profile.html'

class UserEditView(UpdateView):
    model = User
    template_name = 'stories/user-edit.html'
    form_class = EditUserForm

    def get_success_url(self):
        return reverse_lazy('stories:user-profile' , kwargs={'pk': self.request.user.pk})