from django.contrib import admin
from board_app.models import BoardFlowPost

@admin.register(BoardFlowPost)
class BoardFlowPost(admin.ModelAdmin):
    pass
