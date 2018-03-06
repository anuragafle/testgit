# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Authority(models.Model):
    name = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'authority'


class OauthAccessToken(models.Model):
    token_id = models.CharField(max_length=256, blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    authentication_id = models.CharField(max_length=256, blank=True, null=True)
    user_name = models.CharField(max_length=256, blank=True, null=True)
    client_id = models.CharField(max_length=256, blank=True, null=True)
    authentication = models.TextField(blank=True, null=True)
    refresh_token = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_access_token'


class OauthRefreshToken(models.Model):
    token_id = models.CharField(max_length=256, blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    authentication = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_refresh_token'


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=500, blank=True, null=True)
    activated = models.IntegerField(blank=True, null=True)
    activationkey = models.CharField(max_length=50, blank=True, null=True)
    resetpasswordkey = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserAuthority(models.Model):
    username = models.ForeignKey(User, models.DO_NOTHING, db_column='username')
    authority = models.ForeignKey(Authority, models.DO_NOTHING, db_column='authority')

    class Meta:
        managed = False
        db_table = 'user_authority'
        unique_together = (('username', 'authority'),)
