from django.contrib import admin
from .models import Company,Individual,InvitebyComapany,CompanyIndividualRequest,CompanyIndividualMembership,Task,TaskMembership,SearchbyCompany,ConnectionRequestbyCompany,ConnectionQueue,Supplier,SupplierAnalytics,InvitebySupplier,SupplierIndivudualRequest,SupplierIndividualMembership,SearchbySupplier,ConnectionRequestsbySupplier,ConnectionLead,Notifications,Product,Transaction,Orders


# Register your models here.
admin.site.register(Company)
admin.site.register(Individual)
admin.site.register(InvitebyComapany)
admin.site.register(CompanyIndividualRequest)
admin.site.register(CompanyIndividualMembership)
admin.site.register(Task)
admin.site.register(SearchbyCompany)
admin.site.register(ConnectionRequestbyCompany)
admin.site.register(ConnectionQueue)
admin.site.register(Supplier)
admin.site.register(SupplierAnalytics)
admin.site.register(InvitebySupplier)
admin.site.register(SupplierIndivudualRequest)
admin.site.register(SupplierIndividualMembership)
admin.site.register(SearchbySupplier)
admin.site.register(ConnectionRequestsbySupplier)
admin.site.register(ConnectionLead)
admin.site.register(Notifications)
admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(Orders)

