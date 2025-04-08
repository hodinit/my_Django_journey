import os
import django
# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth.models import User
from boards.models import Board, Topic, Post
from django.core.paginator import Paginator



print(Topic.objects.count())
print(Topic.objects.filter(board__name='Django').count())

queryset = Topic.objects.filter(board__name='Django').order_by('-last_updated')
paginator = Paginator(queryset, 20)

print(paginator.num_pages)
print(paginator.page(2))

page = paginator.page(2)

print(type(page))
print(type(paginator))
print(page.previous_page_number())

