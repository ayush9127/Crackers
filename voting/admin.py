from django.contrib import admin
from .models import Election, Candidate, Vote


class CandidateInline(admin.TabularInline):
    """Show candidates directly inside the Election admin page."""
    model = Candidate
    extra = 2
    fields = ['name', 'description']


@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'start_time', 'end_time', 'total_votes', 'created_at']
    list_filter = ['start_time', 'end_time']
    search_fields = ['title', 'description']
    inlines = [CandidateInline]
    readonly_fields = ['created_at']

    def status(self, obj):
        return obj.status
    status.short_description = 'Status'


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'election', 'vote_count']
    list_filter = ['election']
    search_fields = ['name', 'election__title']


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['voter', 'election', 'candidate', 'voter_ip', 'voted_at']
    list_filter = ['election', 'voted_at']
    search_fields = ['voter__username', 'election__title', 'candidate__name']
    readonly_fields = ['voter', 'election', 'candidate', 'voter_ip', 'voted_at']

    # Votes should never be editable — only viewable for audit
    def has_add_permission(self, request):
        return False
