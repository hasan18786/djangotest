from django.db import models

# Member model
class Members(models.Model):
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)

	class Meta:
		verbose_name = "MemberXXX"
		verbose_name_plural = "MemberXXXs"
		app_label = "members"

	def __str__(self):
		return self.firstname + " " + self.lastname


class Salary(models.Model):
	members = models.ForeignKey(Members, blank=False, null=False, on_delete=models.CASCADE)
	amount = models.FloatField()
	salary_date = models.DateTimeField()
	company_name = models.CharField(max_length=255)
