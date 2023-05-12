# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class CategoryWork(models.Model):
    id_category = models.AutoField(primary_key=True)
    name_of_work = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_work'


class Classification(models.Model):
    id_classification = models.AutoField(primary_key=True)
    name_classification = models.CharField(max_length=20, blank=True, null=True)
    id_main_classification = models.ForeignKey('self', models.DO_NOTHING, db_column='id_main_classification', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classification'


class Contractor(models.Model):
    id_contractor = models.AutoField(primary_key=True)
    name_of_contractor = models.CharField(max_length=20, blank=True, null=True)
    id_entity = models.ForeignKey('Entity', models.DO_NOTHING, db_column='id_entity', blank=True, null=True)
    id_director = models.ForeignKey('User', models.DO_NOTHING, db_column='id_director', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contractor'


class Country(models.Model):
    id_country = models.AutoField(primary_key=True)
    name_country = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    name_of_customer = models.CharField(max_length=45, blank=True, null=True)
    id_entity = models.ForeignKey('Entity', models.DO_NOTHING, db_column='id_entity', blank=True, null=True)
    id_director = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Description(models.Model):
    id_description = models.AutoField(primary_key=True)
    name_descriotion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'description'


class DescriptionObject(models.Model):
    id_object = models.OneToOneField('Object', models.DO_NOTHING, db_column='id_object', primary_key=True)
    id_description = models.ForeignKey(Description, models.DO_NOTHING, db_column='id_description', blank=True, null=True)
    value = models.CharField(max_length=20, blank=True, null=True)
    id_unit = models.ForeignKey('Unit', models.DO_NOTHING, db_column='id_unit', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'description_object'


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


class Entity(models.Model):
    id_entity = models.AutoField(primary_key=True)
    name_of_entity = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity'


class Genders(models.Model):
    id_gender = models.AutoField(primary_key=True)
    name_gender = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genders'


class Object(models.Model):
    id_object = models.AutoField(primary_key=True)
    name_object = models.CharField(max_length=45, blank=True, null=True)
    id_classification = models.ForeignKey(Classification, models.DO_NOTHING, db_column='id_classification', blank=True, null=True)
    id_address = models.ForeignKey('River', models.DO_NOTHING, db_column='id_address', blank=True, null=True)
    description = models.CharField(max_length=25, blank=True, null=True)
    photo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'object'


class Position(models.Model):
    id_position = models.AutoField(primary_key=True)
    name_position = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'position'


class River(models.Model):
    id_river = models.AutoField(primary_key=True)
    name_river = models.CharField(max_length=20, blank=True, null=True)
    id_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='id_country', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'river'


class ShopOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=32)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    creation_time = models.DateTimeField()
    comment = models.TextField(blank=True, null=True)
    payment = models.ForeignKey('ShopPayment', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shop_order'


class ShopOrderitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    discount = models.DecimalField(max_digits=20, decimal_places=2)
    order = models.ForeignKey(ShopOrder, models.DO_NOTHING)
    product = models.ForeignKey('ShopProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shop_orderitem'


class ShopPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    time = models.DateTimeField()
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shop_payment'


class ShopProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    unit = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.CharField(max_length=200, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_product'


class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    name_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'


class Subcategory(models.Model):
    id_subcategory = models.AutoField(primary_key=True)
    name_of_subcategory = models.CharField(max_length=45, blank=True, null=True)
    id_main_category = models.ForeignKey('self', models.DO_NOTHING, db_column='id_main_category', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subcategory'


class Unit(models.Model):
    id_unit = models.AutoField(primary_key=True)
    name_unit = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unit'


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    second_name = models.CharField(max_length=20, blank=True, null=True)
    date_of_berth = models.DateField(blank=True, null=True)
    telephone = models.CharField(max_length=11, blank=True, null=True)
    login = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    id_position = models.ForeignKey(Position, models.DO_NOTHING, db_column='id_position', blank=True, null=True)
    id_gender = models.ForeignKey(Genders, models.DO_NOTHING, db_column='id_gender', blank=True, null=True)
    id_status = models.ForeignKey(Status, models.DO_NOTHING, db_column='id_status', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Work(models.Model):
    id_work = models.AutoField(primary_key=True)
    id_subcategory = models.ForeignKey(Subcategory, models.DO_NOTHING, db_column='id_subcategory', blank=True, null=True)
    date_of_start = models.DateField(blank=True, null=True)
    date_of_end = models.DateField(blank=True, null=True)
    count_people = models.IntegerField(blank=True, null=True)
    count_day = models.IntegerField(blank=True, null=True)
    id_unit = models.ForeignKey(Unit, models.DO_NOTHING, db_column='id_unit', blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    id_status = models.ForeignKey(Status, models.DO_NOTHING, db_column='id_status', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work'


class WorkShedue(models.Model):
    id_work_shedue = models.AutoField(primary_key=True)
    id_object = models.ForeignKey(Object, models.DO_NOTHING, db_column='id_object', blank=True, null=True)
    id_contractor = models.ForeignKey(Contractor, models.DO_NOTHING, db_column='id_contractor', blank=True, null=True)
    id_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='id_customer', blank=True, null=True)
    date_of_start = models.DateField(blank=True, null=True)
    date_of_end = models.DateField(blank=True, null=True)
    id_status = models.ForeignKey(Status, models.DO_NOTHING, db_column='id_status', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_shedue'
