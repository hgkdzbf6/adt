# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class SystemImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField(upload_to='upload')

    class Meta:
        managed = False
        db_table = 'system_image'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class IndexIndex(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'index_index'


class QueryQuery(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'query_query'


class SystemAuth(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=20)
    status = models.IntegerField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    create_by = models.BigIntegerField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_auth'


class SystemCategory(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    category = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'system_category'


class SystemClause(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    clause = models.CharField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'system_clause'


class SystemCommonSensitiveWords(models.Model):
    id = models.BigAutoField(primary_key=True)
    word = models.CharField(max_length=30)
    advice_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'system_common_sensitive_words'
        unique_together = (('id', 'word'),)


class SystemDistrict(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    district = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'system_district'


class SystemLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip = models.CharField(max_length=15)
    node = models.CharField(max_length=200)
    username = models.CharField(max_length=32)
    action = models.CharField(max_length=200)
    content = models.TextField()
    create_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'system_log'


class SystemMenu(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField()
    title = models.CharField(max_length=100)
    node = models.CharField(max_length=200)
    icon = models.CharField(max_length=100)
    url = models.CharField(max_length=400)
    params = models.CharField(max_length=500, blank=True, null=True)
    target = models.CharField(max_length=20)
    sort = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    create_by = models.BigIntegerField()
    create_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_menu'


class SystemOtherSensitiveWords(models.Model):
    id = models.BigAutoField(primary_key=True)
    district_id = models.SmallIntegerField()
    category_id = models.SmallIntegerField()
    word = models.CharField(max_length=30)
    advice_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'system_other_sensitive_words'
        unique_together = (('id', 'word'),)


class SystemUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=32)
    qq = models.CharField(max_length=16, blank=True, null=True)
    mail = models.CharField(max_length=32, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    login_num = models.BigIntegerField(blank=True, null=True)
    login_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    authorize = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    create_by = models.BigIntegerField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_user'


class SystemUserCharge(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    consume = models.FloatField(blank=True, null=True)
    charge = models.FloatField(blank=True, null=True)
    overage = models.FloatField()
    create_at = models.DateTimeField(blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_user_charge'


class SystemUserSimple(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    phone = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_user_simple'
