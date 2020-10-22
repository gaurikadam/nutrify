from django.db import models
import uuid 
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.

UNDEFINED = 'UD'


class Company(models.Model):
    class Meta:
        verbose_name_plural = _("Companies")
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING, primary_key=True)
    companyname = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    about = models.CharField(max_length=1000)
    date_of_establishment = models.DateTimeField()
    location = models.CharField(max_length=100)
    AREAS_FOCUS = [
        ('AREA1', 'AREA 1'),
        ('AREA2', 'AREA 2'),
        ('AREA3', 'AREA 3'),
        ('AREA4', 'AREA 4'),
    ]
    TYPES_OF_MARKET = [
        ('TYPE1', 'TYPE 1'),
        ('TYPE2', 'TYPE 2'),
        ('TYPE3', 'TYPE 3'),
        ('TYPE4', 'TYPE 4'),
    ]
    areas_to_focus = models.CharField(max_length=100,choices=AREAS_FOCUS,default=None)
    types_of_market_access = models.CharField(max_length=100,choices=TYPES_OF_MARKET,default=None)
    credits_assigned = models.IntegerField(default=0)
    def __str__(self):
        model_company= str(self.user)
        return model_company

class Supplier(models.Model):

    class Meta:
        verbose_name_plural = _("Suppliers")
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING, primary_key=True)
    CATEGORY_CHOICES = [
        ('CATEGORY1', 'CATEGORY 1'),
        ('CATEGORY2', 'CATEGORY 2'),
        ('CATEGORY3', 'CATEGORY 3'),
        ('CATEGORY4', 'CATEGORY 4')
    ]
    category = models.CharField(_("Category"), max_length=100,choices=CATEGORY_CHOICES, default=UNDEFINED)
    factory_certificate_image = models.ImageField(_("Factory certificate image"),upload_to ="supplier_media")
    lab_certificate_image = models.ImageField(_("Lab certificate image"),upload_to ="supplier_media")
    factory_equipments = models.CharField(_("Factory equipments"), max_length=1000)
    lab_equipments = models.CharField(_("Lab equipments"), max_length=1000)
    formats_of_dosage = models.CharField(_("Formats of dosage"), max_length=1000)
    capacity_of_each_facility = models.CharField(_("Capacity of each facility"), max_length=1000)
    f_d_services = models.CharField(_("F & D Services"), max_length=1000)
    address = models.CharField(_("Address"), max_length=1000)
    is_certified_factory = models.BooleanField(_("Is certified factory?"))
    has_certified_labs = models.BooleanField(_("Has certified labs?"))

    def __str__(self):
        model_supplier= str(self.user)
        return model_supplier

class SupplierAnalytics(models.Model):
     
    class Meta:
         verbose_name_plural = _("Supplier Analytics")
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(_("Timestamp"))
    shortlisted_count = models.IntegerField(_("Shortlisted count"))
    bookmarked_count = models.IntegerField(_("Bookmarked count"))

    def __str__(self):
        model_SearchbySupplier= str(self.supplier)
        return model_SearchbySupplier    


class Individual(models.Model):
    class Meta:
        verbose_name_plural = _("Individuals")
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING, primary_key=True)
    country = models.CharField(_("Country"), max_length=100)
    city = models.CharField(_("City"), max_length=100)
    recent_job_title = models.CharField(_("Recent Job Title"), max_length=100)
    EMPLOYEMENT_TYPE = [
        ('TYPE1', 'TYPE 1'),
        ('TYPE2', 'TYPE 2'),
        ('TYPE3', 'TYPE 3'),
        ('TYPE4', 'TYPE 4'),
    ]
    INDUSTRY = [
        ('INDUSTRY1', 'INDUSTRY 1'),
        ('INDUSTRY2', 'INDUSTRY 2'),
        ('INDUSTRY3', 'INDUSTRY 3'),
        ('INDUSTRY4', 'INDUSTRY 4'),
    ]
    employment_type = models.CharField(_("Employment Type"), max_length=100,choices=EMPLOYEMENT_TYPE, default=UNDEFINED)
    industry = models.CharField(_("Industry"), max_length=100,choices=INDUSTRY, default=UNDEFINED)
    profile_image = models.ImageField(_("Profile Image"),upload_to ="individual_profile_image")
    def __str__(self):
        model_CompanyIndividual= str(self.user)
        return model_CompanyIndividual


class InvitebyComapany(models.Model):
    class Meta:
        verbose_name_plural = _("Company Invites")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inviteFrom = models.ForeignKey(Company,on_delete=models.CASCADE)
    inviteTo= models.ForeignKey(Individual,on_delete=models.CASCADE)

    def __str__(self):
        model_invitebyCompany= '{} | {}'.format(str(self.inviteFrom),str(self.inviteTo))
        return model_invitebyCompany


class CompanyIndividualRequest(models.Model):
    class Meta:
        verbose_name_plural = _("Company Individual Requests")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inviteFrom = models.ForeignKey(Individual,on_delete=models.CASCADE)
    inviteTo= models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
            model_invitebyCompany= '{} | {}'.format(str(self.invitebyComapany),str(self.companyIndividualRequest))
            return model_invitebyCompany


class CompanyIndividualMembership(models.Model):
    class Meta:
        verbose_name_plural = _("Company Individual Memberships")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invitebyComapany = models.ForeignKey(InvitebyComapany, blank=True, null=True,on_delete=models.CASCADE)
    companyIndividualRequest = models.ForeignKey(CompanyIndividualRequest, blank=True, null=True,on_delete=models.CASCADE),

    def __str__(self):
        model_CompanyIndividualMembership = '{} | {}'.format(str(self.invitebyComapany),str(self.companyIndividualRequest))
        return model_CompanyIndividualMembership
        

class InvitebySupplier(models.Model):
     
    class Meta:
        verbose_name_plural = _("Invites by Supplier")
    inviteFrom = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    inviteTo= models.ForeignKey(Individual,on_delete=models.CASCADE)
    def __str__(self):
        model_InvitebySupplier = '{} | {}'.format(str(self.inviteFrom),str(self.inviteTo))
        return model_InvitebySupplier

class SupplierIndivudualRequest(models.Model):

    class Meta:
        verbose_name_plural = _("Supplier Indivudual Requests")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inviteFrom = models.ForeignKey(Individual,on_delete=models.CASCADE)
    inviteTo= models.ForeignKey(Supplier,on_delete=models.CASCADE)

    def __str__(self):
        model_supplierIndivudualRequest = '{} | {}'.format(str(self.inviteFrom),str(self.inviteTo))
        return model_supplierIndivudualRequest


class SupplierIndividualMembership(models.Model):

    class Meta:
        verbose_name_plural = _("Supplier Individual Memberships")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invitebySupplier = models.ForeignKey(InvitebySupplier, blank=True, null=True,on_delete=models.CASCADE)
    supplierIndivudualRequest = models.ForeignKey(SupplierIndivudualRequest, blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self):
        SupplierIndividualMembership = '{} | {}'.format(str(self.invitebySupplier),str(self.supplierIndivudualRequest))
        return SupplierIndividualMembership



class Task(models.Model):
    class Meta: 
        verbose_name_plural = _("Tasks")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=1000)
    TYPES = [
        ('TYPE1', 'TYPE 1'),
        ('TYPE2', 'TYPE 2'),
        ('TYPE3', 'TYPE 3'),
        ('TYPE4', 'TYPE 4'),
    ]
    types = models.CharField(_("Type"), max_length=100,choices=TYPES, default=UNDEFINED)
    description = models.CharField(_("Description"), max_length=1000)
    time_to_allot = models.IntegerField(_("Time to allot for this task"))
    slots_available = models.IntegerField(_("Slots available"))
    is_open = models.BooleanField(_("Is open?"))
    is_closed = models.BooleanField(_("Is closed?"))
    is_paused = models.BooleanField(_("Is paused?"))
    def __str__(self):
        model_Task = str(self.name)
        return model_Task



class TaskMembership(models.Model):
    class Meta:
        verbose_name_plural = _("Task Memberships")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    companyIndividualMembership= models.ForeignKey(CompanyIndividualMembership,on_delete=models.CASCADE)

    def __str__(self):
        model_TaskMembership = str(self.id)
        return model_TaskMembership


class SearchbyCompany(models.Model):
    class Meta:
        verbose_name_plural = _("Searches by company")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    taskMembership = models.ForeignKey(TaskMembership,on_delete=models.CASCADE)

    def __str__(self):
        model_CompanyIndividualMembership = str(self.id)
        return model_CompanyIndividualMembership


        
class ConnectionRequestbyCompany(models.Model):
    class Meta:
        verbose_name_plural = _("Connection Requests by company")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    taskMembership= models.ForeignKey(TaskMembership,on_delete=models.CASCADE)
    supplierIndividualMembership= models.ForeignKey(SupplierIndividualMembership,on_delete=models.CASCADE)
    STATUS_CHOICES = [
    ('Bookmarked', 'Bookmarked'),
    ('Shortlisted', 'Shortlisted'),
    ('Blocked', 'Blocked'),
        ]
    status = models.CharField(_("Category"), max_length=100,choices=STATUS_CHOICES, default=UNDEFINED)
    def __str__(self):
        ConnectionRequest = str(self.id)
        return ConnectionRequest
        
    
class ConnectionQueue(models.Model):

    class Meta:
        verbose_name_plural = _("Connections Queue")
    id = models.UUIDFi
    eld(primary_key=True, default=uuid.uuid4, editable=False)
    taskMembership= models.ForeignKey(TaskMembership,on_delete=models.CASCADE)
    supplierIndividualMembership= models.ForeignKey(SupplierIndividualMembership,on_delete=models.CASCADE)
    # status = 
    timeStamp = models.DateTimeField(_("timestamp"),auto_now_add=True)
    def __str__(self):
        model_supplier= str(self.id)
        return model_supplier


class SearchbySupplier(models.Model):

    class Meta:
        verbose_name_plural = _("Searches")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    supplierIndividualMembership = models.ForeignKey(SupplierIndividualMembership,on_delete=models.CASCADE)
    is_saved_search = models.BooleanField(_("Is saved search?"))
    def __str__(self):
        model_SearchbySupplier = str(self.id)
        return model_SearchbySupplier


class ConnectionRequestsbySupplier(models.Model):

    class Meta:
            verbose_name_plural = _("Connection Requests by Suppliers")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    taskMembership= models.ForeignKey(TaskMembership,on_delete=models.CASCADE)
    supplierIndividualMembership= models.ForeignKey(SupplierIndividualMembership,on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Blocked', 'Blocked'),
        ('Closed', 'Closed'),
    ]
    status = models.CharField(_("Status"), max_length=100,choices=STATUS_CHOICES, default=UNDEFINED)
    def __str__(self):
        model_SearchbySupplier = str(self.id)
        return model_SearchbySupplier
    

class ConnectionLead(models.Model):

    class Meta:
        verbose_name_plural = _("ConnectionLeads")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_membership = models.ForeignKey(TaskMembership,on_delete=models.CASCADE)
    supplierIndividualMembership = models.ForeignKey(SupplierIndividualMembership,on_delete=models.CASCADE)
    def __str__(self):
        model_Leads = str(self.id)
        return model_Leads
      

class Notifications(models.Model):
    class Meta:
        verbose_name_plural = _("Notifications")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.CharField(_("Message"),max_length=100)
    is_read = models.BooleanField(_("Is read?"))

    def __str__(self):
        model_Notifications = '{} | {}'.format(str(self.user),str(self.message))
        return model_Notifications

#payment 
class Product(models.Model):
    class Meta:
        verbose_name_plural = _("Products")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    productName = models.CharField(_("Product Name"),max_length=100)

    def __str__(self):
        model_Products = '{} | {}'.format(str(self.id),str(self.productName))
        return model_Products

class Transaction(models.Model):
    class Meta:
        verbose_name_plural = _("Transactions")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    orderId = models.CharField(_("OrderID"),max_length=14, unique=True)
    orderAmount = models.FloatField(_("OrderAmount"))
    referenceId = models.IntegerField(_("ReferenceID"),unique=True, null=True)
    transactionStatus = models.CharField(_("transactionStatus"),max_length=255)
    transactionMsg = models.CharField(_("transactionMsg"),max_length=255)
    paymentMode = models.CharField(_("payment"),max_length=255, null=True)
    signature = models.CharField(_("signature"),max_length=255)
    transactionTime = models.DateTimeField(_("transactionTime"))
   
    def __str__(self):
        model_Transaction = str(self.orderId)
        return model_Transaction

class Orders(models.Model):
    class Meta:
        verbose_name_plural = _("Orders")
    transactionDetails = models.OneToOneField(Transaction,on_delete=models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    productName = models.ForeignKey(Product,on_delete=models.CASCADE) 
    quantity = models.IntegerField(_("Quantity"),null=False)

    def __str__(self):
        model_Orders = str(self.id)
        return model_Orders