from django import template
from stories.models import NavLinks, Category, Comment
from string import capwords
from stories.forms import SubscriberForm

register = template.Library()

@register.simple_tag
def get_nav_links():
    return NavLinks.objects.filter(active=True)



@register.filter
def custom_text_edit(value, mode):
    if mode == 'upper':
        return value.upper()
    elif mode == 'lower':
        return value.lower()


# @register.filter
# def custom_capitalize(value):
    # return capwords(value) #makes first letters capitalized
    # # return value.upper() makes all uppercase
    # # return value.lower() makes all lowercase


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag
def get_comments(recipe_id):
    return Comment.objects.filter(recipe=recipe_id, reply_comment__isnull=True)


@register.simple_tag
def get_subscriber_form():
    return SubscriberForm()



