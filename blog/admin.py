from django.contrib import admin
from .models import Post

# created superuser and password from command line
# usr:superuser, pwd:superuser, email: superuser@email.com

# Register your models here.
admin.site.register(Post)