from django.contrib import admin

from django.contrib import admin
from .models import Review, Product

admin.site.register(Review)
admin.site.register(Product)
from django.contrib import admin

# Below code for hiding unwanted modesl from admin panel
from social_django.models import Association, Nonce, UserSocialAuth
admin.site.unregister(Association)
admin.site.unregister(Nonce)
admin.site.unregister(UserSocialAuth)

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)
