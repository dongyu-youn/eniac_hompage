from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):

   fieldsets = UserAdmin.fieldsets + ((
        "Custom Profile",
        {
            "fields": (
                "major",
                "fav_pro_genre",
                "grade",
            )
        },
    ), )
        
#tkfkddksdptj shrrh 