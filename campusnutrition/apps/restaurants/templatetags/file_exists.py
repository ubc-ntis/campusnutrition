from django import template
from django.core.files.storage import default_storage
from django.contrib.staticfiles import finders

register = template.Library()

@register.filter(name='file_exists')
def file_exists(filepath):
    # Replace all spaces with dashes
    file_path_correct = filepath.replace(" ", "-").lower() + ".png"
    absolute_path = finders.find(file_path_correct)
    print(absolute_path)

    if absolute_path:
        return file_path_correct
    else:
        return "placeholder.png"
