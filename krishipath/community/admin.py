

from django.contrib import admin
from .models import ChatMessage, BlockedUser

admin.site.register(ChatMessage)
admin.site.register(BlockedUser)
