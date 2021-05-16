from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):

   fieldsets = ((
        "Custom Profile",
        {
            "fields": (
                "email",
                "fav_pro_genre",
                "name",
                "major",
                "grade",
                "entered_eniac",
                "profile_image",
                
            )
        },
    ), )
        
#tkfkddksdptj shrrh 