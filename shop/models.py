# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bridge(models.Model):
    id_object = models.AutoField(primary_key=True)
    name_object = models.CharField(max_length=45, blank=True, null=True)
    id_classification = models.ForeignKey('Classification', models.DO_NOTHING, db_column='id_classification', blank=True, null=True)
    id_address = models.ForeignKey('River', models.DO_NOTHING, db_column='id_address', blank=True, null=True)
    description = models.CharField(max_length=25, blank=True, null=True)
    photo = models.ImageField(upload_to='products/img/%Y/%m/%d')
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name_object
    class Meta:
        managed = False
        db_table = 'bridge'


class CategoryWork(models.Model):
    id_category = models.AutoField(primary_key=True)
    name_of_work = models.CharField(max_length=20, blank=True, null=True)
    status_cat_work = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_work'


class Classification(models.Model):
    id_classification = models.AutoField(primary_key=True)
    name_classification = models.CharField(max_length=20, blank=True, null=True)
    id_main_classification = models.ForeignKey('self', models.DO_NOTHING, db_column='id_main_classification', blank=True, null=True)
    status_classific = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name_classification
    class Meta:
        managed = False
        db_table = 'classification'


class Contractor(models.Model):
    id_contractor = models.AutoField(primary_key=True)
    name_of_contractor = models.CharField(max_length=20, blank=True, null=True)
    id_entity = models.ForeignKey('Entity', models.DO_NOTHING, db_column='id_entity', blank=True, null=True)
    id_director = models.ForeignKey('User', models.DO_NOTHING, db_column='id_director', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name_of_contractor
    class Meta:
        managed = False
        db_table = 'contractor'


class Country(models.Model):
    id_country = models.AutoField(primary_key=True)
    name_country = models.CharField(max_length=20, blank=True, null=True)
    status_country = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    name_of_customer = models.CharField(max_length=45, blank=True, null=True)
    id_entity = models.ForeignKey('Entity', models.DO_NOTHING, db_column='id_entity', blank=True, null=True)
    id_director = models.ForeignKey('User', models.DO_NOTHING, db_column='id_director', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name_of_customer
    class Meta:
        managed = False
        db_table = 'customer'


class Description(models.Model):
    id_description = models.AutoField(primary_key=True)
    name_descriotion = models.CharField(max_length=45, blank=True, null=True)
    status_desc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'description'


class DescriptionObject(models.Model):
    id_object = models.OneToOneField(Bridge, models.DO_NOTHING, db_column='id_object', primary_key=True)  # The composite primary key (id_object, id_description) found, that is not supported. The first column is selected.
    id_description = models.ForeignKey(Description, models.DO_NOTHING, db_column='id_description')
    value = models.CharField(max_length=20, blank=True, null=True)
    id_unit = models.ForeignKey('Unit', models.DO_NOTHING, db_column='id_unit', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'description_object'
        unique_together = (('id_object', 'id_description'),)


class Entity(models.Model):
    id_entity = models.AutoField(primary_key=True)
    name_of_entity = models.CharField(max_length=3, blank=True, null=True)
    status_entity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity'


class Genders(models.Model):
    id_gender = models.AutoField(primary_key=True)
    name_gender = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genders'


class Position(models.Model):
    id_position = models.AutoField(primary_key=True)
    name_position = models.CharField(max_length=15, blank=True, null=True)
    status_position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'position'


class River(models.Model):
    id_river = models.AutoField(primary_key=True)
    name_river = models.CharField(max_length=20, blank=True, null=True)
    id_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='id_country', blank=True, null=True)
    status_river = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name_river
    class Meta:
        managed = False
        db_table = 'river'


class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    name_status = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name_status
    class Meta:
        managed = False
        db_table = 'status'


class Subcategory(models.Model):
    id_subcategory = models.AutoField(primary_key=True)
    name_of_subcategory = models.CharField(max_length=45, blank=True, null=True)
    id_main_category = models.ForeignKey(CategoryWork, models.DO_NOTHING, db_column='id_main_category', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subcategory'


class Unit(models.Model):
    id_unit = models.AutoField(primary_key=True)
    name_unit = models.CharField(max_length=5, blank=True, null=True)
    status_unit = models.IntegerField(blank=True, null=True)

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
    status = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Work(models.Model):
    id_work = models.OneToOneField('WorkShedue', models.DO_NOTHING, db_column='id_work', primary_key=True)  # The composite primary key (id_work, id_subcategory) found, that is not supported. The first column is selected.
    id_subcategory = models.ForeignKey(Subcategory, models.DO_NOTHING, db_column='id_subcategory')
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
        unique_together = (('id_work', 'id_subcategory'),)


class WorkShedue(models.Model):
    id_work_shedue = models.AutoField(primary_key=True)
    id_object = models.ForeignKey(Bridge, models.DO_NOTHING, db_column='id_object', blank=True, null=True)
    id_contractor = models.ForeignKey(Contractor, models.DO_NOTHING, db_column='id_contractor', blank=True, null=True)
    id_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='id_customer', blank=True, null=True)
    date_of_start = models.DateField(blank=True, null=True)
    date_of_end = models.DateField(blank=True, null=True)
    id_status = models.ForeignKey(Status, models.DO_NOTHING, db_column='id_status', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_shedue'
