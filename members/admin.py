from django.contrib import admin
from .models import Members, Salary
from rangefilter.filter import DateRangeFilter


class MembersAdmin(admin.ModelAdmin):
	list_display = ['firstname', 'lastname']

class SalaryAdmin(admin.ModelAdmin):
	list_display = ('members', 'company_name', 'amount', 'salary_date')
	search_fields = ('amount', 'members__firstname')
	ordering = ('-amount',)
	list_filter = (
			'members',
			'company_name',
			'amount',
			('salary_date', DateRangeFilter)
	)
	list_per_page = 3

	# fields = ('members', 'amount', 'company_name')
	list_editable = ('amount',)
	exclude = ('company_name', )
	readonly_fields = ('salary_date',)

	# def has_add_permission(self, request):
	# 	return False

	def has_delete_permission(self, request, obj=None):
		return False

	def changelist_view(self, request, extra_context=None):
		extra_context = extra_context or {}
	
		# extra_context['has_add_permission'] = False
		extra_context['title'] = "Member Salary List"


		return super().changelist_view(request, extra_context)

	def change_view(self, request, object_id, form_url='', extra_context=None):
		extra_context = {
			'title': 'Edit Member Salary'
		}

		return super(SalaryAdmin, self).change_view(request, object_id, form_url, extra_context)


admin.site.register(Members, MembersAdmin)
admin.site.register(Salary, SalaryAdmin)
