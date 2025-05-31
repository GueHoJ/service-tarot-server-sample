# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ConaiUserMst(models.Model):
    conai_user_mst_id = models.UUIDField(primary_key=True, db_comment='코나이유저마스터 고유 아이디')
    user_id = models.CharField(max_length=100, db_comment='사용자 아이디')
    user_name = models.CharField(max_length=100, db_comment='사용자 이름')
    user_phone_number = models.IntegerField(blank=True, null=True, db_comment='사용자 전화번호')

    class Meta:
        managed = False
        db_table = 'conai_user_mst'


class ConaiUserMstMod(models.Model):
    conai_user_mst_id = models.UUIDField(primary_key=True, db_comment='코나이유저마스터 고유 아이디')
    user_id = models.CharField(max_length=100, db_comment='사용자 아이디')
    user_name = models.CharField(max_length=100, db_comment='사용자 이름')
    user_phone_number = models.IntegerField(blank=True, null=True, db_comment='사용자 전화번호')

    class Meta:
        managed = False
        db_table = 'conai_user_mst'