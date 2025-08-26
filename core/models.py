# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Access(models.Model):
    access_id = models.AutoField(db_column='ACCESS_ID', primary_key=True)  # Field name made lowercase.
    u = models.ForeignKey('Users', models.DO_NOTHING, db_column='U_ID')  # Field name made lowercase.
    m = models.ForeignKey('Materials', models.DO_NOTHING, db_column='M_ID')  # Field name made lowercase.
    sec = models.ForeignKey('Section', models.DO_NOTHING, db_column='SEC_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'access'


class Announcement(models.Model):
    a_id = models.AutoField(db_column='A_ID', primary_key=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT')  # Field name made lowercase.
    time = models.DateTimeField(db_column='TIME')  # Field name made lowercase.
    t_id = models.IntegerField(db_column='T_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'announcement'


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


class Courses(models.Model):
    c_id = models.AutoField(db_column='C_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=20)  # Field name made lowercase.
    c_code = models.CharField(db_column='C_CODE', max_length=6)  # Field name made lowercase.
    credits = models.IntegerField(db_column='CREDITS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'courses'


class Consultation(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name="student_consultations", 
        on_delete=models.CASCADE
    )
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name="teacher_consultations", 
        on_delete=models.CASCADE
    )
    topic = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consultation: {self.student} → {self.teacher}"





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


class Enrollment(models.Model):
    enroll_id = models.AutoField(db_column='ENROLL_ID', primary_key=True)  # Field name made lowercase.
    sec = models.ForeignKey('Section', models.DO_NOTHING, db_column='SEC_ID')  # Field name made lowercase.
    u = models.ForeignKey('Users', models.DO_NOTHING, db_column='U_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'enrollment'


class Form(models.Model):
    f_id = models.AutoField(db_column='F_ID', primary_key=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION')  # Field name made lowercase.
    date = models.DateField(db_column='DATE')  # Field name made lowercase.
    s_id = models.IntegerField(db_column='S_ID')  # Field name made lowercase.
    g = models.ForeignKey('Gradesheet', models.DO_NOTHING, db_column='G_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form'


class Gradesheet(models.Model):
    g_id = models.AutoField(db_column='G_ID', primary_key=True)  # Field name made lowercase.
    grade = models.TextField(db_column='GRADE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gradesheet'


class Materials(models.Model):
    m_id = models.AutoField(db_column='M_ID', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='TITLE')  # Field name made lowercase.
    p = models.ForeignKey('self', models.DO_NOTHING, db_column='P_ID')  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=9)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50)  # Field name made lowercase.
    url = models.TextField(db_column='URL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'materials'


class Receive(models.Model):
    receive_id = models.AutoField(db_column='RECEIVE_ID', primary_key=True)  # Field name made lowercase.
    s_id = models.IntegerField(db_column='S_ID')  # Field name made lowercase.
    a = models.ForeignKey(Announcement, models.DO_NOTHING, db_column='A_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'receive'


class Section(models.Model):
    sec_id = models.AutoField(db_column='SEC_ID', primary_key=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='NUMBER')  # Field name made lowercase.
    room = models.CharField(db_column='ROOM', max_length=10)  # Field name made lowercase.
    time = models.DateTimeField(db_column='TIME')  # Field name made lowercase.
    c = models.ForeignKey(Courses, models.DO_NOTHING, db_column='C_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'section'


class Upload(models.Model):
    up_id = models.AutoField(db_column='UP_ID', primary_key=True)  # Field name made lowercase.
    s_id = models.IntegerField(db_column='S_ID')  # Field name made lowercase.
    m = models.ForeignKey(Materials, models.DO_NOTHING, db_column='M_ID')  # Field name made lowercase.
    g = models.ForeignKey(Gradesheet, models.DO_NOTHING, db_column='G_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'upload'


class UsersManager(BaseUserManager):
    def create_user(self, gmail, password=None, **extra_fields):
        if not gmail:
            raise ValueError("The Gmail field must be set")
        user = self.model(gmail=gmail, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, gmail, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(gmail, password, **extra_fields)

class Users(models.Model):
    u_id = models.AutoField(db_column='U_ID', primary_key=True)
    fname = models.CharField(db_column='FNAME', max_length=20)
    mname = models.CharField(db_column='MNAME', max_length=20, blank=True, null=True)
    lname = models.CharField(db_column='LNAME', max_length=20)
    password = models.TextField(db_column='PASSWORD')
    dept = models.CharField(db_column='DEPT', max_length=3)
    type = models.IntegerField(db_column='TYPE')
    s_id = models.IntegerField(db_column='S_ID', blank=True, null=True)
    gsuite = models.TextField(db_column='GSUITE', blank=True, null=True)
    t_id = models.IntegerField(db_column='T_ID', blank=True, null=True)
    gmail = models.TextField(db_column='GMAIL', blank=True, null=True)
    designation = models.CharField(db_column='DESIGNATION', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'users'


class View(models.Model):
    view_id = models.AutoField(db_column='VIEW_ID', primary_key=True)  # Field name made lowercase.
    u = models.ForeignKey(Users, models.DO_NOTHING, db_column='U_ID')  # Field name made lowercase.
    g = models.ForeignKey(Gradesheet, models.DO_NOTHING, db_column='G_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'view'


class Visibility(models.Model):
    visi_id = models.AutoField(db_column='VISI_ID', primary_key=True)  # Field name made lowercase.
    t_id = models.IntegerField(db_column='T_ID')  # Field name made lowercase.
    g = models.ForeignKey(Gradesheet, models.DO_NOTHING, db_column='G_ID')  # Field name made lowercase.
    s_id = models.IntegerField(db_column='S_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'visibility'


class Consultation(models.Model):
    student = models.ForeignKey(Users, related_name='student_consultations', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Users, related_name='teacher_consultations', on_delete=models.CASCADE)

    class Meta:
        db_table = 'consultation'

class ConsultationMessage(models.Model):
    consultation = models.ForeignKey(Consultation, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(Users, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'consultation_message'