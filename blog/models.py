from django.db import models


class Post(models.Model):
    RSO = models.CharField(max_length=40)
    Description = models.TextField()
    date = models.DateTimeField()

    class Meta:
        db_table = 'Student_Post'


YESNO = (
    ('YES', 'YES'),
    ('NO', 'NO')
)

FOC = (
    ('SEMESTER', 'SEMESTER'),
    ('1 yr ', '1 yr'),
    ('2 yr', '2 yr'),
    ('3 yr', '3 yr'),
    ('4 yr', '4 yr'),
    ('5 yr', '5 yr'),
    ('6 yr', '6 yr')
)


class Item(models.Model):
    Tag_num = models.CharField(max_length=5, verbose_name='Tag Number', blank=True)
    NOA_num = models.CharField(max_length=100, verbose_name='Aproval Bill Number', blank=True)
    Item_name = models.CharField(max_length=100, verbose_name='Item Name', blank=True)
    Item_des = models.TextField(verbose_name='Item Description', blank=True)
    Manf_name = models.CharField(max_length=100, verbose_name='Manufaturer Name', blank=True)
    Model_num = models.CharField(max_length=100, verbose_name='Model Number', blank=True)
    Ser_num = models.CharField(max_length=100, verbose_name='Serial Number', blank=True)
    Seller_name = models.CharField(max_length=100, verbose_name='Seller Name', blank=True)
    Pur_date = models.DateTimeField(verbose_name='Purchase Date', blank=False, null=False)
    Pur_price = models.CharField(max_length=100, verbose_name='Purchase Price', blank=True)
    Warranty = models.CharField(max_length=100, choices=YESNO, verbose_name='Warranty', blank=True)  # drop down
    War_end_date = models.DateTimeField(max_length=100, verbose_name='Warranty End Date', blank=False, null=True)
    Store_local = models.CharField(max_length=40, verbose_name='Storage Location Name', blank=True)
    Store_add = models.CharField(max_length=40, verbose_name='Storage Location Address', blank=True)
    Store_room = models.CharField(max_length=40, verbose_name='Storage Location Room', blank=True)
    FOC_cat = models.CharField(max_length=100, choices=FOC, verbose_name='FOC Replacement Guidline', blank=True)

    def __str__(self):
        return self.Tag_num

    class Meta:
        db_table = 'items'


class RSO(models.Model):
    RSO_name = models.CharField(max_length=40, verbose_name='RSO Name', blank=True)
    RSO_prez = models.CharField(max_length=40, verbose_name='RSO President', blank=True)
    Prez_ph = models.CharField(max_length=12, verbose_name='President Phone Number', blank=True)
    Prez_email = models.CharField(max_length=40, verbose_name='President Email', blank=True)
    RSO_advisor = models.CharField(max_length=40, verbose_name='RSO Advisor', blank=True)
    Advisor_ph = models.CharField(max_length=11, verbose_name='Advisor Phone Number', blank=True)
    Advisor_email = models.CharField(max_length=40, verbose_name='Advisor Email', blank=True)

    def __str__(self):
        return self.RSO_name

    class Meta:
        db_table = 'RSO'


COND = (
    ('NEW', 'NEW'),
    ('LIKE NEW', 'LIKE NEW'),
    ('GOOD', 'GOOD'),
    ('FAIR', 'FAIR'),
    ('POOR', 'POOR'),
    ('UNUSABLE', 'UNUSABLE'),
    ('LOST', 'LOST'),
    ('LOST', 'LOST'),
    ('LOST', 'LOST'),
)


class Inventory_Check(models.Model):
    Tag_num = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True)
    RSO_name = models.ForeignKey(RSO, on_delete=models.CASCADE, blank=True)
    Curr_date = models.DateTimeField(verbose_name='Current Date', blank=True)
    Condition = models.CharField(max_length=100, choices=COND, verbose_name='Condition', blank=True)
    Retire_Date = models.DateTimeField(verbose_name='Retire Date', blank=True)
    Ck_Notes = models.TextField(verbose_name='Item Notes', blank=True)

    class Meta:
        db_table = 'inventory_check'


def __str__(self):
    return self.PrimaryKey
