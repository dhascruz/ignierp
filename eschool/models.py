from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.db.models import F
from django_otp.plugins.otp_totp.models import TOTPDevice


class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact = models.CharField(max_length=50)
    established_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name

        
class AccountingAccounts(models.Model):
    level = models.IntegerField(blank=True, null=True)
    type_of_account = models.PositiveIntegerField(blank=True, null=True)
    mainaccno = models.PositiveIntegerField(db_column='MainAccno', blank=True, null=True)  # Field name made lowercase.
    branchno = models.PositiveIntegerField(db_column='Branchno', blank=True, null=True)  # Field name made lowercase.
    order = models.PositiveIntegerField(db_column='Order', blank=True, null=True)  # Field name made lowercase.
    accno = models.CharField(db_column='AccNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accname_ar = models.CharField(db_column='AccName_ar', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accname_en = models.CharField(db_column='AccName_en', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parentno = models.PositiveIntegerField(db_column='ParentNo', blank=True, null=True)  # Field name made lowercase.
    selling_price = models.PositiveIntegerField(db_column='Selling_price', blank=True, null=True)  # Field name made lowercase.
    creditlimit = models.FloatField(db_column='CreditLimit', blank=True, null=True)  # Field name made lowercase.
    acctype = models.PositiveSmallIntegerField(db_column='AccType', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=25, blank=True, null=True)  # Field name made lowercase.
    acclevel = models.BigIntegerField(db_column='AccLevel', blank=True, null=True)  # Field name made lowercase.
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    contact_position = models.CharField(max_length=255, blank=True, null=True)
    iban = models.CharField(max_length=255, blank=True, null=True)
    bank = models.PositiveIntegerField(blank=True, null=True)
    openbalance = models.FloatField(db_column='OpenBalance', blank=True, null=True)  # Field name made lowercase.
    credit = models.FloatField(db_column='Credit', blank=True, null=True)  # Field name made lowercase.
    debit = models.FloatField(db_column='Debit', blank=True, null=True)  # Field name made lowercase.
    opendate = models.DateTimeField(db_column='OpenDate', blank=True, null=True)  # Field name made lowercase.
    lastacctransdate = models.DateTimeField(db_column='LastAccTransDate', blank=True, null=True)  # Field name made lowercase.
    laststocktransdate = models.DateTimeField(db_column='LastStockTransDate', blank=True, null=True)  # Field name made lowercase.
    accnature = models.SmallIntegerField(db_column='AccNature', blank=True, null=True)  # Field name made lowercase.
    accclassifying = models.SmallIntegerField(db_column='Accclassifying', blank=True, null=True)  # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    salesdiscount = models.SmallIntegerField(db_column='SalesDiscount', blank=True, null=True)  # Field name made lowercase.
    sellingpricecat = models.SmallIntegerField(db_column='SellingPriceCat', blank=True, null=True)  # Field name made lowercase.
    isdetailaccount = models.SmallIntegerField(db_column='isDetailAccount', blank=True, null=True)  # Field name made lowercase.
    respperson = models.CharField(db_column='RespPerson', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invoicesdueperiod = models.BigIntegerField(db_column='InvoicesDuePeriod', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createduserno = models.IntegerField(db_column='CreatedUserno', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='Createddate', blank=True, null=True)  # Field name made lowercase.
    parentmainaccno = models.BigIntegerField(db_column='ParentMainAccno', blank=True, null=True)  # Field name made lowercase.
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounting_accounts'


class AccountingAccountsTrans(models.Model):
    transid = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    isfromvoucher = models.IntegerField(db_column='isFromVoucher')  # Field name made lowercase.
    qr_code = models.CharField(max_length=255, blank=True, null=True)
    payment_id = models.IntegerField(blank=True, null=True)
    student = models.IntegerField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    academicyear = models.IntegerField(blank=True, null=True)
    trans_type = models.IntegerField(blank=True, null=True)
    branchno = models.PositiveIntegerField(blank=True, null=True)
    transno = models.PositiveIntegerField(blank=True, null=True)
    transyear = models.TextField(db_column='transYear', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    branchsubno = models.PositiveIntegerField(db_column='BranchSubno', blank=True, null=True)  # Field name made lowercase.
    gregorian_date = models.DateField(db_column='Gregorian_date', blank=True, null=True)  # Field name made lowercase.
    hijri_date = models.CharField(db_column='Hijri_date', max_length=50, blank=True, null=True)  # Field name made lowercase.
    document_number = models.PositiveIntegerField(db_column='Document_Number', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(blank=True, null=True)
    total_discount = models.FloatField(blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    posted = models.PositiveIntegerField(db_column='Posted')  # Field name made lowercase.
    reversedno = models.PositiveIntegerField(db_column='Reversedno', blank=True, null=True)  # Field name made lowercase.
    reversedyear = models.CharField(db_column='ReversedYear', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reversedbranch = models.CharField(db_column='ReversedBranch', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transtype = models.PositiveSmallIntegerField(db_column='transType', blank=True, null=True)  # Field name made lowercase.
    linked_with = models.PositiveIntegerField(db_column='Linked_with', blank=True, null=True)  # Field name made lowercase.
    reversed_by = models.PositiveIntegerField(db_column='Reversed_By', blank=True, null=True)  # Field name made lowercase.
    reversed_date = models.DateTimeField(db_column='Reversed_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_modify_date = models.DateTimeField(db_column='Last_Modify_date', blank=True, null=True)  # Field name made lowercase.
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    post_by = models.PositiveIntegerField(db_column='Post_By', blank=True, null=True)  # Field name made lowercase.
    postdate = models.DateTimeField(db_column='PostDate', blank=True, null=True)  # Field name made lowercase.
    costcenterno = models.PositiveIntegerField(db_column='CostCenterno', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounting_accounts_trans'


class AccountingAccountsTransdetail(models.Model):
    student = models.IntegerField(blank=True, null=True)
    payment_id = models.IntegerField(blank=True, null=True)
    academicyear = models.IntegerField(blank=True, null=True)
    term = models.IntegerField(blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    fee_type = models.IntegerField(blank=True, null=True)
    bus_fee = models.IntegerField(blank=True, null=True)
    recno = models.PositiveIntegerField(db_column='Recno', blank=True, null=True)  # Field name made lowercase.
    branchno = models.PositiveIntegerField(db_column='Branchno', blank=True, null=True)  # Field name made lowercase.
    transyear = models.PositiveIntegerField(db_column='transYear', blank=True, null=True)  # Field name made lowercase.
    accyear = models.PositiveIntegerField(db_column='AccYear', blank=True, null=True)  # Field name made lowercase.
    posted = models.PositiveIntegerField(blank=True, null=True)
    transno = models.PositiveIntegerField(db_column='TransNo', blank=True, null=True)  # Field name made lowercase.
    accno = models.PositiveIntegerField(db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    debit = models.FloatField(blank=True, null=True)
    credit = models.FloatField(blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    predebitbal = models.FloatField(db_column='PreDebitBal', blank=True, null=True)  # Field name made lowercase.
    precreditbal = models.FloatField(db_column='PreCreditBal', blank=True, null=True)  # Field name made lowercase.
    costcenterno = models.PositiveIntegerField(db_column='CostCenterno', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounting_accounts_transdetail'


class AccountingEmployeesSalary(models.Model):
    trans_id = models.PositiveIntegerField(blank=True, null=True)
    employee = models.PositiveIntegerField(blank=True, null=True)
    basic_salary = models.PositiveIntegerField(blank=True, null=True)
    net_salary = models.PositiveIntegerField(blank=True, null=True)
    discounts = models.PositiveIntegerField(blank=True, null=True)
    allowances = models.PositiveIntegerField(blank=True, null=True)
    deductions = models.PositiveIntegerField(blank=True, null=True)
    rewards = models.PositiveIntegerField(blank=True, null=True)
    dboda = models.PositiveIntegerField(db_column='DBODA', blank=True, null=True)  # Field name made lowercase.
    month = models.PositiveIntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounting_employees_salary'


class AccountingLinks(models.Model):
    account_id = models.PositiveIntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=250, blank=True, null=True)
    name_en = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounting_links'


class AccountingPayments(models.Model):
    id = models.BigAutoField(primary_key=True)
    op_date = models.DateField(blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    creditor = models.IntegerField(blank=True, null=True)
    user = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    discount = models.PositiveIntegerField(db_column='Discount', blank=True, null=True)  # Field name made lowercase.
    discount_percent = models.IntegerField(blank=True, null=True)
    discount_amount = models.IntegerField(blank=True, null=True)
    cash = models.IntegerField(db_column='Cash', blank=True, null=True)  # Field name made lowercase.
    bank_transfer = models.IntegerField(db_column='Bank_Transfer', blank=True, null=True)  # Field name made lowercase.
    atm = models.IntegerField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    cheque = models.IntegerField(db_column='Cheque', blank=True, null=True)  # Field name made lowercase.
    check_bank = models.CharField(max_length=255, blank=True, null=True)
    check_number = models.CharField(max_length=255, blank=True, null=True)
    check_maturity_date = models.DateField(blank=True, null=True)
    bank_transfer_name = models.IntegerField(db_column='Bank_Transfer_name', blank=True, null=True)  # Field name made lowercase.
    bank_transfer_number = models.TextField(db_column='Bank_Transfer_number', db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    bank_transfer_maturity_date = models.DateField(db_column='Bank_Transfer_maturity_date', blank=True, null=True)  # Field name made lowercase.
    bank_transfer_note = models.TextField(db_column='Bank_Transfer_note', db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    debt = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    accepted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounting_payments'


class AccountingReceiptVoucher(models.Model):
    description = models.TextField(blank=True, null=True)
    contact = models.PositiveIntegerField(blank=True, null=True)
    debit_id = models.IntegerField(blank=True, null=True)
    cash = models.IntegerField(db_column='Cash', blank=True, null=True)  # Field name made lowercase.
    bank_transfer = models.IntegerField(db_column='Bank_Transfer', blank=True, null=True)  # Field name made lowercase.
    point_of_sales = models.IntegerField(blank=True, null=True)
    cheque = models.IntegerField(db_column='Cheque', blank=True, null=True)  # Field name made lowercase.
    check_bank = models.TextField(blank=True, null=True)
    check_number = models.TextField(blank=True, null=True)
    check_maturity_date = models.TextField(blank=True, null=True)
    bank_transfer_name = models.TextField(db_column='Bank_Transfer_name', blank=True, null=True)  # Field name made lowercase.
    bank_transfer_number = models.TextField(db_column='Bank_Transfer_number', blank=True, null=True)  # Field name made lowercase.
    bank_transfer_maturity_date = models.TextField(db_column='Bank_Transfer_maturity_date', blank=True, null=True)  # Field name made lowercase.
    bank_transfer_note = models.TextField(db_column='Bank_Transfer_note', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='Created_By', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.IntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    reference_id = models.TextField(db_column='reference_ID', blank=True, null=True)  # Field name made lowercase.
    reference_type = models.IntegerField(blank=True, null=True)
    employee_name = models.TextField(blank=True, null=True)
    donor = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounting_receipt_voucher'


class AccountingReceiptVoucherTrans(models.Model):
    voucher_id = models.IntegerField(blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)
    accno = models.IntegerField(db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    costcenterno = models.IntegerField(db_column='CostCenterno', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounting_receipt_voucher_trans'


class AccountingReceivable(models.Model):
    id = models.BigAutoField(primary_key=True)
    mainaccno = models.BigIntegerField(db_column='MainAccno', blank=True, null=True)  # Field name made lowercase.
    branchno = models.BigIntegerField(db_column='Branchno', blank=True, null=True)  # Field name made lowercase.
    order = models.IntegerField(db_column='Order', blank=True, null=True)  # Field name made lowercase.
    accno = models.CharField(db_column='AccNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accname_ar = models.CharField(db_column='AccName_ar', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accname_en = models.CharField(db_column='AccName_en', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parentno = models.BigIntegerField(db_column='ParentNo', blank=True, null=True)  # Field name made lowercase.
    selling_price = models.IntegerField(db_column='Selling_price', blank=True, null=True)  # Field name made lowercase.
    creditlimit = models.FloatField(db_column='CreditLimit', blank=True, null=True)  # Field name made lowercase.
    acctype = models.SmallIntegerField(db_column='AccType', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=25, blank=True, null=True)  # Field name made lowercase.
    acclevel = models.BigIntegerField(db_column='AccLevel', blank=True, null=True)  # Field name made lowercase.
    openbalance = models.FloatField(db_column='OpenBalance', blank=True, null=True)  # Field name made lowercase.
    credit = models.FloatField(db_column='Credit', blank=True, null=True)  # Field name made lowercase.
    debit = models.FloatField(db_column='Debit', blank=True, null=True)  # Field name made lowercase.
    opendate = models.DateTimeField(db_column='OpenDate', blank=True, null=True)  # Field name made lowercase.
    lastacctransdate = models.DateTimeField(db_column='LastAccTransDate', blank=True, null=True)  # Field name made lowercase.
    laststocktransdate = models.DateTimeField(db_column='LastStockTransDate', blank=True, null=True)  # Field name made lowercase.
    accnature = models.SmallIntegerField(db_column='AccNature', blank=True, null=True)  # Field name made lowercase.
    accclassifying = models.SmallIntegerField(db_column='Accclassifying', blank=True, null=True)  # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    salesdiscount = models.SmallIntegerField(db_column='SalesDiscount', blank=True, null=True)  # Field name made lowercase.
    sellingpricecat = models.SmallIntegerField(db_column='SellingPriceCat', blank=True, null=True)  # Field name made lowercase.
    isdetailaccount = models.SmallIntegerField(db_column='isDetailAccount', blank=True, null=True)  # Field name made lowercase.
    respperson = models.CharField(db_column='RespPerson', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invoicesdueperiod = models.BigIntegerField(db_column='InvoicesDuePeriod', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createduserno = models.IntegerField(db_column='CreatedUserno', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='Createddate', blank=True, null=True)  # Field name made lowercase.
    parentmainaccno = models.BigIntegerField(db_column='ParentMainAccno', blank=True, null=True)  # Field name made lowercase.
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounting_receivable'


class Announcements(models.Model):
    stick = models.PositiveIntegerField(blank=True, null=True)
    view = models.PositiveBigIntegerField(blank=True, null=True)
    categorie = models.BigIntegerField(blank=True, null=True)
    field = models.BigIntegerField(blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    img_thumb = models.CharField(max_length=255, blank=True, null=True)
    title_ar = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    desc_ar = models.CharField(max_length=255, blank=True, null=True)
    desc_en = models.CharField(max_length=255, blank=True, null=True)
    other_details_ar = models.TextField(blank=True, null=True)
    other_details_en = models.TextField(blank=True, null=True)
    created_by = models.IntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.IntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'announcements'


class AssetsAttachments(models.Model):
    asset_id = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    file_path = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_attachments'


class AssetsCompanies(models.Model):
    asset_id = models.PositiveIntegerField(blank=True, null=True)
    manufacture_name = models.CharField(max_length=255, blank=True, null=True)
    manufacture_address = models.CharField(max_length=255, blank=True, null=True)
    supplier_name = models.CharField(max_length=255, blank=True, null=True)
    supplier_address = models.CharField(max_length=255, blank=True, null=True)
    phone1 = models.CharField(max_length=50, blank=True, null=True)
    phone2 = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=127, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    guarantee_no = models.CharField(max_length=50, blank=True, null=True)
    guarantee_start_date = models.DateField(blank=True, null=True)
    guarantee_end_date = models.DateField(blank=True, null=True)
    received_date = models.DateField(blank=True, null=True)
    received_notes = models.CharField(max_length=500, blank=True, null=True)
    production_date = models.DateField(blank=True, null=True)
    contract_number = models.CharField(max_length=255, blank=True, null=True)
    contract_date = models.DateField(blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    customs_declaration = models.CharField(max_length=255, blank=True, null=True)
    customs_declaration_date = models.DateField(blank=True, null=True)
    shipping_no = models.CharField(max_length=255, blank=True, null=True)
    shipping_way = models.CharField(max_length=255, blank=True, null=True)
    shipping_date = models.DateField(blank=True, null=True)
    import_license_no = models.CharField(max_length=255, blank=True, null=True)
    arrival_area = models.CharField(max_length=255, blank=True, null=True)
    arrival_date = models.DateField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_companies'


class AssetsDepreciations(models.Model):
    asset_id = models.PositiveIntegerField(blank=True, null=True)
    depreciation_type = models.PositiveIntegerField(blank=True, null=True)
    not_subject_to_revaluation = models.PositiveIntegerField(blank=True, null=True)
    not_subject_to_depreciation = models.PositiveIntegerField(blank=True, null=True)
    life_span = models.PositiveIntegerField(blank=True, null=True)
    life_span_unit = models.PositiveIntegerField(blank=True, null=True)
    currency = models.PositiveIntegerField(blank=True, null=True)
    salvage_value = models.PositiveIntegerField(blank=True, null=True)
    starting_value = models.PositiveIntegerField(blank=True, null=True)
    addition_value = models.PositiveIntegerField(blank=True, null=True)
    exclusion_value = models.PositiveIntegerField(blank=True, null=True)
    accumulated_depreciation = models.PositiveIntegerField(blank=True, null=True)
    current_asset_value = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_depreciations'


class AssetsGroups(models.Model):
    is_group = models.PositiveIntegerField(blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    item_no = models.CharField(max_length=255, blank=True, null=True)
    parent_no = models.IntegerField(blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    item_type = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)
    item_acc = models.IntegerField(blank=True, null=True)
    depreciation_acc = models.IntegerField(blank=True, null=True)
    accumulated_depreciation_acc = models.IntegerField(blank=True, null=True)
    expenses_acc = models.IntegerField(blank=True, null=True)
    capital_gain_acc = models.IntegerField(blank=True, null=True)
    capital_loss_acc = models.IntegerField(blank=True, null=True)
    revaluation_surplus_acc = models.IntegerField(blank=True, null=True)
    revaluation_deficiency_acc = models.IntegerField(blank=True, null=True)
    feature1 = models.CharField(max_length=255, blank=True, null=True)
    feature2 = models.CharField(max_length=255, blank=True, null=True)
    feature3 = models.CharField(max_length=255, blank=True, null=True)
    feature4 = models.CharField(max_length=255, blank=True, null=True)
    feature5 = models.CharField(max_length=255, blank=True, null=True)
    feature6 = models.CharField(max_length=255, blank=True, null=True)
    feature7 = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_groups'


class AssetsMaintenances(models.Model):
    asset_id = models.PositiveIntegerField(blank=True, null=True)
    contract_no = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_maintenances'


class AssetsTrans(models.Model):
    type_id = models.PositiveIntegerField(blank=True, null=True)
    account_id = models.PositiveIntegerField(blank=True, null=True)
    trans_date = models.DateField(blank=True, null=True)
    currency = models.PositiveIntegerField(blank=True, null=True)
    currency_price = models.FloatField(blank=True, null=True)
    cost_center = models.CharField(max_length=255, blank=True, null=True)
    seller = models.CharField(max_length=500, blank=True, null=True)
    department = models.PositiveIntegerField(blank=True, null=True)
    distributor = models.CharField(max_length=255, blank=True, null=True)
    details = models.CharField(max_length=500, blank=True, null=True)
    has_restriction = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_trans'


class AssetsTransDetails(models.Model):
    trans_id = models.PositiveIntegerField(blank=True, null=True)
    asset_id = models.PositiveIntegerField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    seller = models.CharField(max_length=255, blank=True, null=True)
    cost_center = models.CharField(max_length=255, blank=True, null=True)
    distributor = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)
    additions = models.FloatField(blank=True, null=True)
    exclusions = models.FloatField(blank=True, null=True)
    depreciations = models.FloatField(blank=True, null=True)
    current_department = models.PositiveIntegerField(blank=True, null=True)
    new_department = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_trans_details'


class AssetsTransTypes(models.Model):
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    details = models.CharField(max_length=500, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_trans_types'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent = models.IntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class CommunityService(models.Model):
    hr_id = models.IntegerField(db_column='HR_id', blank=True, null=True)  # Field name made lowercase.
    student_id = models.IntegerField(db_column='Student_id', blank=True, null=True)  # Field name made lowercase.
    first_name_ar = models.CharField(max_length=30, blank=True, null=True)
    first_name_en = models.CharField(max_length=30, blank=True, null=True)
    father_name_ar = models.CharField(max_length=30, blank=True, null=True)
    father_name_en = models.CharField(max_length=30, blank=True, null=True)
    grand_father_name_ar = models.CharField(max_length=30, blank=True, null=True)
    grand_father_name_en = models.CharField(max_length=30, blank=True, null=True)
    last_name_ar = models.CharField(max_length=30, blank=True, null=True)
    last_name_en = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=75, blank=True, null=True)
    jobtitle = models.CharField(max_length=30, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    course = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_updated_date = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    deleted_date = models.DateField(blank=True, null=True)
    accepted_by = models.IntegerField(blank=True, null=True)
    accepted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'community_service'


class CommunityServiceCourse(models.Model):
    name_ar = models.CharField(max_length=30)
    name_en = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.CharField(max_length=30, blank=True, null=True)
    end_date = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=180, blank=True, null=True)
    created_by = models.IntegerField()
    created_date = models.DateTimeField()
    last_update_date = models.DateTimeField(blank=True, null=True)
    last_update_by = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'community_service_course'


class Contact(models.Model):
    readed = models.PositiveIntegerField()
    sended_to_admin_main = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    admin_reply_status = models.PositiveIntegerField()
    admin_reply = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact'


class ContractsApprovals(models.Model):
    order = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    contract_id = models.PositiveIntegerField(blank=True, null=True)
    department = models.PositiveIntegerField(blank=True, null=True)
    replied_date = models.DateTimeField(blank=True, null=True)
    replied_by = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contracts_approvals'


class Counters(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    data_append = models.CharField(max_length=255, blank=True, null=True)
    start_from = models.IntegerField(blank=True, null=True)
    end_with = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'counters'


class DashboardFollows(models.Model):
    user_id = models.PositiveIntegerField()
    type = models.CharField(max_length=255)
    par1 = models.PositiveIntegerField(blank=True, null=True)
    par2 = models.PositiveIntegerField(blank=True, null=True)
    par3 = models.PositiveIntegerField(blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    to_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_follows'


class Dictionary(models.Model):
    token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    txt_ar = models.TextField(blank=True, null=True)
    txt_en = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dictionary'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocumentManagementSystems(models.Model):
    account_type = models.PositiveIntegerField(blank=True, null=True)
    account_type_id = models.PositiveIntegerField(blank=True, null=True)
    contact = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    file_path = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_management_systems'


class DocumentsApprovals(models.Model):
    college = models.IntegerField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    program = models.PositiveIntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=255, blank=True, null=True)
    hr_position = models.IntegerField(blank=True, null=True)
    employee = models.IntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    show_signature = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_approvals'


class Events(models.Model):
    teacher = models.IntegerField(blank=True, null=True)
    is_public = models.IntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    img_path = models.CharField(max_length=255, blank=True, null=True)
    banner_path = models.CharField(max_length=255, blank=True, null=True)
    event_path = models.CharField(max_length=255, blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    points_of_speak = models.CharField(max_length=500, blank=True, null=True)
    sponsers = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    price_before_discount = models.FloatField()
    currency = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    estimated_seats = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    map = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class FinancialsAddedTaxes(models.Model):
    academicyear = models.IntegerField(blank=True, null=True)
    term = models.IntegerField(blank=True, null=True)
    fee_type = models.IntegerField(blank=True, null=True)
    college = models.PositiveIntegerField(blank=True, null=True)
    program = models.PositiveIntegerField(blank=True, null=True)
    major = models.PositiveIntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    citizen = models.PositiveIntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    ratio = models.FloatField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_added_taxes'


class FinancialsAdditionalFees(models.Model):
    fee_type = models.PositiveIntegerField(blank=True, null=True)
    fee_plan = models.PositiveIntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    is_mandatory = models.PositiveIntegerField(blank=True, null=True)
    has_added_tax = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_additional_fees'


class FinancialsBusFees(models.Model):
    user_type = models.IntegerField()
    academic_year = models.PositiveIntegerField(blank=True, null=True)
    college = models.PositiveIntegerField(blank=True, null=True)
    student_type = models.PositiveIntegerField(blank=True, null=True)
    bus_path = models.CharField(max_length=255)
    go_month = models.FloatField(blank=True, null=True)
    return_month = models.FloatField(blank=True, null=True)
    go_return_month = models.FloatField(blank=True, null=True)
    go_first = models.FloatField(blank=True, null=True)
    return_first = models.FloatField(blank=True, null=True)
    go_return_first = models.FloatField(blank=True, null=True)
    go_second = models.FloatField(blank=True, null=True)
    return_second = models.FloatField(blank=True, null=True)
    go_return_second = models.FloatField(blank=True, null=True)
    go_third = models.FloatField(blank=True, null=True)
    return_third = models.FloatField(blank=True, null=True)
    go_return_third = models.FloatField(blank=True, null=True)
    go_fourth = models.FloatField(blank=True, null=True)
    return_fourth = models.FloatField(blank=True, null=True)
    go_return_fourth = models.FloatField(blank=True, null=True)
    go_year = models.FloatField(blank=True, null=True)
    return_year = models.FloatField(blank=True, null=True)
    go_return_year = models.FloatField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_bus_fees'


class FinancialsBusStudents(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_type = models.IntegerField()
    contract_id = models.IntegerField(blank=True, null=True)
    student = models.PositiveIntegerField(blank=True, null=True)
    academic_year = models.PositiveIntegerField(blank=True, null=True)
    fee_id = models.PositiveIntegerField(blank=True, null=True)
    plan_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    from_field = models.DateField(db_column='from', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.DateField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    discount_ratio = models.FloatField()
    paid_amount = models.FloatField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_bus_students'


class FinancialsCostcenter(models.Model):
    name_ar = models.CharField(max_length=50, blank=True, null=True)
    name_en = models.CharField(max_length=50, blank=True, null=True)
    parentno = models.IntegerField(db_column='ParentNo', blank=True, null=True)  # Field name made lowercase.
    cost_number = models.CharField(max_length=50, blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_costcenter'


class FinancialsCoursesFees(models.Model):
    parent = models.IntegerField(blank=True, null=True)
    academicyear = models.IntegerField(blank=True, null=True)
    term = models.IntegerField(blank=True, null=True)
    student_type = models.PositiveIntegerField(blank=True, null=True)
    has_added_tax = models.IntegerField(blank=True, null=True)
    level = models.PositiveIntegerField(blank=True, null=True)
    level_price = models.FloatField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    major = models.PositiveIntegerField(blank=True, null=True)
    program = models.PositiveIntegerField(blank=True, null=True)
    college = models.PositiveIntegerField(blank=True, null=True)
    course = models.PositiveIntegerField(blank=True, null=True)
    course_price = models.IntegerField(blank=True, null=True)
    department = models.PositiveIntegerField(blank=True, null=True)
    degree = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_courses_fees'


class FinancialsDiscountStudents(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    fee_type = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    student = models.PositiveIntegerField(blank=True, null=True)
    academicyear = models.IntegerField(blank=True, null=True)
    term = models.PositiveIntegerField(blank=True, null=True)
    percent = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_discount_students'


class FinancialsDiscounts(models.Model):
    student_type = models.PositiveIntegerField(blank=True, null=True)
    discount_type = models.IntegerField()
    fee_type = models.IntegerField()
    main_account_id = models.IntegerField(blank=True, null=True)
    two_sons = models.FloatField(blank=True, null=True)
    three_sons = models.FloatField(blank=True, null=True)
    four_sons = models.FloatField(blank=True, null=True)
    five_sons = models.FloatField(blank=True, null=True)
    academicyear = models.PositiveIntegerField(blank=True, null=True)
    field_term = models.IntegerField(db_column=' term', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    description = models.CharField(max_length=255, blank=True, null=True)
    college = models.IntegerField(blank=True, null=True)
    major = models.PositiveIntegerField(blank=True, null=True)
    program = models.IntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    must_pay = models.FloatField(blank=True, null=True)
    discount_percent = models.FloatField(blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    degree = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_discounts'


class FinancialsFeesTypes(models.Model):
    main_account_id = models.IntegerField(blank=True, null=True)
    cach_account_id = models.IntegerField(blank=True, null=True)
    bank_remittances_id = models.IntegerField(blank=True, null=True)
    sale_point_id = models.IntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    desc_ar = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_fees_types'


class FinancialsFinesManagement(models.Model):
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    academicyear = models.IntegerField(blank=True, null=True)
    term = models.PositiveIntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    fine_type = models.PositiveIntegerField(blank=True, null=True)
    fine_amount = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_fines_management'


class FinancialsGetoutFees(models.Model):
    student = models.IntegerField(blank=True, null=True)
    college = models.PositiveIntegerField(blank=True, null=True)
    major = models.PositiveIntegerField(blank=True, null=True)
    program = models.PositiveIntegerField(blank=True, null=True)
    plan = models.PositiveIntegerField(blank=True, null=True)
    from_day = models.PositiveIntegerField(blank=True, null=True)
    to_day = models.PositiveIntegerField(blank=True, null=True)
    from_month = models.PositiveIntegerField(blank=True, null=True)
    to_month = models.PositiveIntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    ratio = models.FloatField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_getout_fees'


class FinancialsInstallments(models.Model):
    academicyear = models.PositiveIntegerField(blank=True, null=True)
    student_type = models.PositiveIntegerField(blank=True, null=True)
    main_account_id = models.IntegerField(blank=True, null=True)
    college = models.IntegerField(blank=True, null=True)
    major = models.PositiveIntegerField(blank=True, null=True)
    program = models.IntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    student = models.IntegerField(blank=True, null=True)
    in_study_fees = models.IntegerField()
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_installments'


class FinancialsInstallmentsItems(models.Model):
    installment = models.PositiveIntegerField(blank=True, null=True)
    term = models.IntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    month = models.PositiveIntegerField()
    percent = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_installments_items'


class FinancialsMandatoryMinPayment(models.Model):
    academicyear = models.IntegerField(blank=True, null=True)
    term = models.IntegerField(blank=True, null=True)
    college = models.IntegerField(blank=True, null=True)
    major = models.PositiveIntegerField(blank=True, null=True)
    program = models.PositiveIntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    degree = models.PositiveIntegerField(blank=True, null=True)
    mandatory_percent = models.FloatField(blank=True, null=True)
    due_period_days = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_mandatory_min_payment'


class FinancialsMandatoryMinPaymentCustom(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    academicyear = models.IntegerField(blank=True, null=True)
    student = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveIntegerField(blank=True, null=True)
    mandatory_percent = models.FloatField(blank=True, null=True)
    due_period_days = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_mandatory_min_payment_custom'


class FinancialsPaymentDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    payment = models.PositiveIntegerField(blank=True, null=True)
    payment_method = models.PositiveIntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    bank = models.IntegerField(blank=True, null=True)
    check_number = models.CharField(max_length=255, blank=True, null=True)
    transfer_date = models.DateTimeField(blank=True, null=True)
    reference_no = models.CharField(max_length=255, blank=True, null=True)
    name_of_transferor = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_payment_details'


class FinancialsPayments(models.Model):
    id = models.BigAutoField(primary_key=True)
    op_number = models.CharField(max_length=50, blank=True, null=True)
    op_type = models.IntegerField(blank=True, null=True)
    fee_type = models.IntegerField()
    parent = models.IntegerField(blank=True, null=True)
    student = models.PositiveIntegerField(blank=True, null=True)
    academicyear = models.IntegerField(blank=True, null=True)
    term = models.PositiveIntegerField(blank=True, null=True)
    discount = models.PositiveIntegerField(db_column='Discount', blank=True, null=True)  # Field name made lowercase.
    discount_percent = models.FloatField(blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    cash = models.FloatField(db_column='Cash', blank=True, null=True)  # Field name made lowercase.
    bank_transfer = models.FloatField(db_column='Bank_Transfer', blank=True, null=True)  # Field name made lowercase.
    atm = models.FloatField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    cheque = models.FloatField(db_column='Cheque', blank=True, null=True)  # Field name made lowercase.
    credit_card = models.FloatField(blank=True, null=True)
    card_type = models.CharField(max_length=255, blank=True, null=True)
    check_bank = models.CharField(max_length=255, blank=True, null=True)
    check_number = models.CharField(max_length=255, blank=True, null=True)
    check_maturity_date = models.DateField(blank=True, null=True)
    transfer_date = models.DateTimeField(blank=True, null=True)
    reference_of_transfare = models.CharField(max_length=255, blank=True, null=True)
    name_of_transferor = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_payments'


class FinancialsSponsors(models.Model):
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    legalform = models.PositiveIntegerField(blank=True, null=True)
    tel_number = models.CharField(max_length=255, blank=True, null=True)
    coordinator = models.CharField(max_length=255, blank=True, null=True)
    head_office = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    sponsor_type = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_sponsors'


class FinancialsSponsorsTypes(models.Model):
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_sponsors_types'


class FinancialsSponsorships(models.Model):
    notes = models.CharField(max_length=255, blank=True, null=True)
    student = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveIntegerField(blank=True, null=True)
    sponsor = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financials_sponsorships'


class GeneralAcademicStatuses(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_academic_statuses'


class GeneralBanks(models.Model):
    account_id = models.IntegerField(blank=True, null=True)
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_banks'


class GeneralCities(models.Model):
    is_active = models.PositiveIntegerField()
    country_id = models.PositiveIntegerField(blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    lng = models.CharField(max_length=255, blank=True, null=True)
    geonameid = models.CharField(db_column='geonameId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_cities'


class GeneralContactPerson(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    details = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=150, blank=True, null=True)
    fax = models.CharField(max_length=150, blank=True, null=True)
    cel_phone = models.CharField(max_length=150, blank=True, null=True)
    s_b = models.CharField(db_column='S_B', max_length=150, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    last_update_by = models.IntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_contact_person'


class GeneralContactPersonMessage(models.Model):
    speach_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact_person = models.IntegerField(blank=True, null=True)
    upload_path = models.TextField(blank=True, null=True)
    attachment = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    accept_number = models.IntegerField(blank=True, null=True)
    important = models.IntegerField(blank=True, null=True)
    archive_url = models.TextField(blank=True, null=True)
    manual_archive = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    spical_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_contact_person_message'


class GeneralCountries(models.Model):
    is_active = models.PositiveIntegerField()
    gcc = models.PositiveIntegerField(db_column='GCC', blank=True, null=True)  # Field name made lowercase.
    continent = models.CharField(max_length=50, blank=True, null=True)
    capital = models.CharField(max_length=255, blank=True, null=True)
    languages = models.CharField(max_length=255, blank=True, null=True)
    geonameid = models.CharField(db_column='geonameId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    areainsqkm = models.CharField(db_column='areaInSqKm', max_length=255, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='countryCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.CharField(db_column='currencyCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_countries'


class GeneralCurrencies(models.Model):
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    currency_code = models.CharField(max_length=255, blank=True, null=True)
    price_in_usd = models.FloatField(db_column='price_in_USD', blank=True, null=True)  # Field name made lowercase.
    price_in_sar = models.FloatField(db_column='price_in_SAR', blank=True, null=True)  # Field name made lowercase.
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_currencies'


class GeneralEducationLevels(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_education_levels'


class GeneralElearningInfractions(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_elearning_infractions'


class GeneralElearningParticipates(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_elearning_participates'


class GeneralElearningPermissions(models.Model):
    is_active = models.IntegerField()
    name_ar = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    desc_ar = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_elearning_permissions'


class GeneralFields(models.Model):
    gennerally_id = models.PositiveIntegerField(blank=True, null=True)
    col_name = models.CharField(max_length=255, blank=True, null=True)
    col_md = models.IntegerField(blank=True, null=True)
    col_type = models.CharField(max_length=255, blank=True, null=True)
    options_orm = models.CharField(max_length=255, blank=True, null=True)
    col_required = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_fields'


class GeneralGenders(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_genders'


class GeneralGenerally(models.Model):
    section = models.PositiveIntegerField(blank=True, null=True)
    parent = models.PositiveIntegerField(blank=True, null=True)
    parent_col_name = models.CharField(max_length=255, blank=True, null=True)
    model_name = models.CharField(max_length=255, blank=True, null=True)
    add_rule = models.CharField(max_length=255, blank=True, null=True)
    browse_rule = models.CharField(max_length=255, blank=True, null=True)
    edit_rule = models.CharField(max_length=255, blank=True, null=True)
    delete_rule = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_generally'


class GeneralHrDepartments(models.Model):
    university = models.IntegerField(blank=True, null=True)
    college = models.IntegerField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    director = models.PositiveIntegerField(blank=True, null=True)
    deputy_director = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_hr_departments'


class GeneralHrEmployeeTypes(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    vacations_balance = models.IntegerField(blank=True, null=True)
    is_teacher = models.IntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_hr_employee_types'


class GeneralHrFinesTypes(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    percentage = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_hr_fines_types'


class GeneralHrLeavetypes(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_hr_leavetypes'


class GeneralHrPositions(models.Model):
    is_active = models.PositiveIntegerField()
    department = models.PositiveIntegerField(blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    job_requirements = models.TextField(blank=True, null=True)
    send_messages = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    send_to_same_department = models.IntegerField()
    required_members = models.IntegerField(blank=True, null=True)
    opened_for_admission = models.IntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_hr_positions'


class GeneralHrRewardsTypes(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_hr_rewards_types'


class GeneralHrSections(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_hr_sections'


class GeneralHrStatuses(models.Model):
    is_active = models.PositiveIntegerField()
    can_login = models.IntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_hr_statuses'


class GeneralHrWarningsTypes(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_hr_warnings_types'


class GeneralHsCertificateType(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_hs_certificate_type'


class GeneralLegalforms(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_legalforms'


class GeneralMajors(models.Model):
    is_active = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_majors'


class GeneralMaritalStatus(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_marital_status'


class GeneralReligions(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_religions'


class GeneralScientificDegrees(models.Model):
    is_active = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_scientific_degrees'


class GeneralStoresCategories(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_stores_categories'


class GeneralStoresStores(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_stores_stores'


class GeneralStoresUnits(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    fraction = models.CharField(max_length=255, blank=True, null=True)
    fraction_of_orginal = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_stores_units'


class GeneralStudentParentRelation(models.Model):
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_student_parent_relation'


class HomeIcons(models.Model):
    id = models.BigAutoField(primary_key=True)
    show_for_visitors = models.PositiveIntegerField(db_column='Show_for_Visitors', blank=True, null=True)  # Field name made lowercase.
    title_ar = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    href = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    img_thumb = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_icons'


class HrAllowancesRelations(models.Model):
    type = models.PositiveIntegerField(blank=True, null=True)
    employee = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_allowances_relations'


class HrAllowancesTypes(models.Model):
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    percentage = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_allowances_types'


class HrAttendance(models.Model):
    term = models.IntegerField(blank=True, null=True)
    reviewed = models.PositiveIntegerField(blank=True, null=True)
    reviewed_by = models.PositiveIntegerField(blank=True, null=True)
    reviewed_date = models.DateTimeField(blank=True, null=True)
    employee = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    clock_in = models.TimeField(blank=True, null=True)
    clock_out = models.TimeField(blank=True, null=True)
    late = models.TimeField(blank=True, null=True)
    early = models.TimeField(blank=True, null=True)
    absent = models.IntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_attendance'


class HrDeductionsAdvancePayment(models.Model):
    employee_id = models.IntegerField(db_column='employee_ID')  # Field name made lowercase.
    amount = models.IntegerField()
    year = models.IntegerField()
    number_month = models.IntegerField()
    month = models.IntegerField()
    created_by = models.IntegerField(db_column='Created_by')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date')  # Field name made lowercase.
    is_deleted = models.IntegerField()
    deleted_by = models.IntegerField()
    deleted_date = models.DateTimeField()
    last_update_by = models.IntegerField()
    last_update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hr_deductions_advance_payment'


class HrDeductionsAdvancePaymentRecords(models.Model):
    employee_id = models.IntegerField(db_column='employee_ID', blank=True, null=True)  # Field name made lowercase.
    advace_payment_id = models.IntegerField(blank=True, null=True)
    amount = models.CharField(max_length=50, blank=True, null=True)
    is_paied = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.IntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_deductions_advance_payment_records'


class HrDeductionsRelations(models.Model):
    type = models.PositiveIntegerField(blank=True, null=True)
    employee = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_deductions_relations'


class HrDeductionsTypes(models.Model):
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    percentage = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_deductions_types'


class HrEmploymentApplications(models.Model):
    university = models.IntegerField(blank=True, null=True)
    college = models.PositiveIntegerField(blank=True, null=True)
    app_type = models.IntegerField()
    display_in_home = models.IntegerField(blank=True, null=True)
    renewal_date = models.DateField(blank=True, null=True)
    facebook_account = models.CharField(max_length=255, blank=True, null=True)
    twitter_account = models.CharField(max_length=255, blank=True, null=True)
    youtube_link = models.CharField(max_length=255, blank=True, null=True)
    account_id = models.PositiveIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    vacations_balance = models.IntegerField(blank=True, null=True)
    user_id = models.PositiveIntegerField(blank=True, null=True)
    employee_status = models.IntegerField(blank=True, null=True)
    deputy = models.PositiveIntegerField(blank=True, null=True)
    user_password = models.CharField(max_length=50, blank=True, null=True)
    app_status = models.PositiveIntegerField(blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    program = models.CharField(max_length=255, blank=True, null=True)
    plan = models.CharField(max_length=255, blank=True, null=True)
    study_class = models.CharField(max_length=255, blank=True, null=True)
    course = models.CharField(max_length=500, blank=True, null=True)
    max_daily_sections = models.IntegerField(blank=True, null=True)
    weekly_sections = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    app_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    app_password = models.CharField(max_length=50, blank=True, null=True)
    name_first_en = models.CharField(max_length=255, blank=True, null=True)
    name_father_en = models.CharField(max_length=255, blank=True, null=True)
    name_grandfather_en = models.CharField(max_length=255, blank=True, null=True)
    name_last_en = models.CharField(max_length=255, blank=True, null=True)
    name_first_ar = models.CharField(max_length=255, blank=True, null=True)
    name_father_ar = models.CharField(max_length=255, blank=True, null=True)
    name_grandfather_ar = models.CharField(max_length=255, blank=True, null=True)
    name_last_ar = models.CharField(max_length=255, blank=True, null=True)
    place_of_birth = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_birth_higri = models.CharField(max_length=30, blank=True, null=True)
    marital_status = models.PositiveIntegerField(blank=True, null=True)
    number_of_dependents = models.PositiveIntegerField(blank=True, null=True)
    nationality = models.PositiveIntegerField(blank=True, null=True)
    id_no = models.CharField(max_length=50, blank=True, null=True)
    id_copy = models.CharField(max_length=255, blank=True, null=True)
    id_expiry_date_higri = models.CharField(max_length=50, blank=True, null=True)
    id_expiry_date = models.DateField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    religion = models.PositiveIntegerField(blank=True, null=True)
    gender = models.PositiveIntegerField(blank=True, null=True)
    passport_number = models.CharField(max_length=50, blank=True, null=True)
    hr_section = models.PositiveIntegerField(blank=True, null=True)
    employee_type = models.PositiveIntegerField(blank=True, null=True)
    passport_expiration_date = models.DateField(blank=True, null=True)
    passport_expiration_date_higri = models.CharField(max_length=50, blank=True, null=True)
    department = models.PositiveIntegerField(blank=True, null=True)
    insurance_number = models.CharField(max_length=100, blank=True, null=True)
    hr_position = models.PositiveIntegerField(blank=True, null=True)
    starting_date = models.DateField(blank=True, null=True)
    employee_not_in_payroll = models.PositiveIntegerField(blank=True, null=True)
    job_title_ar = models.CharField(max_length=200, blank=True, null=True)
    job_title_en = models.CharField(max_length=200, blank=True, null=True)
    basic_salary = models.PositiveIntegerField(blank=True, null=True)
    bank = models.PositiveIntegerField(blank=True, null=True)
    iban = models.CharField(max_length=100, blank=True, null=True)
    profile_img = models.CharField(max_length=255, blank=True, null=True)
    img_path = models.CharField(max_length=255, blank=True, null=True)
    cv_file = models.CharField(max_length=255, blank=True, null=True)
    signature_file = models.CharField(max_length=255, blank=True, null=True)
    requirements_rating = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    delete_reason = models.CharField(max_length=255, blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    approved_by = models.PositiveIntegerField(blank=True, null=True)
    rejected_date = models.DateTimeField(blank=True, null=True)
    rejected_by = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employment_applications'


class HrEmploymentApplicationsApprovals(models.Model):
    order = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    app_id = models.PositiveIntegerField(blank=True, null=True)
    department = models.PositiveIntegerField(blank=True, null=True)
    interview_date = models.DateTimeField(blank=True, null=True)
    interview_place = models.TextField(blank=True, null=True)
    class_id = models.CharField(max_length=255, blank=True, null=True)
    attendee_pw = models.CharField(max_length=255, blank=True, null=True)
    moderator_pw = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    presenter_url = models.TextField(blank=True, null=True)
    attendee_url = models.TextField(blank=True, null=True)
    has_exam = models.PositiveIntegerField(blank=True, null=True)
    replied_date = models.DateTimeField(blank=True, null=True)
    replied_by = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employment_applications_approvals'


class HrEmploymentApplicationsCertificates(models.Model):
    application_id = models.PositiveIntegerField(blank=True, null=True)
    college_name = models.CharField(max_length=255, blank=True, null=True)
    certificate_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    period_in_days = models.PositiveIntegerField(blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    country = models.PositiveIntegerField(blank=True, null=True)
    attachment_file = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employment_applications_certificates'


class HrEmploymentApplicationsExperiances(models.Model):
    application_id = models.PositiveIntegerField(blank=True, null=True)
    employer_name = models.CharField(max_length=255, blank=True, null=True)
    period_in_months = models.PositiveIntegerField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    employer_location = models.CharField(max_length=255, blank=True, null=True)
    responsibality = models.TextField(blank=True, null=True)
    attachment_file = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employment_applications_experiances'


class HrEmploymentApplicationsQualifications(models.Model):
    application_id = models.PositiveIntegerField(blank=True, null=True)
    country = models.PositiveIntegerField(blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    graduation_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    degree = models.CharField(max_length=255, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    attachment_file = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employment_applications_qualifications'


class HrEmploymentCustomSections(models.Model):
    application_id = models.PositiveIntegerField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    course = models.PositiveIntegerField(blank=True, null=True)
    class_field = models.PositiveIntegerField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    is_concurrent = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hr_employment_custom_sections'


class HrEmploymentExcludedSections(models.Model):
    application_id = models.PositiveIntegerField(blank=True, null=True)
    day = models.CharField(max_length=255, blank=True, null=True)
    section_order = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hr_employment_excluded_sections'


class HrEmploymentForms(models.Model):
    for_university = models.IntegerField(blank=True, null=True)
    for_college = models.IntegerField(blank=True, null=True)
    college = models.PositiveIntegerField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    program = models.IntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    course = models.IntegerField(blank=True, null=True)
    name_ar = models.IntegerField()
    name_en = models.IntegerField()
    mobile = models.IntegerField()
    email = models.IntegerField()
    code = models.PositiveIntegerField(blank=True, null=True)
    vacations_balance = models.PositiveIntegerField(blank=True, null=True)
    date_of_birth = models.PositiveIntegerField(blank=True, null=True)
    date_of_birth_higri = models.IntegerField(blank=True, null=True)
    place_of_birth = models.PositiveIntegerField(blank=True, null=True)
    marital_status = models.PositiveIntegerField(blank=True, null=True)
    number_of_dependents = models.PositiveIntegerField(blank=True, null=True)
    nationality = models.PositiveIntegerField(blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    id_no = models.PositiveIntegerField(blank=True, null=True)
    id_copy = models.PositiveIntegerField(blank=True, null=True)
    img_path = models.IntegerField(blank=True, null=True)
    cv_file = models.IntegerField()
    id_expiry_date = models.PositiveIntegerField(blank=True, null=True)
    id_expiry_date_higri = models.PositiveIntegerField(blank=True, null=True)
    religion = models.PositiveIntegerField(blank=True, null=True)
    gender = models.PositiveIntegerField(blank=True, null=True)
    passport_number = models.IntegerField()
    hr_position = models.IntegerField()
    hr_section = models.IntegerField()
    employee_type = models.IntegerField()
    job_title = models.IntegerField()
    department = models.IntegerField()
    passport_expiration_date = models.IntegerField()
    passport_expiration_date_higri = models.IntegerField()
    starting_date = models.IntegerField()
    employee_not_in_payroll = models.IntegerField()
    insurance_number = models.IntegerField()
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employment_forms'


class HrFinesWarnings(models.Model):
    employee = models.PositiveIntegerField(blank=True, null=True)
    fine_type = models.PositiveIntegerField(blank=True, null=True)
    warning_type = models.PositiveIntegerField(blank=True, null=True)
    type = models.PositiveIntegerField(blank=True, null=True)
    month = models.PositiveIntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    reason = models.TextField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    approved_by = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_fines_warnings'


class HrLeaverequest(models.Model):
    leave_date = models.DateField(blank=True, null=True)
    leave_type = models.PositiveIntegerField(blank=True, null=True)
    from_field = models.TimeField(db_column='from', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.TimeField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_leaverequest'


class HrRewards(models.Model):
    employee = models.PositiveIntegerField(blank=True, null=True)
    reward_type = models.PositiveIntegerField(blank=True, null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    starting_due_month = models.PositiveIntegerField(blank=True, null=True)
    starting_due_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    reason = models.TextField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    approved_by = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_rewards'


class HrVacationsSettings(models.Model):
    college = models.IntegerField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    program = models.IntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    hr_position = models.IntegerField(blank=True, null=True)
    vacations_balance = models.IntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_vacations_settings'


class Imagescenter(models.Model):
    section = models.CharField(max_length=50, blank=True, null=True)
    ref_id = models.PositiveIntegerField(blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    img_thumb = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'imagescenter'


class Journal(models.Model):
    file_path = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    issue_number = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.IntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.IntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'journal'


class Layers(models.Model):
    id = models.BigAutoField(primary_key=True)
    slide_id = models.PositiveBigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    type = models.PositiveIntegerField(blank=True, null=True)
    hidden_on_mobile = models.PositiveIntegerField(blank=True, null=True)
    incoming_animation_classes = models.CharField(db_column='Incoming_animation_Classes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    outgoing_animation_classes = models.CharField(db_column='Outgoing_animation_Classes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_start = models.IntegerField(blank=True, null=True)
    data_speed = models.IntegerField(blank=True, null=True)
    data_x_ar = models.CharField(max_length=255, blank=True, null=True)
    data_x_en = models.CharField(max_length=255, blank=True, null=True)
    data_y_ar = models.CharField(max_length=255, blank=True, null=True)
    data_y_en = models.CharField(max_length=255, blank=True, null=True)
    data_easing = models.CharField(max_length=50, blank=True, null=True)
    data_endeasing = models.CharField(max_length=50, blank=True, null=True)
    data_end = models.IntegerField(blank=True, null=True)
    data_endspeed = models.IntegerField(blank=True, null=True)
    text_ar = models.CharField(max_length=255, blank=True, null=True)
    text_en = models.CharField(max_length=255, blank=True, null=True)
    href = models.CharField(max_length=255, blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    img_thumb = models.CharField(max_length=255, blank=True, null=True)
    font_color = models.CharField(max_length=255, blank=True, null=True)
    bg_color = models.CharField(max_length=255, blank=True, null=True)
    font_size = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layers'


class Letters(models.Model):
    target = models.IntegerField()
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'letters'


class LettersApplications(models.Model):
    letter = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    date3 = models.DateField(blank=True, null=True)
    date4 = models.DateField(blank=True, null=True)
    date5 = models.DateField(blank=True, null=True)
    time1 = models.TimeField(blank=True, null=True)
    time2 = models.TimeField(blank=True, null=True)
    number1 = models.IntegerField(blank=True, null=True)
    number2 = models.IntegerField(blank=True, null=True)
    number3 = models.IntegerField(blank=True, null=True)
    number4 = models.IntegerField(blank=True, null=True)
    number5 = models.IntegerField(blank=True, null=True)
    number6 = models.IntegerField(blank=True, null=True)
    varchar1 = models.CharField(max_length=255, blank=True, null=True)
    varchar2 = models.CharField(max_length=255, blank=True, null=True)
    varchar3 = models.CharField(max_length=255, blank=True, null=True)
    varchar4 = models.CharField(max_length=255, blank=True, null=True)
    varchar5 = models.CharField(max_length=255, blank=True, null=True)
    text1 = models.TextField(blank=True, null=True)
    text2 = models.TextField(blank=True, null=True)
    text3 = models.TextField(blank=True, null=True)
    text4 = models.TextField(blank=True, null=True)
    dropdown1 = models.IntegerField(blank=True, null=True)
    dropdown2 = models.IntegerField(blank=True, null=True)
    dropdown3 = models.IntegerField(blank=True, null=True)
    dropdown4 = models.IntegerField(blank=True, null=True)
    dropdown5 = models.IntegerField(blank=True, null=True)
    checkbox1 = models.CharField(max_length=150, blank=True, null=True)
    checkbox2 = models.CharField(max_length=150, blank=True, null=True)
    attachment = models.TextField(blank=True, null=True)
    directory = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'letters_applications'


class LettersApplicationsApprovals(models.Model):
    order = models.PositiveIntegerField(blank=True, null=True)
    app_status = models.PositiveIntegerField(blank=True, null=True)
    application_id = models.PositiveIntegerField(blank=True, null=True)
    department = models.PositiveIntegerField(blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    approved_by = models.PositiveIntegerField(blank=True, null=True)
    rejected_date = models.DateTimeField(blank=True, null=True)
    rejected_by = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'letters_applications_approvals'


class LettersApprovals(models.Model):
    order = models.PositiveIntegerField()
    letter = models.PositiveIntegerField(blank=True, null=True)
    department = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'letters_approvals'


class LettersDropdowns(models.Model):
    source = models.PositiveIntegerField()
    source_data = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'letters_dropdowns'


class LettersDropdownsOptions(models.Model):
    dropdown = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    salary_affect = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'letters_dropdowns_options'


class LettersFields(models.Model):
    letter = models.PositiveIntegerField(blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    col_name = models.CharField(max_length=255, blank=True, null=True)
    required = models.PositiveIntegerField(blank=True, null=True)
    type = models.PositiveIntegerField(blank=True, null=True)
    dropdown = models.PositiveIntegerField(blank=True, null=True)
    checkbox = models.PositiveIntegerField(blank=True, null=True)
    lable_width = models.PositiveIntegerField(blank=True, null=True)
    field_width = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'letters_fields'


class LibraryMainCats(models.Model):
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'library_main_cats'


class LibraryManager(models.Model):
    type = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    auther = models.CharField(max_length=255, blank=True, null=True)
    date_of_publication = models.DateField(blank=True, null=True)
    place_of_publication = models.CharField(max_length=255, blank=True, null=True)
    edition = models.CharField(max_length=255, blank=True, null=True)
    number_of_pages = models.PositiveIntegerField(blank=True, null=True)
    category_no = models.CharField(max_length=150, blank=True, null=True)
    topic_of_book = models.CharField(max_length=150, blank=True, null=True)
    public_number = models.CharField(max_length=150, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    summary_book = models.TextField(blank=True, null=True)
    pdf_file = models.CharField(max_length=255, blank=True, null=True)
    cover_image = models.CharField(max_length=255, blank=True, null=True)
    isbn = models.CharField(max_length=255, blank=True, null=True)
    part_number = models.IntegerField(blank=True, null=True)
    place_of_book = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    date_of_thesis = models.DateField(blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    hand_graduation = models.CharField(max_length=255, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    supervisor = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'library_manager'


class Menus(models.Model):
    order = models.IntegerField(blank=True, null=True)
    target = models.IntegerField()
    parent = models.IntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    internal_link = models.CharField(max_length=50, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    new_link = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menus'


class Messages(models.Model):
    priority = models.IntegerField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    from_field = models.PositiveIntegerField(db_column='from', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=255, blank=True, null=True)
    to_program = models.CharField(max_length=255, blank=True, null=True)
    to_major = models.CharField(max_length=255, blank=True, null=True)
    to_department = models.CharField(max_length=255, blank=True, null=True)
    to_section = models.CharField(max_length=255, blank=True, null=True)
    seen = models.CharField(max_length=255, blank=True, null=True)
    marked = models.TextField(blank=True, null=True)
    draft = models.TextField(blank=True, null=True)
    trash = models.TextField(blank=True, null=True)
    academic_year = models.IntegerField()
    term = models.PositiveIntegerField(blank=True, null=True)
    section = models.IntegerField(blank=True, null=True)
    lesson = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    upload_files = models.TextField(blank=True, null=True)
    closed = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class News(models.Model):
    stick = models.PositiveIntegerField(blank=True, null=True)
    view = models.PositiveBigIntegerField(blank=True, null=True)
    categorie = models.BigIntegerField(blank=True, null=True)
    field = models.BigIntegerField(blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    img_thumb = models.CharField(max_length=255, blank=True, null=True)
    title_ar = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    desc_ar = models.CharField(max_length=255, blank=True, null=True)
    desc_en = models.CharField(max_length=255, blank=True, null=True)
    other_details_ar = models.TextField(blank=True, null=True)
    other_details_en = models.TextField(blank=True, null=True)
    created_by = models.IntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.IntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class Notifications(models.Model):
    notification_cat = models.PositiveIntegerField(blank=True, null=True)
    first_ref = models.PositiveIntegerField(blank=True, null=True)
    affected_user = models.PositiveIntegerField(blank=True, null=True)
    effected_by = models.PositiveIntegerField(blank=True, null=True)
    sent_to_mail = models.PositiveIntegerField(blank=True, null=True)
    seen_in_system = models.PositiveIntegerField(blank=True, null=True)
    seen_in_system_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notifications'


class NotificationsList(models.Model):
    token = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    first_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications_list'


class OnlineApprovals(models.Model):
    order = models.PositiveIntegerField()
    course_exam = models.IntegerField(blank=True, null=True)
    exam = models.PositiveIntegerField(blank=True, null=True)
    department = models.PositiveIntegerField()
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_approvals'


class OnlineCourseExamCoordinators(models.Model):
    teacher = models.PositiveIntegerField(blank=True, null=True)
    course = models.PositiveIntegerField(blank=True, null=True)
    exam = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    college = models.IntegerField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    program = models.IntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_course_exam_coordinators'


class OnlineCourseExamParts(models.Model):
    course_exam_id = models.PositiveIntegerField(blank=True, null=True)
    locale = models.IntegerField(blank=True, null=True)
    no_of_questions = models.PositiveIntegerField(blank=True, null=True)
    question_type = models.PositiveIntegerField(blank=True, null=True)
    select_questions = models.PositiveIntegerField(blank=True, null=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    total_score = models.FloatField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_course_exam_parts'


class OnlineCourseExamQuestions(models.Model):
    course_exam_id = models.PositiveIntegerField(blank=True, null=True)
    exam_part_id = models.PositiveIntegerField(blank=True, null=True)
    question_id = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_course_exam_questions'


class OnlineCourseExamShares(models.Model):
    course_exam_id = models.PositiveIntegerField(blank=True, null=True)
    section = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_course_exam_shares'


class OnlineCourseExamStudents(models.Model):
    course_exam_id = models.PositiveIntegerField(blank=True, null=True)
    student = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_course_exam_students'


class OnlineCourseExams(models.Model):
    exam = models.PositiveIntegerField(blank=True, null=True)
    course_exam = models.IntegerField(blank=True, null=True)
    approved = models.IntegerField(blank=True, null=True)
    teacher = models.PositiveIntegerField(blank=True, null=True)
    global_field = models.IntegerField(db_column='global', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    is_general = models.IntegerField()
    in_exams_bank = models.IntegerField()
    term = models.PositiveIntegerField(blank=True, null=True)
    course = models.PositiveIntegerField(blank=True, null=True)
    section = models.PositiveIntegerField(blank=True, null=True)
    lesson = models.IntegerField(blank=True, null=True)
    chapter = models.IntegerField(blank=True, null=True)
    trial = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    locale = models.IntegerField()
    start_at = models.DateTimeField(blank=True, null=True)
    started_by = models.IntegerField(blank=True, null=True)
    started_date = models.DateTimeField(blank=True, null=True)
    is_cancelled = models.IntegerField(blank=True, null=True)
    cancelled_by = models.IntegerField(blank=True, null=True)
    cancelled_date = models.DateTimeField(blank=True, null=True)
    required_update = models.IntegerField(blank=True, null=True)
    update_start_date = models.DateTimeField(blank=True, null=True)
    required_cancel = models.IntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_course_exams'


class OnlineExamsAnswers(models.Model):
    question_id = models.PositiveIntegerField(blank=True, null=True)
    answer_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_exams_answers'


class OnlineExamsAprrovals(models.Model):
    order = models.PositiveIntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)
    exam_id = models.PositiveIntegerField()
    department = models.PositiveIntegerField()
    replied_date = models.DateTimeField(blank=True, null=True)
    replied_by = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_exams_aprrovals'


class OnlineExamsAttachments(models.Model):
    type = models.PositiveIntegerField(blank=True, null=True)
    type_id = models.PositiveIntegerField(blank=True, null=True)
    file_path = models.CharField(max_length=255)
    file2_path = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_exams_attachments'


class OnlineExamsQuestions(models.Model):
    term = models.IntegerField(blank=True, null=True)
    exercise = models.IntegerField(blank=True, null=True)
    teacher = models.PositiveIntegerField(blank=True, null=True)
    course = models.PositiveIntegerField(blank=True, null=True)
    college = models.IntegerField()
    major = models.IntegerField(blank=True, null=True)
    program = models.IntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    lesson = models.IntegerField(blank=True, null=True)
    question_type = models.PositiveIntegerField(blank=True, null=True)
    no_of_points = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    video_path = models.CharField(max_length=255, blank=True, null=True)
    score = models.PositiveIntegerField(blank=True, null=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    difficulty_degree = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_exams_questions'


class OnlineStudentExamAnswers(models.Model):
    student_exam = models.PositiveIntegerField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    question = models.PositiveIntegerField(blank=True, null=True)
    answer = models.PositiveIntegerField(blank=True, null=True)
    matched_answer = models.IntegerField(blank=True, null=True)
    student_answer = models.IntegerField(blank=True, null=True)
    answer_order = models.IntegerField(blank=True, null=True)
    answer_description = models.TextField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    mark = models.FloatField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_student_exam_answers'


class OnlineStudentExamLogins(models.Model):
    student = models.PositiveIntegerField(blank=True, null=True)
    exam = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'online_student_exam_logins'


class OnlineStudentExams(models.Model):
    exam = models.PositiveIntegerField(blank=True, null=True)
    student = models.PositiveIntegerField(blank=True, null=True)
    section = models.PositiveIntegerField(blank=True, null=True)
    is_saved = models.IntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_student_exams'


class OnlineStudentTestAnswers(models.Model):
    student_exam = models.PositiveIntegerField(blank=True, null=True)
    question = models.PositiveIntegerField(blank=True, null=True)
    answer = models.PositiveIntegerField(blank=True, null=True)
    matched_answer = models.IntegerField(blank=True, null=True)
    student_answer = models.IntegerField(blank=True, null=True)
    answer_order = models.IntegerField(blank=True, null=True)
    answer_description = models.TextField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    mark = models.FloatField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_student_test_answers'


class OnlineStudentTests(models.Model):
    exam = models.PositiveIntegerField(blank=True, null=True)
    student = models.PositiveIntegerField(blank=True, null=True)
    section = models.PositiveIntegerField(blank=True, null=True)
    is_saved = models.IntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_student_tests'


class Pages(models.Model):
    order = models.PositiveIntegerField(blank=True, null=True)
    title_ar = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    content_ar = models.TextField(blank=True, null=True)
    content_en = models.TextField(blank=True, null=True)
    created_by = models.IntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.IntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages'


class PermissionSections(models.Model):
    parent = models.PositiveIntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permission_sections'


class PermissionsGroups(models.Model):
    name_ar = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions_groups'


class PermissionsGroupsRolesRelations(models.Model):
    groub = models.PositiveIntegerField(blank=True, null=True)
    role = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions_groups_roles_relations'


class PermissionsGroupsUsersRelations(models.Model):
    groub = models.PositiveIntegerField(blank=True, null=True)
    user = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions_groups_users_relations'


class Relations(models.Model):
    announcements = models.PositiveIntegerField(blank=True, null=True)
    new = models.PositiveIntegerField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    tag = models.PositiveIntegerField(blank=True, null=True)
    lang = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relations'


class ResultsApprovals(models.Model):
    order = models.PositiveIntegerField()
    department = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'results_approvals'


class ResultsEditApprovals(models.Model):
    order = models.PositiveIntegerField()
    department = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'results_edit_approvals'


class Roles(models.Model):
    section = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    disables = models.IntegerField(blank=True, null=True)
    add_hr = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class RolesUsers(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    role_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'roles_users'
        unique_together = (('user_id', 'role_id'),)


class Slides(models.Model):
    id = models.BigAutoField(primary_key=True)
    show_for_visitors = models.PositiveIntegerField(db_column='Show_for_Visitors', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=255, blank=True, null=True)
    href = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    img_thumb = models.CharField(max_length=255, blank=True, null=True)
    bg_color = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'slides'


class Speeches(models.Model):
    readed = models.PositiveIntegerField()
    sended_to_admin_main = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    admin_reply_status = models.PositiveIntegerField()
    admin_reply = models.TextField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    important = models.IntegerField(blank=True, null=True)
    archive_url = models.TextField(db_collation='utf8mb3_general_ci', blank=True, null=True)
    accepted = models.IntegerField(db_column='Accepted', blank=True, null=True)  # Field name made lowercase.
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    upload_files = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'speeches'


class SpeechesSettings(models.Model):
    id = models.BigAutoField(primary_key=True)
    position = models.PositiveBigIntegerField(blank=True, null=True)
    type = models.PositiveIntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    title_male_ar = models.CharField(max_length=255, blank=True, null=True)
    title_female_ar = models.CharField(max_length=255, blank=True, null=True)
    title_male_en = models.CharField(max_length=255, blank=True, null=True)
    title_female_en = models.CharField(max_length=255, blank=True, null=True)
    data_x_ar = models.CharField(max_length=255, blank=True, null=True)
    data_x_en = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'speeches_settings'


class StoresGoodsDeliveryVoucher(models.Model):
    voucher_type = models.PositiveIntegerField(blank=True, null=True)
    type_of_recipient = models.PositiveIntegerField()
    store = models.PositiveIntegerField(blank=True, null=True)
    customer = models.PositiveIntegerField(blank=True, null=True)
    employee = models.PositiveIntegerField(blank=True, null=True)
    room = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    count_type_customer = models.IntegerField(blank=True, null=True)
    count_type_employee = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_goods_delivery_voucher'


class StoresGoodsDeliveryVoucherItems(models.Model):
    voucher_id = models.PositiveIntegerField(blank=True, null=True)
    item = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_goods_delivery_voucher_items'


class StoresGoodsEliminationVoucher(models.Model):
    img = models.CharField(max_length=255, blank=True, null=True)
    img_thumb = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_goods_elimination_voucher'


class StoresGoodsEliminationVoucherItems(models.Model):
    voucher_id = models.PositiveIntegerField(blank=True, null=True)
    item = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_goods_elimination_voucher_items'


class StoresGoodsReceiptsVoucher(models.Model):
    deliverer_type = models.PositiveIntegerField(blank=True, null=True)
    employee = models.PositiveIntegerField(blank=True, null=True)
    store = models.PositiveIntegerField(blank=True, null=True)
    supplier = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    count_type_employee = models.IntegerField(blank=True, null=True)
    count_type_supplier = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_goods_receipts_voucher'


class StoresGoodsReceiptsVoucherItems(models.Model):
    voucher_id = models.PositiveIntegerField(blank=True, null=True)
    item = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_goods_receipts_voucher_items'


class StoresGoodsTransfareVoucher(models.Model):
    from_store = models.PositiveIntegerField(blank=True, null=True)
    to_store = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_goods_transfare_voucher'


class StoresGoodsTransfareVoucherItems(models.Model):
    voucher_id = models.PositiveIntegerField(blank=True, null=True)
    item = models.PositiveIntegerField(blank=True, null=True)
    new_item = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_goods_transfare_voucher_items'


class StoresInventory(models.Model):
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    shelf = models.CharField(max_length=255, blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    category = models.PositiveIntegerField(blank=True, null=True)
    unit = models.PositiveIntegerField(blank=True, null=True)
    sales_price = models.PositiveIntegerField(blank=True, null=True)
    min_qty = models.PositiveIntegerField(blank=True, null=True)
    max_qty = models.PositiveIntegerField(blank=True, null=True)
    store = models.PositiveIntegerField(blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    commision = models.IntegerField(blank=True, null=True)
    commision_percentage = models.PositiveIntegerField(blank=True, null=True)
    service_item = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    init_quantitiy = models.CharField(max_length=255, blank=True, null=True)
    temp_qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_inventory'


class StoresPurchase(models.Model):
    type = models.CharField(max_length=10, blank=True, null=True)
    quotation = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_purchase'


class StoresPurchaseElements(models.Model):
    purchase_number = models.PositiveIntegerField(blank=True, null=True)
    item = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_purchase_elements'


class StoresPurchaseElementsReturned(models.Model):
    element = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    returned_date = models.DateField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_purchase_elements_returned'


class StoresSalesElementsReturned(models.Model):
    element = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    returned_date = models.DateField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_sales_elements_returned'


class StoresSalesInvoice(models.Model):
    type_of_recipient = models.PositiveIntegerField()
    store = models.PositiveIntegerField(blank=True, null=True)
    customer = models.PositiveIntegerField(blank=True, null=True)
    student = models.PositiveIntegerField(blank=True, null=True)
    employee = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_sales_invoice'


class StoresSalesInvoiceItems(models.Model):
    voucher_id = models.PositiveIntegerField(blank=True, null=True)
    item = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_sales_invoice_items'


class StoresStocktakingProcess(models.Model):
    temp_id = models.IntegerField(blank=True, null=True)
    is_submitted = models.IntegerField(blank=True, null=True)
    type = models.PositiveIntegerField(blank=True, null=True)
    store_id = models.PositiveIntegerField(blank=True, null=True)
    categorie_id = models.PositiveIntegerField(blank=True, null=True)
    stocktake = models.PositiveIntegerField(blank=True, null=True)
    stocktake_date = models.DateTimeField(blank=True, null=True)
    stocktake_by = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_stocktaking_process'


class StoresStocktakingProcessElements(models.Model):
    stocktaking_id = models.PositiveIntegerField(blank=True, null=True)
    item = models.PositiveIntegerField(blank=True, null=True)
    qty = models.PositiveIntegerField(blank=True, null=True)
    qty_before_stocktaking = models.IntegerField(blank=True, null=True)
    cost_before_stocktaking = models.IntegerField(blank=True, null=True)
    cost_after_stocktaking = models.IntegerField(blank=True, null=True)
    cost_difference = models.IntegerField(blank=True, null=True)
    qty_diff = models.IntegerField(blank=True, null=True)
    stocktake = models.PositiveIntegerField(blank=True, null=True)
    stocktake_date = models.DateTimeField(blank=True, null=True)
    stocktake_by = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_stocktaking_process_elements'


class StudentsAbsents(models.Model):
    student_id = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveIntegerField()
    excused_absence = models.IntegerField()
    day_absence = models.IntegerField(blank=True, null=True)
    class_id = models.IntegerField(blank=True, null=True)
    section_id = models.PositiveIntegerField(blank=True, null=True)
    lab_id = models.IntegerField(blank=True, null=True)
    mark = models.FloatField()
    absent_date = models.DateField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_absents'


class StudentsApplications(models.Model):
    academicyear = models.IntegerField(blank=True, null=True)
    student_code = models.CharField(max_length=200, blank=True, null=True)
    app_status = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    last_exam_notification = models.IntegerField(blank=True, null=True)
    religion = models.IntegerField()
    cancelled_date = models.DateTimeField(blank=True, null=True)
    id_can_order_other = models.PositiveIntegerField(blank=True, null=True)
    s_type = models.PositiveIntegerField(db_column='S_Type', blank=True, null=True)  # Field name made lowercase.
    graduation_gpa = models.FloatField(db_column='graduation_GPA', blank=True, null=True)  # Field name made lowercase.
    graduation_date = models.DateField(blank=True, null=True)
    academic_status = models.IntegerField()
    grade = models.PositiveIntegerField(db_column='Grade', blank=True, null=True)  # Field name made lowercase.
    rejected = models.PositiveIntegerField(blank=True, null=True)
    rejected_date = models.DateTimeField(blank=True, null=True)
    rejected_by = models.PositiveIntegerField(blank=True, null=True)
    rejected_notes = models.TextField(blank=True, null=True)
    finished = models.PositiveIntegerField(blank=True, null=True)
    app_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    app_password = models.CharField(max_length=50, blank=True, null=True)
    student_id = models.PositiveIntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    study_type = models.PositiveIntegerField(blank=True, null=True)
    student_type = models.PositiveIntegerField(blank=True, null=True)
    degree = models.PositiveIntegerField(blank=True, null=True)
    level = models.PositiveIntegerField(blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    app_type = models.IntegerField(blank=True, null=True)
    amount_to_pay = models.IntegerField()
    amount_paid = models.IntegerField()
    cash = models.IntegerField(db_column='Cash')  # Field name made lowercase.
    bank_transfer = models.IntegerField(db_column='Bank_Transfer')  # Field name made lowercase.
    atm = models.IntegerField(db_column='ATM')  # Field name made lowercase.
    cheque = models.IntegerField(db_column='Cheque')  # Field name made lowercase.
    check_bank = models.CharField(max_length=255, blank=True, null=True)
    check_number = models.CharField(max_length=255, blank=True, null=True)
    check_maturity_date = models.DateField(blank=True, null=True)
    discount = models.IntegerField(db_column='Discount')  # Field name made lowercase.
    university = models.IntegerField()
    college = models.IntegerField()
    major = models.PositiveIntegerField(blank=True, null=True)
    program = models.IntegerField()
    plan = models.IntegerField()
    branch = models.IntegerField(blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    academic_supervisor = models.PositiveIntegerField(blank=True, null=True)
    initial_approval = models.PositiveIntegerField(db_column='Initial_Approval')  # Field name made lowercase.
    interview_date = models.DateTimeField(blank=True, null=True)
    interview_state = models.CharField(max_length=10, blank=True, null=True)
    interview_notes = models.TextField(blank=True, null=True)
    ip_of_application = models.CharField(max_length=40, blank=True, null=True)
    need_to_review = models.PositiveIntegerField(blank=True, null=True)
    full_name_arabic = models.CharField(db_column='Full_Name_Arabic', max_length=255, blank=True, null=True)  # Field name made lowercase.
    full_name_english = models.CharField(db_column='Full_Name_English', max_length=255, blank=True, null=True)  # Field name made lowercase.
    place_of_birth = models.CharField(db_column='Place_of_birth', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_of_birth = models.DateField(db_column='Date_of_Birth', blank=True, null=True)  # Field name made lowercase.
    date_of_birth_higri = models.CharField(db_column='Date_of_Birth_higri', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gender = models.PositiveIntegerField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    has_brothers = models.IntegerField(blank=True, null=True)
    order_in_brothers = models.IntegerField(blank=True, null=True)
    academic_number = models.CharField(db_column='Academic_Number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nationality = models.PositiveIntegerField(db_column='Nationality', blank=True, null=True)  # Field name made lowercase.
    id_no = models.CharField(db_column='ID_No', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_expiry_date = models.DateField(db_column='ID_Expiry_Date', blank=True, null=True)  # Field name made lowercase.
    id_expiry_date_higri = models.CharField(db_column='ID_Expiry_Date_higri', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    office_phone = models.CharField(db_column='Office_Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    house_no = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    g_relation = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=200, blank=True, null=True)
    sponsor_full_name_arabic = models.CharField(db_column='Sponsor_Full_Name_Arabic', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sponsor_full_name_english = models.CharField(db_column='Sponsor_Full_Name_English', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sponsor_mobile = models.CharField(db_column='Sponsor_Mobile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sponsor_office_number = models.CharField(db_column='Sponsor_Office_number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sponsor_email = models.CharField(db_column='Sponsor_Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sponsor_legal_form = models.PositiveIntegerField(db_column='Sponsor_Legal_Form', blank=True, null=True)  # Field name made lowercase.
    sponsor_address = models.CharField(db_column='Sponsor_Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hs_school_name = models.CharField(db_column='hs_School_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hs_certificate_type = models.PositiveIntegerField(db_column='hs_Certificate_Type', blank=True, null=True)  # Field name made lowercase.
    hs_qudurat_points = models.PositiveIntegerField(db_column='hs_Qudurat_points', blank=True, null=True)  # Field name made lowercase.
    hs_tofel_points = models.PositiveIntegerField(db_column='hs_Tofel_Points', blank=True, null=True)  # Field name made lowercase.
    hs_country = models.PositiveIntegerField(db_column='hs_Country', blank=True, null=True)  # Field name made lowercase.
    hs_graduation_year = models.TextField(db_column='hs_Graduation_Year', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hs_graduation_year_higri = models.CharField(db_column='hs_Graduation_Year_Higri', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hs_percentage = models.CharField(db_column='hs_Percentage', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hs_grade_total = models.PositiveIntegerField(db_column='hs_Grade_total', blank=True, null=True)  # Field name made lowercase.
    hs_tahsele_points = models.PositiveIntegerField(db_column='hs_Tahsele_Points', blank=True, null=True)  # Field name made lowercase.
    hs_city = models.PositiveIntegerField(db_column='hs_City', blank=True, null=True)  # Field name made lowercase.
    ba_college = models.CharField(db_column='ba_College', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ba_university = models.CharField(db_column='ba_University', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ba_major = models.CharField(db_column='ba_Major', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ba_general_grade = models.CharField(db_column='ba_General_Grade', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ba_gpa = models.FloatField(db_column='ba_GPA', blank=True, null=True)  # Field name made lowercase.
    ba_gpa_old = models.CharField(db_column='ba_GPA_old', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ba_grade_total = models.CharField(db_column='ba_Grade_Total', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ba_graduation_year = models.TextField(db_column='ba_Graduation_Year', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ba_graduation_year_higri = models.CharField(db_column='ba_Graduation_Year_higri', max_length=50, blank=True, null=True)  # Field name made lowercase.
    master_college = models.CharField(db_column='Master_College', max_length=255, blank=True, null=True)  # Field name made lowercase.
    master_university = models.CharField(db_column='Master_University', max_length=255, blank=True, null=True)  # Field name made lowercase.
    master_major = models.CharField(db_column='Master_Major', max_length=255, blank=True, null=True)  # Field name made lowercase.
    master_graduate_year = models.CharField(db_column='Master_Graduate_year', max_length=255, blank=True, null=True)  # Field name made lowercase.
    master_total_grade = models.CharField(db_column='Master_Total_Grade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    master_general_grade = models.CharField(db_column='Master_General_Grade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    master_gpa = models.CharField(db_column='Master_GPA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    e_employeed = models.CharField(db_column='E_Employeed', max_length=10, blank=True, null=True)  # Field name made lowercase.
    e_eapproval = models.CharField(db_column='E_Eapproval', max_length=10, blank=True, null=True)  # Field name made lowercase.
    e_employer = models.CharField(db_column='E_Employer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    e_location = models.CharField(db_column='E_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    e_experience_level = models.PositiveIntegerField(db_column='E_Experience_level', blank=True, null=True)  # Field name made lowercase.
    e_occupation = models.CharField(db_column='E_Occupation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    e_work_tel_number = models.CharField(db_column='E_work_tel_number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    e_salary = models.CharField(db_column='E_Salary', max_length=255, blank=True, null=True)  # Field name made lowercase.
    e_level = models.CharField(db_column='E_Level', max_length=255, blank=True, null=True)  # Field name made lowercase.
    starting_date = models.CharField(db_column='Starting_Date', max_length=255, blank=True, null=True)  # Field name made lowercase.
    e_organization_id = models.CharField(db_column='E_Organization_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    browser = models.CharField(max_length=50, blank=True, null=True)
    os = models.CharField(max_length=50, blank=True, null=True)
    device = models.CharField(max_length=50, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_applications'


class StudentsApplicationsApprovals(models.Model):
    seen = models.IntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    app_id = models.PositiveIntegerField(blank=True, null=True)
    department = models.PositiveIntegerField(blank=True, null=True)
    interview_date = models.DateTimeField(blank=True, null=True)
    interview_place = models.TextField(blank=True, null=True)
    interview_mark = models.IntegerField(blank=True, null=True)
    interview_note = models.CharField(max_length=255, blank=True, null=True)
    class_id = models.CharField(max_length=255, blank=True, null=True)
    attendee_pw = models.CharField(max_length=255, blank=True, null=True)
    moderator_pw = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    presenter_url = models.TextField(blank=True, null=True)
    attendee_url = models.TextField(blank=True, null=True)
    replied_date = models.DateTimeField(blank=True, null=True)
    replied_by = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_applications_approvals'


class StudentsApplicationsDocumentDetails(models.Model):
    student_application_document_id = models.PositiveIntegerField()
    file_path = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_applications_document_details'


class StudentsApplicationsDocuments(models.Model):
    student_application_id = models.PositiveIntegerField()
    document_type = models.PositiveIntegerField()
    file_path = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_applications_documents'


class StudentsApplicationsDocumentsTypes(models.Model):
    student_application_type = models.CharField(max_length=50)
    name_ar = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    max_file_size = models.PositiveIntegerField()
    allow_file_ext = models.CharField(max_length=255)
    required = models.PositiveIntegerField()
    is_deleted = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_applications_documents_types'


class StudentsApplicationsSteps(models.Model):
    student_application_id = models.PositiveIntegerField()
    step = models.CharField(max_length=50)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_applications_steps'


class StudentsCertificates(models.Model):
    term = models.PositiveIntegerField(blank=True, null=True)
    student = models.PositiveIntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    student_order = models.IntegerField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    no_of_views = models.IntegerField()
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_certificates'


class StudentsChatsClasses(models.Model):
    chat_id = models.PositiveIntegerField()
    class_id = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_chats_classes'


class StudentsCoursesDegrees(models.Model):
    exam = models.PositiveIntegerField()
    course_exam = models.IntegerField(blank=True, null=True)
    section = models.PositiveIntegerField()
    course = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveIntegerField()
    student = models.PositiveIntegerField()
    degree = models.CharField(max_length=255)
    status = models.PositiveIntegerField()
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_courses_degrees'


class StudentsCoursesDegreesBranches(models.Model):
    students_courses_degree = models.PositiveIntegerField()
    course_exam = models.IntegerField(blank=True, null=True)
    lab = models.PositiveIntegerField(blank=True, null=True)
    degree = models.CharField(max_length=255)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_courses_degrees_branches'


class StudentsCoursesEquations(models.Model):
    state = models.PositiveIntegerField(blank=True, null=True)
    course_id = models.PositiveIntegerField(blank=True, null=True)
    student_id = models.PositiveIntegerField(blank=True, null=True)
    equivalent_course = models.CharField(max_length=255, blank=True, null=True)
    equivalent_course_mark = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_courses_equations'


class StudentsElectiveCourses(models.Model):
    student = models.PositiveIntegerField(blank=True, null=True)
    course = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_elective_courses'


class StudentsInfractions(models.Model):
    student_id = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveIntegerField()
    section_id = models.PositiveIntegerField(blank=True, null=True)
    mark = models.FloatField()
    infraction_type = models.PositiveIntegerField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    file_path = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_infractions'


class StudentsLessonsDocuments(models.Model):
    student = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveIntegerField(blank=True, null=True)
    section = models.PositiveIntegerField(blank=True, null=True)
    document = models.PositiveIntegerField(blank=True, null=True)
    is_saved = models.IntegerField(blank=True, null=True)
    file_path = models.CharField(max_length=255)
    mark = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_lessons_documents'


class StudentsLessonsDocumentsAnswers(models.Model):
    student_exam = models.PositiveIntegerField(blank=True, null=True)
    question = models.PositiveIntegerField(blank=True, null=True)
    answer = models.PositiveIntegerField(blank=True, null=True)
    matched_answer = models.IntegerField(blank=True, null=True)
    student_answer = models.IntegerField(blank=True, null=True)
    answer_order = models.IntegerField()
    answer_description = models.TextField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    mark = models.FloatField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_lessons_documents_answers'


class StudentsLessonsDocumentsLogs(models.Model):
    student = models.PositiveIntegerField()
    term = models.IntegerField(blank=True, null=True)
    section = models.IntegerField(blank=True, null=True)
    document = models.PositiveIntegerField(blank=True, null=True)
    lesson = models.IntegerField(blank=True, null=True)
    no_of_opens = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_lessons_documents_logs'


class StudentsLetters(models.Model):
    target = models.IntegerField()
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_letters'


class StudentsLettersApplications(models.Model):
    app_status = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    student = models.IntegerField(blank=True, null=True)
    term = models.IntegerField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    program = models.IntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    letter = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    date3 = models.DateField(blank=True, null=True)
    date4 = models.DateField(blank=True, null=True)
    date5 = models.DateField(blank=True, null=True)
    time1 = models.TimeField(blank=True, null=True)
    time2 = models.TimeField(blank=True, null=True)
    number1 = models.IntegerField(blank=True, null=True)
    number2 = models.IntegerField(blank=True, null=True)
    number3 = models.IntegerField(blank=True, null=True)
    number4 = models.IntegerField(blank=True, null=True)
    number5 = models.IntegerField(blank=True, null=True)
    number6 = models.IntegerField(blank=True, null=True)
    varchar1 = models.CharField(max_length=255, blank=True, null=True)
    varchar2 = models.CharField(max_length=255, blank=True, null=True)
    varchar3 = models.CharField(max_length=255, blank=True, null=True)
    varchar4 = models.CharField(max_length=255, blank=True, null=True)
    varchar5 = models.CharField(max_length=255, blank=True, null=True)
    varchar6 = models.CharField(max_length=255, blank=True, null=True)
    varchar7 = models.CharField(max_length=255, blank=True, null=True)
    varchar8 = models.CharField(max_length=255, blank=True, null=True)
    varchar9 = models.CharField(max_length=255, blank=True, null=True)
    varchar10 = models.CharField(max_length=255, blank=True, null=True)
    varchar11 = models.CharField(max_length=255, blank=True, null=True)
    varchar12 = models.CharField(max_length=255, blank=True, null=True)
    text1 = models.TextField(blank=True, null=True)
    text2 = models.TextField(blank=True, null=True)
    text3 = models.TextField(blank=True, null=True)
    text4 = models.TextField(blank=True, null=True)
    text5 = models.TextField(blank=True, null=True)
    dropdown1 = models.IntegerField(blank=True, null=True)
    dropdown2 = models.IntegerField(blank=True, null=True)
    checkbox1 = models.CharField(max_length=150, blank=True, null=True)
    checkbox2 = models.CharField(max_length=150, blank=True, null=True)
    attachment = models.TextField(blank=True, null=True)
    directory = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_letters_applications'


class StudentsLettersApplicationsApprovals(models.Model):
    order = models.PositiveIntegerField(blank=True, null=True)
    app_status = models.PositiveIntegerField(blank=True, null=True)
    application_id = models.PositiveIntegerField(blank=True, null=True)
    department = models.PositiveIntegerField(blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    approved_by = models.PositiveIntegerField(blank=True, null=True)
    rejected_date = models.DateTimeField(blank=True, null=True)
    rejected_by = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_letters_applications_approvals'


class StudentsLettersApprovals(models.Model):
    order = models.PositiveIntegerField()
    letter = models.PositiveIntegerField(blank=True, null=True)
    department = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_letters_approvals'


class StudentsLettersDropdowns(models.Model):
    source = models.PositiveIntegerField()
    source_data = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    is_active = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_letters_dropdowns'


class StudentsLettersDropdownsOptions(models.Model):
    dropdown = models.PositiveIntegerField()
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    salary_affect = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_letters_dropdowns_options'


class StudentsLettersFields(models.Model):
    letter = models.PositiveIntegerField(blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    col_name = models.CharField(max_length=255, blank=True, null=True)
    required = models.PositiveIntegerField(blank=True, null=True)
    type = models.PositiveIntegerField(blank=True, null=True)
    dropdown = models.PositiveIntegerField(blank=True, null=True)
    checkbox = models.PositiveIntegerField(blank=True, null=True)
    lable_width = models.PositiveIntegerField(blank=True, null=True)
    field_width = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_letters_fields'


class StudentsLogs(models.Model):
    operation = models.PositiveIntegerField(blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    old_int_val = models.IntegerField(blank=True, null=True)
    new_int_val = models.IntegerField(blank=True, null=True)
    ref_id = models.PositiveIntegerField(blank=True, null=True)
    ref1_id = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_logs'


class StudentsNotes(models.Model):
    student_id = models.PositiveIntegerField(blank=True, null=True)
    term = models.IntegerField(blank=True, null=True)
    section_id = models.PositiveIntegerField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    file_path = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_notes'


class StudentsOperations(models.Model):
    title_ar = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    ref_id = models.CharField(max_length=255, blank=True, null=True)
    ref1_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_operations'


class StudentsParentsApplications(models.Model):
    allowed_result = models.IntegerField()
    user_id = models.PositiveIntegerField(blank=True, null=True)
    user_password = models.CharField(max_length=50, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    job_place = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    home_number = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.PositiveIntegerField(blank=True, null=True)
    id_no = models.CharField(max_length=50, blank=True, null=True)
    id_copy = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    whats_app = models.CharField(db_column='whats_App', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    relation = models.PositiveIntegerField(blank=True, null=True)
    study_level = models.IntegerField(blank=True, null=True)
    f_name_ar = models.CharField(max_length=255, blank=True, null=True)
    f_name_en = models.CharField(max_length=255, blank=True, null=True)
    f_id_no = models.CharField(max_length=50, blank=True, null=True)
    f_status = models.CharField(max_length=200, blank=True, null=True)
    f_email = models.CharField(max_length=255, blank=True, null=True)
    f_study_level = models.IntegerField(blank=True, null=True)
    f_job_title = models.CharField(max_length=255, blank=True, null=True)
    f_job_place = models.CharField(max_length=255, blank=True, null=True)
    f_whats_app = models.CharField(db_column='f_whats_App', max_length=20)  # Field name made lowercase.
    f_home_number = models.IntegerField()
    f_mobile = models.CharField(max_length=20)
    m_name_ar = models.CharField(max_length=255, blank=True, null=True)
    m_name_en = models.CharField(max_length=255, blank=True, null=True)
    m_id_no = models.CharField(max_length=50, blank=True, null=True)
    m_email = models.CharField(max_length=255, blank=True, null=True)
    m_study_level = models.IntegerField(blank=True, null=True)
    m_job_title = models.CharField(max_length=255, blank=True, null=True)
    m_job_place = models.CharField(max_length=255, blank=True, null=True)
    m_whats_app = models.CharField(db_column='m_whats_App', max_length=20, blank=True, null=True)  # Field name made lowercase.
    m_home_number = models.CharField(max_length=200, blank=True, null=True)
    m_mobile = models.CharField(max_length=50, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_parents_applications'


class StudentsParticipates(models.Model):
    student_id = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveIntegerField()
    section_id = models.PositiveIntegerField(blank=True, null=True)
    participate_type = models.PositiveIntegerField(blank=True, null=True)
    mark = models.PositiveIntegerField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_participates'


class StudentsPermissionsApprovals(models.Model):
    order = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    student_permission_id = models.PositiveIntegerField(blank=True, null=True)
    department = models.PositiveIntegerField(blank=True, null=True)
    replied_date = models.DateTimeField(blank=True, null=True)
    replied_by = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_permissions_approvals'


class StudentsResultsApprovals(models.Model):
    order = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveIntegerField(blank=True, null=True)
    student_term = models.PositiveIntegerField(blank=True, null=True)
    department = models.PositiveIntegerField(blank=True, null=True)
    replied_date = models.DateTimeField(blank=True, null=True)
    replied_by = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_results_approvals'


class StudentsResultsEdits(models.Model):
    student = models.PositiveIntegerField()
    term = models.PositiveIntegerField()
    section = models.PositiveIntegerField()
    exam = models.PositiveIntegerField()
    course_exam = models.IntegerField(blank=True, null=True)
    course = models.PositiveIntegerField(blank=True, null=True)
    mark = models.FloatField()
    status = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_results_edits'


class StudentsResultsEditsApprovals(models.Model):
    order = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    process_id = models.PositiveIntegerField(blank=True, null=True)
    department = models.PositiveIntegerField(blank=True, null=True)
    replied_date = models.DateTimeField(blank=True, null=True)
    replied_by = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_results_edits_approvals'


class StudentsSections(models.Model):
    term = models.PositiveIntegerField(blank=True, null=True)
    student = models.PositiveIntegerField(blank=True, null=True)
    section = models.PositiveIntegerField(blank=True, null=True)
    state = models.PositiveIntegerField(blank=True, null=True)
    exam_status = models.IntegerField()
    score = models.IntegerField(blank=True, null=True)
    mark = models.FloatField(blank=True, null=True)
    total_mark = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    percentage = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    grade_name = models.CharField(max_length=255, blank=True, null=True)
    rejected_by = models.PositiveIntegerField(blank=True, null=True)
    rejected_date = models.DateTimeField(blank=True, null=True)
    rejected_note = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_sections'


class StudentsSectionsLabs(models.Model):
    student = models.PositiveIntegerField(blank=True, null=True)
    lab = models.PositiveIntegerField(blank=True, null=True)
    student_section = models.PositiveIntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    mark = models.FloatField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_sections_labs'


class StudentsSectionsRatingDetails(models.Model):
    student_rating = models.PositiveIntegerField(blank=True, null=True)
    question = models.PositiveIntegerField(blank=True, null=True)
    answer = models.CharField(max_length=255, blank=True, null=True)
    rate = models.PositiveIntegerField(blank=True, null=True)
    prev_rate_diff = models.FloatField(blank=True, null=True)
    seen = models.IntegerField(blank=True, null=True)
    seen_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_sections_rating_details'


class StudentsSectionsRatings(models.Model):
    student = models.PositiveIntegerField(blank=True, null=True)
    rating = models.PositiveIntegerField(blank=True, null=True)
    period = models.PositiveIntegerField(blank=True, null=True)
    section = models.PositiveIntegerField(blank=True, null=True)
    seen = models.IntegerField(blank=True, null=True)
    seen_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_sections_ratings'


class StudentsSectionsRatings22(models.Model):
    student = models.PositiveIntegerField(blank=True, null=True)
    section = models.PositiveIntegerField(blank=True, null=True)
    question = models.PositiveIntegerField(blank=True, null=True)
    answer = models.CharField(max_length=255, blank=True, null=True)
    rate = models.PositiveIntegerField(blank=True, null=True)
    seen = models.IntegerField(blank=True, null=True)
    seen_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_sections_ratings22'


class StudentsStudyPermissions(models.Model):
    student = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveIntegerField(blank=True, null=True)
    permission_type = models.PositiveIntegerField(blank=True, null=True)
    reason = models.PositiveIntegerField(blank=True, null=True)
    permission_date = models.DateField(blank=True, null=True)
    file_path = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_study_permissions'


class StudentsStudyState(models.Model):
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_study_state'


class StudentsTeachersChats(models.Model):
    parent = models.IntegerField(blank=True, null=True)
    msg_type = models.IntegerField(blank=True, null=True)
    teacher = models.PositiveIntegerField(blank=True, null=True)
    student = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveIntegerField(blank=True, null=True)
    section = models.IntegerField(blank=True, null=True)
    course = models.PositiveIntegerField(blank=True, null=True)
    chapter = models.IntegerField(blank=True, null=True)
    lesson = models.IntegerField(blank=True, null=True)
    question = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    upload_files = models.TextField(blank=True, null=True)
    closed = models.IntegerField(blank=True, null=True)
    attendee_url = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_teachers_chats'


class StudentsTerms(models.Model):
    order = models.IntegerField(blank=True, null=True)
    chat_service = models.IntegerField(blank=True, null=True)
    period = models.CharField(max_length=255, blank=True, null=True)
    term = models.PositiveIntegerField(blank=True, null=True)
    student = models.PositiveIntegerField(blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    college = models.IntegerField(blank=True, null=True)
    program = models.IntegerField()
    major = models.IntegerField()
    plan = models.IntegerField()
    level = models.IntegerField(blank=True, null=True)
    branch = models.IntegerField(blank=True, null=True)
    s_type = models.IntegerField(db_column='S_Type', blank=True, null=True)  # Field name made lowercase.
    seating_no = models.IntegerField(blank=True, null=True)
    secret_code = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    approved = models.IntegerField(blank=True, null=True)
    allowed_result = models.IntegerField()
    transfered = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_terms'


class StudentsTypes(models.Model):
    study_type = models.PositiveIntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_types'


class StudentsVclasses(models.Model):
    term = models.PositiveIntegerField()
    teacher = models.PositiveIntegerField()
    class_id = models.CharField(max_length=255)
    attendee_pw = models.CharField(max_length=255, blank=True, null=True)
    moderator_pw = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    attendee_limit = models.PositiveIntegerField(blank=True, null=True)
    presenter_url = models.TextField(blank=True, null=True)
    is_recorded = models.IntegerField()
    completed = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_vclasses'


class StudentsYearsDegrees(models.Model):
    student = models.PositiveIntegerField()
    academic_year = models.PositiveIntegerField()
    related_terms = models.CharField(max_length=255)
    course = models.PositiveIntegerField(blank=True, null=True)
    degree = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    approved = models.IntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_years_degrees'


class StudyAcademicyears(models.Model):
    college = models.IntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    max_absent = models.IntegerField()
    beginning_year = models.DateField(blank=True, null=True)
    end_year = models.DateField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_academicyears'


class StudyBranches(models.Model):
    college = models.PositiveIntegerField(blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_branches'


class StudyCollegeSettings(models.Model):
    college = models.IntegerField(blank=True, null=True)
    absence_status = models.IntegerField()
    first_warning = models.IntegerField()
    second_warning = models.IntegerField()
    receive_apps = models.IntegerField()
    calculate_age_to = models.DateField(blank=True, null=True)
    app_title_ar = models.CharField(max_length=255, blank=True, null=True)
    app_title_en = models.CharField(max_length=255, blank=True, null=True)
    app_fees = models.FloatField(blank=True, null=True)
    required_interview = models.IntegerField()
    app_description_ar = models.TextField(blank=True, null=True)
    app_description_en = models.TextField(blank=True, null=True)
    app_success_msg_ar = models.CharField(max_length=500, blank=True, null=True)
    app_success_msg_en = models.CharField(max_length=500, blank=True, null=True)
    registeration_status = models.IntegerField()
    app_academicyear = models.IntegerField(blank=True, null=True)
    app_term = models.IntegerField(blank=True, null=True)
    create_student_membership = models.CharField(max_length=255, blank=True, null=True)
    first_students_from = models.IntegerField()
    first_students_to = models.IntegerField()
    student_log_qrcode = models.IntegerField()
    notify_students = models.IntegerField()
    allow_change_status = models.IntegerField()
    brothers_discount = models.IntegerField()
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_college_settings'


class StudyColleges(models.Model):
    university = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    display_in_home = models.IntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    language = models.IntegerField()
    country = models.IntegerField(blank=True, null=True)
    country_code = models.IntegerField(blank=True, null=True)
    city = models.IntegerField()
    started_date = models.DateField()
    desc_ar = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    academic_year = models.IntegerField(blank=True, null=True)
    term = models.IntegerField(blank=True, null=True)
    exams_term = models.IntegerField(blank=True, null=True)
    day_sections = models.IntegerField()
    absence_status = models.IntegerField()
    first_warning = models.IntegerField()
    second_warning = models.IntegerField()
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    video_file = models.CharField(max_length=255, blank=True, null=True)
    profile_banner = models.CharField(max_length=200, blank=True, null=True)
    images = models.CharField(max_length=500, blank=True, null=True)
    video_path = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_colleges'


class StudyCourses(models.Model):
    language = models.IntegerField()
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    allow_concurrent_sessions = models.FloatField()
    max_absent = models.IntegerField()
    prerequisite_status = models.IntegerField()
    max_degree = models.IntegerField()
    min_degree = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    degree = models.PositiveIntegerField(blank=True, null=True)
    course_code = models.CharField(max_length=255, blank=True, null=True)
    course_number = models.CharField(max_length=255, blank=True, null=True)
    credit_hours = models.PositiveIntegerField(blank=True, null=True)
    attending_hours = models.PositiveIntegerField(blank=True, null=True)
    show_in_certificate = models.IntegerField()
    elective_course = models.PositiveIntegerField(blank=True, null=True)
    alternatives_courses = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_courses'


class StudyCoursesExams(models.Model):
    exam = models.PositiveIntegerField()
    exam_branch = models.IntegerField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    college = models.IntegerField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    program = models.IntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    course = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveIntegerField()
    mandatory = models.IntegerField()
    display_seating_no = models.IntegerField()
    display_name = models.IntegerField()
    display_secret_code = models.IntegerField()
    course_percentage = models.FloatField(blank=True, null=True)
    degree = models.FloatField()
    percentage = models.FloatField(blank=True, null=True)
    min_degree = models.FloatField()
    valid_from = models.DateField(blank=True, null=True)
    valid_to = models.DateField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_courses_exams'


class StudyCoursesPrerequisite(models.Model):
    course = models.PositiveIntegerField(blank=True, null=True)
    prerequisite_course = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'study_courses_prerequisite'


class StudyCoursesPrograms(models.Model):
    course = models.PositiveIntegerField(blank=True, null=True)
    college = models.IntegerField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    program = models.PositiveIntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    min_degree = models.FloatField(blank=True, null=True)
    max_degree = models.PositiveIntegerField(blank=True, null=True)
    term_mark = models.IntegerField(blank=True, null=True)
    max_absent = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_courses_programs'


class StudyDegrees(models.Model):
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_degrees'


class StudyDepartments(models.Model):
    college = models.PositiveIntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    desc_ar = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_departments'


class StudyExamCommitteeRanges(models.Model):
    term = models.IntegerField(blank=True, null=True)
    committee = models.PositiveIntegerField(blank=True, null=True)
    from_field = models.IntegerField(db_column='from', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_exam_committee_ranges'


class StudyExams(models.Model):
    parent = models.IntegerField(blank=True, null=True)
    exam_mark = models.IntegerField(blank=True, null=True)
    college = models.IntegerField(blank=True, null=True)
    branch = models.IntegerField(blank=True, null=True)
    program = models.IntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    display_result = models.IntegerField()
    display_details = models.IntegerField(blank=True, null=True)
    mark = models.FloatField(blank=True, null=True)
    min_mark = models.FloatField(blank=True, null=True)
    valid_from = models.DateField(blank=True, null=True)
    valid_to = models.DateField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_exams'


class StudyExamsCommittees(models.Model):
    college = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    committee_no = models.PositiveIntegerField(blank=True, null=True)
    no_of_students = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_exams_committees'


class StudyGrades(models.Model):
    college = models.IntegerField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    program = models.IntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    grade_en = models.CharField(max_length=50)
    grade_ar = models.CharField(max_length=50)
    min_degree = models.IntegerField()
    max_degree = models.IntegerField()
    rate = models.FloatField(blank=True, null=True)
    color = models.CharField(max_length=50)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_grades'


class StudyGraduatedSettings(models.Model):
    college = models.IntegerField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    program = models.PositiveIntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    display_in_certificate = models.PositiveIntegerField(blank=True, null=True)
    grade_for_course = models.IntegerField()
    grade_for_total = models.IntegerField()
    displayed_grade = models.IntegerField(blank=True, null=True)
    is_colored = models.IntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_graduated_settings'


class StudyGraduatesGrade(models.Model):
    college = models.IntegerField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    program = models.IntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    grade_en = models.CharField(max_length=50)
    grade_ar = models.CharField(max_length=50)
    min_rate = models.FloatField()
    max_rate = models.FloatField()
    min_percentage = models.IntegerField(blank=True, null=True)
    max_percentage = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=50)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_graduates_grade'


class StudyLabs(models.Model):
    section = models.PositiveIntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255)
    room = models.PositiveIntegerField(blank=True, null=True)
    teacher = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_labs'


class StudyLabsDates(models.Model):
    lab = models.PositiveIntegerField(blank=True, null=True)
    day = models.CharField(max_length=20, blank=True, null=True)
    start = models.TimeField(blank=True, null=True)
    end = models.TimeField(blank=True, null=True)
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'study_labs_dates'


class StudyLessonDocumentStudents(models.Model):
    study_document_id = models.PositiveIntegerField(blank=True, null=True)
    student = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_lesson_document_students'


class StudyLessonsDocuments(models.Model):
    term = models.IntegerField(blank=True, null=True)
    section = models.IntegerField(blank=True, null=True)
    course = models.IntegerField(blank=True, null=True)
    teacher = models.IntegerField(blank=True, null=True)
    lesson = models.PositiveIntegerField()
    document_type = models.CharField(max_length=255)
    is_general = models.IntegerField()
    many_attempts = models.IntegerField(blank=True, null=True)
    accepted_mark = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    locale = models.IntegerField(blank=True, null=True)
    mark = models.IntegerField()
    file_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file_path = models.CharField(max_length=255)
    youtube_link = models.CharField(max_length=255, blank=True, null=True)
    download_limit = models.DateField(blank=True, null=True)
    upload_limit = models.DateField()
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_lessons_documents'


class StudyLessonsTestParts(models.Model):
    study_document_id = models.PositiveIntegerField(blank=True, null=True)
    question_type = models.IntegerField(blank=True, null=True)
    total_score = models.FloatField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_lessons_test_parts'


class StudyLessonsTestQuestions(models.Model):
    study_document_id = models.PositiveIntegerField(blank=True, null=True)
    study_part_id = models.PositiveIntegerField(blank=True, null=True)
    question_id = models.PositiveIntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_lessons_test_questions'


class StudyLevels(models.Model):
    type = models.IntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    level_order = models.IntegerField()
    plan = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_levels'


class StudyLevelsCourses(models.Model):
    type = models.IntegerField()
    course = models.PositiveIntegerField(blank=True, null=True)
    level = models.PositiveIntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    alternative_course = models.IntegerField(blank=True, null=True)
    weekly_sections = models.IntegerField(blank=True, null=True)
    sessions_type = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'study_levels_courses'


class StudyMajors(models.Model):
    language = models.IntegerField()
    college = models.PositiveIntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    desc_ar = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    fa_education = models.CharField(max_length=200, blank=True, null=True)
    mo_education = models.CharField(max_length=200, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_majors'


class StudyPlanDepartments(models.Model):
    plan = models.PositiveIntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    no_of_students = models.IntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_plan_departments'


class StudyPlans(models.Model):
    program = models.PositiveIntegerField(blank=True, null=True)
    branch = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    is_final = models.IntegerField(blank=True, null=True)
    in_control = models.IntegerField(blank=True, null=True)
    require_admission = models.IntegerField(blank=True, null=True)
    number_ar = models.IntegerField(blank=True, null=True)
    number_en = models.IntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    desc_ar = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    is_open = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_plans'


class StudyPrograms(models.Model):
    major = models.PositiveIntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    desc_ar = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_programs'


class StudyRooms(models.Model):
    college = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_rooms'


class StudySectionPlans(models.Model):
    teacher = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveIntegerField(blank=True, null=True)
    section = models.IntegerField(blank=True, null=True)
    course = models.PositiveIntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    cw = models.TextField(blank=True, null=True)
    hw = models.TextField(blank=True, null=True)
    plan_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_section_plans'


class StudySections(models.Model):
    is_package = models.IntegerField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    allow_comments = models.IntegerField()
    is_online = models.IntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    section_no = models.CharField(max_length=100, blank=True, null=True)
    term = models.PositiveIntegerField(blank=True, null=True)
    course = models.PositiveIntegerField(blank=True, null=True)
    college = models.IntegerField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    program = models.IntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    room = models.PositiveIntegerField(blank=True, null=True)
    teacher = models.PositiveIntegerField(blank=True, null=True)
    gender = models.PositiveIntegerField(blank=True, null=True)
    max_students = models.PositiveIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    term_lessons = models.IntegerField()
    shared_exams = models.IntegerField(blank=True, null=True)
    questions_bank = models.IntegerField()
    logo_path = models.CharField(max_length=255, blank=True, null=True)
    display_main = models.IntegerField()
    status = models.IntegerField()
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_sections'


class StudySectionsAlternatives(models.Model):
    section = models.PositiveIntegerField(blank=True, null=True)
    teacher = models.PositiveIntegerField(blank=True, null=True)
    section_date = models.DateField(blank=True, null=True)
    section_order = models.IntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_sections_alternatives'


class StudySectionsCategories(models.Model):
    college = models.PositiveIntegerField(blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_sections_categories'


class StudySectionsChapters(models.Model):
    term = models.IntegerField(blank=True, null=True)
    section_id = models.PositiveIntegerField(blank=True, null=True)
    course = models.IntegerField(blank=True, null=True)
    chapter_order = models.IntegerField(blank=True, null=True)
    sessions_count = models.IntegerField(blank=True, null=True)
    is_completed = models.IntegerField(blank=True, null=True)
    teacher = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_sections_chapters'


class StudySectionsComments(models.Model):
    parent = models.IntegerField(blank=True, null=True)
    section = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    upload_files = models.TextField(blank=True, null=True)
    upload_videos = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_sections_comments'


class StudySectionsCommentsInteractions(models.Model):
    comment = models.IntegerField(blank=True, null=True)
    seen = models.IntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_sections_comments_interactions'


class StudySectionsDates(models.Model):
    section = models.PositiveIntegerField(blank=True, null=True)
    type = models.IntegerField()
    section_order = models.IntegerField(blank=True, null=True)
    day = models.CharField(max_length=20, blank=True, null=True)
    start = models.TimeField(blank=True, null=True)
    end = models.TimeField(blank=True, null=True)
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'study_sections_dates'


class StudySectionsDescriptions(models.Model):
    type = models.IntegerField()
    section = models.PositiveIntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    desc_ar = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_sections_descriptions'


class StudySectionsLessons(models.Model):
    chapter_id = models.PositiveIntegerField(blank=True, null=True)
    lesson_order = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_sections_lessons'


class StudySectionsRatingRanges(models.Model):
    rating = models.PositiveIntegerField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_sections_rating_ranges'


class StudySectionsRatings(models.Model):
    target = models.IntegerField()
    term = models.IntegerField(blank=True, null=True)
    college = models.PositiveIntegerField(blank=True, null=True)
    major = models.PositiveIntegerField(blank=True, null=True)
    program = models.PositiveIntegerField(blank=True, null=True)
    plan = models.PositiveIntegerField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    training_course = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    question = models.CharField(max_length=255, blank=True, null=True)
    answer_type = models.IntegerField(blank=True, null=True)
    display_to_parent = models.IntegerField(blank=True, null=True)
    show_participates = models.IntegerField(blank=True, null=True)
    show_infractions = models.IntegerField(blank=True, null=True)
    show_notes = models.IntegerField(blank=True, null=True)
    show_absents = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_sections_ratings'


class StudySectionsRatingsCategories(models.Model):
    college = models.PositiveIntegerField(blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_sections_ratings_categories'


class StudySectionsSettings(models.Model):
    college = models.IntegerField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    program = models.IntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    classes = models.CharField(max_length=200, blank=True, null=True)
    allow_comments = models.IntegerField()
    shared_exams = models.IntegerField(blank=True, null=True)
    term_lessons = models.IntegerField()
    questions_bank = models.IntegerField()
    first_session_start = models.TimeField(blank=True, null=True)
    session_duration = models.TimeField(blank=True, null=True)
    virtual_class_duration = models.TimeField()
    break_name = models.CharField(max_length=255, blank=True, null=True)
    break_teacher = models.IntegerField(blank=True, null=True)
    break_duration = models.TimeField(blank=True, null=True)
    break_start = models.IntegerField()
    break_name_2 = models.CharField(max_length=255)
    break_teacher_2 = models.IntegerField(blank=True, null=True)
    break_duration_2 = models.TimeField(blank=True, null=True)
    break_start_2 = models.IntegerField(blank=True, null=True)
    break_name_3 = models.CharField(max_length=255, blank=True, null=True)
    break_teacher_3 = models.IntegerField(blank=True, null=True)
    break_duration_3 = models.TimeField(blank=True, null=True)
    break_start_3 = models.IntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_sections_settings'


class StudySectionsShares(models.Model):
    section = models.PositiveIntegerField(blank=True, null=True)
    teacher_from = models.PositiveIntegerField(blank=True, null=True)
    course_from = models.PositiveIntegerField(blank=True, null=True)
    plan_from = models.IntegerField(blank=True, null=True)
    teacher_to = models.PositiveIntegerField()
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_sections_shares'


class StudyTerms(models.Model):
    college = models.IntegerField(blank=True, null=True)
    academicyear = models.PositiveIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    course_ratio = models.IntegerField(blank=True, null=True)
    custom_course_ratio = models.IntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    must_exceed_min_limit_for_required_exams = models.IntegerField()
    must_exceed_min_limit_for_courses = models.IntegerField()
    min_hours = models.PositiveIntegerField(blank=True, null=True)
    max_hours = models.PositiveIntegerField(blank=True, null=True)
    beginning_term = models.DateField(blank=True, null=True)
    end_term = models.DateField(blank=True, null=True)
    reg_date_start = models.DateField(blank=True, null=True)
    reg_date_end = models.DateField(blank=True, null=True)
    fine_reg_date_start = models.DateField(blank=True, null=True)
    fine_reg_date_end = models.DateField(blank=True, null=True)
    drag_add_date_start = models.DateField(blank=True, null=True)
    drag_add_date_end = models.DateField(blank=True, null=True)
    create_sections = models.IntegerField(blank=True, null=True)
    create_exams = models.IntegerField(blank=True, null=True)
    create_exam_approvals = models.IntegerField(blank=True, null=True)
    create_committees = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_terms'


class StudyTermsDegreeHours(models.Model):
    term = models.PositiveIntegerField(blank=True, null=True)
    degree = models.PositiveIntegerField(blank=True, null=True)
    min_hours = models.PositiveIntegerField(blank=True, null=True)
    max_hours = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_terms_degree_hours'


class StudyTermsPlans(models.Model):
    term = models.PositiveIntegerField()
    plan = models.IntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_terms_plans'


class StudyTypes(models.Model):
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    only_exceed_max_hours = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_types'


class StudyUniversities(models.Model):
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    desc_ar = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_universities'


class Tags(models.Model):
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


class Tasks(models.Model):
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    explain = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasks'


class TasksUsersRelations(models.Model):
    task_id = models.PositiveIntegerField(blank=True, null=True)
    user_id = models.PositiveIntegerField(blank=True, null=True)
    done = models.PositiveIntegerField(blank=True, null=True)
    done_attachment = models.CharField(max_length=255, blank=True, null=True)
    not_done = models.PositiveIntegerField(blank=True, null=True)
    reason_for_not_doing = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasks_users_relations'


class TrainersAppApprovalAnswers(models.Model):
    app_exam = models.PositiveIntegerField(blank=True, null=True)
    question = models.PositiveIntegerField(blank=True, null=True)
    answer = models.PositiveIntegerField(blank=True, null=True)
    matched_answer = models.IntegerField(blank=True, null=True)
    student_answer = models.IntegerField(blank=True, null=True)
    answer_order = models.IntegerField(blank=True, null=True)
    answer_description = models.TextField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    mark = models.FloatField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_app_approval_answers'


class TrainersAppApprovalExams(models.Model):
    app_type = models.IntegerField(blank=True, null=True)
    exam = models.IntegerField(blank=True, null=True)
    application_id = models.PositiveIntegerField(blank=True, null=True)
    approval_id = models.PositiveIntegerField(blank=True, null=True)
    is_saved = models.IntegerField(blank=True, null=True)
    mark = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    start_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_app_approval_exams'


class TrainersApplications(models.Model):
    user_id = models.PositiveIntegerField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    user_password = models.CharField(max_length=50, blank=True, null=True)
    app_status = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    app_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    app_password = models.CharField(max_length=50, blank=True, null=True)
    name_first_en = models.CharField(max_length=255, blank=True, null=True)
    name_father_en = models.CharField(max_length=255, blank=True, null=True)
    name_grandfather_en = models.CharField(max_length=255, blank=True, null=True)
    name_last_en = models.CharField(max_length=255, blank=True, null=True)
    name_first_ar = models.CharField(max_length=255, blank=True, null=True)
    name_father_ar = models.CharField(max_length=255, blank=True, null=True)
    name_grandfather_ar = models.CharField(max_length=255, blank=True, null=True)
    name_last_ar = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_birth_higri = models.CharField(max_length=30, blank=True, null=True)
    nationality = models.PositiveIntegerField(blank=True, null=True)
    id_no = models.CharField(max_length=50, blank=True, null=True)
    id_copy = models.CharField(max_length=255, blank=True, null=True)
    cv_file = models.CharField(max_length=255, blank=True, null=True)
    id_expiry_date = models.DateField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    religion = models.PositiveIntegerField(blank=True, null=True)
    gender = models.PositiveIntegerField(blank=True, null=True)
    passport_number = models.CharField(max_length=50, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    device = models.CharField(max_length=255, blank=True, null=True)
    os = models.CharField(max_length=255, blank=True, null=True)
    browser = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    approved_by = models.PositiveIntegerField(blank=True, null=True)
    rejected_date = models.DateTimeField(blank=True, null=True)
    rejected_by = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_applications'


class TrainersApplicationsApprovals(models.Model):
    order = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    app_id = models.PositiveIntegerField(blank=True, null=True)
    department = models.PositiveIntegerField(blank=True, null=True)
    interview_date = models.DateTimeField(blank=True, null=True)
    interview_place = models.TextField(blank=True, null=True)
    has_exam = models.PositiveIntegerField(blank=True, null=True)
    replied_date = models.DateTimeField(blank=True, null=True)
    replied_by = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_applications_approvals'


class TrainersApplicationsCertificates(models.Model):
    application_id = models.PositiveIntegerField(blank=True, null=True)
    college_name = models.CharField(max_length=255, blank=True, null=True)
    certificate_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    period_in_days = models.PositiveIntegerField(blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    country = models.PositiveIntegerField(blank=True, null=True)
    attachment_file = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_applications_certificates'


class TrainersApplicationsQualifications(models.Model):
    application_id = models.PositiveIntegerField(blank=True, null=True)
    country = models.PositiveIntegerField(blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    graduation_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    degree = models.CharField(max_length=255, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    attachment_file = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_applications_qualifications'


class TrainersApprovals(models.Model):
    university = models.IntegerField(blank=True, null=True)
    college = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    related_id = models.IntegerField(blank=True, null=True)
    order = models.PositiveIntegerField()
    department = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_approvals'


class TrainersCourses(models.Model):
    parent = models.IntegerField(blank=True, null=True)
    app_status = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    trainer = models.PositiveIntegerField(blank=True, null=True)
    course_type_id = models.PositiveIntegerField(blank=True, null=True)
    is_local = models.PositiveIntegerField(blank=True, null=True)
    allow_comments = models.IntegerField()
    allow_assessment = models.IntegerField()
    multi_assignment_fill = models.IntegerField()
    for_student = models.IntegerField(blank=True, null=True)
    is_online = models.PositiveIntegerField(blank=True, null=True)
    is_approved = models.PositiveIntegerField(blank=True, null=True)
    program = models.PositiveIntegerField(blank=True, null=True)
    college = models.IntegerField(blank=True, null=True)
    major = models.PositiveIntegerField(blank=True, null=True)
    plan = models.PositiveIntegerField(blank=True, null=True)
    level = models.PositiveIntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    desc_ar = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    is_free = models.IntegerField()
    cost = models.PositiveIntegerField(blank=True, null=True)
    is_price_for_course = models.IntegerField(blank=True, null=True)
    currency = models.IntegerField(blank=True, null=True)
    discount = models.PositiveIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    course_place = models.CharField(max_length=255, blank=True, null=True)
    max_students = models.IntegerField(blank=True, null=True)
    no_of_lectures = models.PositiveIntegerField(blank=True, null=True)
    logo_path = models.CharField(max_length=255, blank=True, null=True)
    video_path = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    approved_by = models.PositiveIntegerField(blank=True, null=True)
    rejected_date = models.DateTimeField(blank=True, null=True)
    rejected_by = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_courses'


class TrainersCoursesApprovals(models.Model):
    order = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    trainer_course_id = models.PositiveIntegerField(blank=True, null=True)
    department = models.PositiveIntegerField(blank=True, null=True)
    replied_date = models.DateTimeField(blank=True, null=True)
    replied_by = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_courses_approvals'


class TrainersCoursesApprovalsCycle(models.Model):
    order = models.PositiveIntegerField()
    department = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_courses_approvals_cycle'


class TrainersCoursesDates(models.Model):
    trainer_course_id = models.PositiveIntegerField(blank=True, null=True)
    day = models.CharField(max_length=20, blank=True, null=True)
    start = models.TimeField(blank=True, null=True)
    end = models.TimeField(blank=True, null=True)
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trainers_courses_dates'


class TrainersCoursesDescriptions(models.Model):
    trainers_course_id = models.PositiveIntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    desc_ar = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_courses_descriptions'


class TrainersCoursesRelated(models.Model):
    trainers_course_id = models.IntegerField(blank=True, null=True)
    related = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_courses_related'


class TrainersCoursesTypes(models.Model):
    major = models.PositiveIntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    desc_ar = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_courses_types'


class TrainersExamParts(models.Model):
    app_exam_id = models.PositiveIntegerField(blank=True, null=True)
    locale = models.IntegerField(blank=True, null=True)
    question_type = models.PositiveIntegerField(blank=True, null=True)
    total_score = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_exam_parts'


class TrainersExamQuestions(models.Model):
    app_exam_id = models.PositiveIntegerField(blank=True, null=True)
    part_id = models.PositiveIntegerField(blank=True, null=True)
    question_id = models.PositiveIntegerField(blank=True, null=True)
    answer_id = models.IntegerField(blank=True, null=True)
    student_answer = models.IntegerField(blank=True, null=True)
    answer_description = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_exam_questions'


class TrainersExams(models.Model):
    app_type = models.IntegerField(blank=True, null=True)
    display_result = models.IntegerField()
    college = models.PositiveIntegerField(blank=True, null=True)
    major = models.PositiveIntegerField(blank=True, null=True)
    program = models.PositiveIntegerField(blank=True, null=True)
    plan = models.PositiveIntegerField(blank=True, null=True)
    teacher = models.PositiveIntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    locale = models.IntegerField()
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_exams'


class TrainersMajors(models.Model):
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    desc_ar = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_majors'


class TrainersTraineeApplications(models.Model):
    user_id = models.PositiveIntegerField(blank=True, null=True)
    user_password = models.CharField(max_length=50, blank=True, null=True)
    app_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    app_password = models.CharField(max_length=50, blank=True, null=True)
    name_first_en = models.CharField(max_length=255, blank=True, null=True)
    name_father_en = models.CharField(max_length=255, blank=True, null=True)
    name_grandfather_en = models.CharField(max_length=255, blank=True, null=True)
    name_last_en = models.CharField(max_length=255, blank=True, null=True)
    name_first_ar = models.CharField(max_length=255, blank=True, null=True)
    name_father_ar = models.CharField(max_length=255, blank=True, null=True)
    name_grandfather_ar = models.CharField(max_length=255, blank=True, null=True)
    name_last_ar = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.PositiveIntegerField(blank=True, null=True)
    id_no = models.CharField(max_length=50, blank=True, null=True)
    id_copy = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    gender = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    device = models.CharField(max_length=255, blank=True, null=True)
    os = models.CharField(max_length=255, blank=True, null=True)
    browser = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_trainee_applications'


class TrainersTraineeCourses(models.Model):
    trainee = models.PositiveIntegerField(blank=True, null=True)
    training_course_id = models.PositiveIntegerField(blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    discount_ratio = models.FloatField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_trainee_courses'


class TrainersTraineeCoursesPayments(models.Model):
    id = models.BigAutoField(primary_key=True)
    trainee = models.PositiveIntegerField(blank=True, null=True)
    course = models.PositiveIntegerField(blank=True, null=True)
    op_date = models.DateField(blank=True, null=True)
    cash = models.IntegerField(db_column='Cash', blank=True, null=True)  # Field name made lowercase.
    bank_transfer = models.IntegerField(db_column='Bank_Transfer', blank=True, null=True)  # Field name made lowercase.
    atm = models.IntegerField(db_column='ATM', blank=True, null=True)  # Field name made lowercase.
    cheque = models.IntegerField(db_column='Cheque', blank=True, null=True)  # Field name made lowercase.
    check_bank = models.CharField(max_length=255, blank=True, null=True)
    check_number = models.CharField(max_length=255, blank=True, null=True)
    check_maturity_date = models.DateField(blank=True, null=True)
    transfer_bank = models.IntegerField(blank=True, null=True)
    transfer_date = models.DateTimeField(blank=True, null=True)
    reference_of_transfare = models.CharField(max_length=255, blank=True, null=True)
    name_of_transferor = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainers_trainee_courses_payments'


class Uploadcenter(models.Model):
    show_in_ar = models.PositiveIntegerField(blank=True, null=True)
    show_in_en = models.PositiveIntegerField(blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    title_ar = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.IntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uploadcenter'


class UserEvaluationSettings(models.Model):
    user = models.IntegerField(blank=True, null=True)
    college = models.IntegerField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    program = models.IntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    course = models.IntegerField(blank=True, null=True)
    weekly_logins = models.IntegerField()
    weekly_questions = models.IntegerField()
    weekly_materials = models.IntegerField()
    weekly_sheets = models.IntegerField()
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_evaluation_settings'


class UserLogins(models.Model):
    last_active_date = models.DateTimeField(blank=True, null=True)
    user_id = models.PositiveIntegerField(blank=True, null=True)
    saved_token = models.IntegerField(blank=True, null=True)
    device_token = models.CharField(max_length=50, blank=True, null=True)
    user_os = models.CharField(max_length=255, blank=True, null=True)
    browser = models.CharField(max_length=255, blank=True, null=True)
    user_agent = models.CharField(max_length=127, blank=True, null=True)
    user_ip = models.CharField(max_length=32, blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    logout_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_logins'


class UserLogs(models.Model):
    college = models.IntegerField(blank=True, null=True)
    user_id = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    related_id = models.IntegerField(blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(db_column='Created_at', blank=True, null=True)  # Field name made lowercase.
    user_os = models.CharField(max_length=255, blank=True, null=True)
    browser = models.CharField(max_length=255, blank=True, null=True)
    user_agent = models.CharField(max_length=127, blank=True, null=True)
    user_ip = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_logs'


class UserNotificationsSettings(models.Model):
    user = models.IntegerField(blank=True, null=True)
    note_type = models.IntegerField(blank=True, null=True)
    system_note = models.PositiveIntegerField(blank=True, null=True)
    email = models.PositiveIntegerField(blank=True, null=True)
    sms = models.PositiveIntegerField(blank=True, null=True)
    push = models.PositiveIntegerField(blank=True, null=True)
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_notifications_settings'


class UserPushrTokens(models.Model):
    user_id = models.PositiveIntegerField(blank=True, null=True)
    token_app = models.IntegerField(blank=True, null=True)
    subscriber_id = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    agent = models.CharField(max_length=255, blank=True, null=True)
    browser = models.CharField(max_length=255, blank=True, null=True)
    os = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_pushr_tokens'


class UserTokens(models.Model):
    user_id = models.PositiveIntegerField(blank=True, null=True)
    user_agent = models.CharField(max_length=40, blank=True, null=True)
    token = models.CharField(unique=True, max_length=40, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    created = models.PositiveIntegerField(blank=True, null=True)
    expires = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_tokens'


class Users(models.Model):
    college = models.IntegerField(blank=True, null=True)
    qr_code = models.CharField(max_length=255, blank=True, null=True)
    dark_mode = models.IntegerField()
    show_dashboard = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=127, blank=True, null=True)
    username = models.CharField(unique=True, max_length=32)
    status = models.IntegerField()
    password = models.CharField(max_length=64)
    mobile = models.CharField(max_length=127, blank=True, null=True)
    user_groub = models.PositiveIntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    img_thumb = models.CharField(max_length=255, blank=True, null=True)
    logins = models.PositiveIntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    last_active = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    webpushr_id = models.CharField(max_length=11, blank=True, null=True)
    webpushr_last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersDailyActions(models.Model):
    user = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    action_type = models.PositiveIntegerField(blank=True, null=True)
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_daily_actions'


class UsersFavouriteUrls(models.Model):
    user = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveIntegerField()
    url = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    last_visit = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_favourite_urls'


class UsersFiles(models.Model):
    file_path = models.CharField(max_length=255, blank=True, null=True)
    description_ar = models.CharField(max_length=255, blank=True, null=True)
    description_en = models.CharField(max_length=255, blank=True, null=True)
    date_to_delete = models.DateField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_files'


class UsersGroup(models.Model):
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    shortcut = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_group'


class UsersLastUrls(models.Model):
    user = models.PositiveIntegerField(blank=True, null=True)
    term = models.PositiveIntegerField()
    url = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    details = models.CharField(max_length=255, blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    youtube_link = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    related_id = models.PositiveIntegerField(blank=True, null=True)
    last_visit = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_last_urls'


class UsersLogs(models.Model):
    college = models.IntegerField(blank=True, null=True)
    term = models.IntegerField(blank=True, null=True)
    user = models.PositiveIntegerField(blank=True, null=True)
    section = models.IntegerField(blank=True, null=True)
    note_type = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    details = models.TextField()
    related_id = models.PositiveIntegerField(blank=True, null=True)
    related_meta = models.CharField(max_length=255)
    url = models.TextField(blank=True, null=True)
    icon = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_logs'


class UsersNotifications(models.Model):
    college = models.IntegerField(blank=True, null=True)
    major = models.IntegerField(blank=True, null=True)
    program = models.IntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    user = models.PositiveIntegerField(blank=True, null=True)
    group = models.PositiveIntegerField(blank=True, null=True)
    valid_to = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=255)
    details = models.TextField()
    url = models.TextField(blank=True, null=True)
    icon = models.TextField(blank=True, null=True)
    push_related_id = models.IntegerField(blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_notifications'


class UsersNotificationsAttachments(models.Model):
    user_notification_id = models.PositiveIntegerField(blank=True, null=True)
    file_path = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.PositiveIntegerField(blank=True, null=True)
    deleted_by = models.PositiveIntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_notifications_attachments'


class UsersNotificationsViews(models.Model):
    note_type = models.IntegerField(blank=True, null=True)
    note_id = models.IntegerField(blank=True, null=True)
    user = models.PositiveIntegerField(blank=True, null=True)
    no_of_views = models.PositiveIntegerField(blank=True, null=True)
    ignored_date = models.DateTimeField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_notifications_views'


class Variables(models.Model):
    id = models.BigAutoField(primary_key=True)
    descriptions = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    value_ar = models.CharField(max_length=255, blank=True, null=True)
    value_en = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    text_ar = models.TextField(blank=True, null=True)
    text_en = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variables'


class VclassSections(models.Model):
    class_id = models.IntegerField()
    section_id = models.PositiveIntegerField()
    follower_id = models.PositiveIntegerField()
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vclass_sections'


class VclassroomUrls(models.Model):
    student = models.PositiveIntegerField()
    class_id = models.PositiveIntegerField()
    attendee_url = models.TextField(blank=True, null=True)
    completed = models.IntegerField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vclassroom_urls'


class VirtualClassrooms(models.Model):
    class_type = models.IntegerField(blank=True, null=True)
    teacher = models.PositiveIntegerField()
    section = models.PositiveIntegerField()
    comment = models.IntegerField(blank=True, null=True)
    chapter = models.IntegerField(blank=True, null=True)
    lesson = models.IntegerField(blank=True, null=True)
    class_id = models.CharField(max_length=255)
    attendee_pw = models.CharField(max_length=255, blank=True, null=True)
    moderator_pw = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    attendee_limit = models.PositiveIntegerField(blank=True, null=True)
    is_recorded = models.IntegerField()
    recording_url = models.TextField(blank=True, null=True)
    presenter_url = models.TextField(blank=True, null=True)
    attachment_url = models.CharField(max_length=255, blank=True, null=True)
    completed = models.IntegerField(blank=True, null=True)
    teacher_note = models.TextField(blank=True, null=True)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'virtual_classrooms'


class WiziqAccounts(models.Model):
    user_id = models.PositiveIntegerField()
    account_id = models.PositiveIntegerField()
    email = models.CharField(max_length=127)
    password = models.CharField(max_length=64)
    created_by = models.PositiveIntegerField(db_column='Created_by', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    last_update_by = models.PositiveIntegerField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wiziq_accounts'



# class CustomUser(AbstractUser):
#     ROLE_CHOICES = (
#         ('admin', 'Admin'),
#         ('farmer', 'Farmer'),
#         ('outlet', 'outlet'),
#     )

#     credit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES)
#     two_factor_enabled = models.BooleanField(default=False)


# class UserTOTPDevice(TOTPDevice):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)    

# class FarmerDetail(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     pincode = models.CharField(max_length=10, blank=True, null=True)
#     village = models.CharField(max_length=100, blank=True, null=True)
#     taluk = models.CharField(max_length=100, blank=True, null=True)
#     district = models.CharField(max_length=100, blank=True, null=True)
#     state = models.CharField(max_length=100, blank=True, null=True)
#     country = models.CharField(max_length=100, blank=True, null=True)
#     # Add other relevant fields


# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='category_images/', null=True, blank=True)
#     description = models.TextField(blank=True)
#     def __str__(self):
#         return self.name



# class AgriProduct(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
#     crop_name = models.CharField(max_length=100)
#     actual_production = models.DecimalField(max_digits=10, decimal_places=2)
#     project_production = models.DecimalField(max_digits=10, decimal_places=2)
#     projection_timeline = models.DecimalField(max_digits=10, decimal_places=2)
#     cultivation_land_value = models.DecimalField(max_digits=10, decimal_places=2)
#     cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
#     project_cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='agri_product_images/', null=True, blank=True)

#     def __str__(self):
#         return f"{self.crop_name} by {self.user.username}"


# class AgriAsset(models.Model):
#     # Fields
#     land_owner = models.CharField(max_length=255)
#     land_location = models.CharField(max_length=255)
#     google_map_location = models.URLField(max_length=500, blank=True, null=True)
#     width = models.FloatField()
#     length = models.FloatField()
#     size = models.FloatField()

#     # Choices for cultivation_method
#     NANCHAI = 'Nanchai'
#     PUNCHAI = 'Punchai'
#     CULTIVATION_METHOD_CHOICES = [
#         (NANCHAI, 'Nanchai'),
#         (PUNCHAI, 'Punchai'),
#     ]
#     cultivation_method = models.CharField(
#         max_length=10,
#         choices=CULTIVATION_METHOD_CHOICES,
#         default=NANCHAI,
#     )

#     # Choices for owner_type
#     OWN = 'own'
#     LEASE = 'lease'
#     OWNER_TYPE_CHOICES = [
#         (OWN, 'Own'),
#         (LEASE, 'Lease'),
#     ]
#     owner_type = models.CharField(
#         max_length=5,
#         choices=OWNER_TYPE_CHOICES,
#         default=OWN,
#     )

#     def __str__(self):
#         return f"{self.land_owner} - {self.land_location}"
    



# class Contact(models.Model):
#     # Fields
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=15)
#     email = models.EmailField()
#     referral = models.CharField(max_length=255, blank=True, null=True)
    
    
    
def __str__(self):
        return self.name

