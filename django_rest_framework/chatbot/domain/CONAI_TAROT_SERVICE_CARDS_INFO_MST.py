# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

def tarot_upload_to(instance, filename):
    return f"tarot/{instance.type}/{instance.deck_name}/{filename}"



class ConaiTarotServiceCardsInfoMst(models.Model):
    conai_tarot_service_cards_info_mst_id = models.UUIDField(primary_key=True, db_comment='Primary key and unique identifier for each tarot card')
    name = models.CharField(max_length=255, db_comment='English name of the tarot card')
    korean_name = models.CharField(max_length=255, blank=True, null=True, db_comment='Korean name of the tarot card')
    card_index = models.IntegerField(unique=True, db_comment='Index of the tarot card within the deck')
    image_url = models.TextField(blank=True, null=True, db_comment='Path to the tarot card image')
    image = models.ImageField(upload_to=tarot_upload_to ,db_comment='Full path for image')
    reference_urls = models.JSONField(blank=True, null=True, db_comment='JSONB field for storing additional reference URLs related to the tarot card')
    deck_name = models.CharField(max_length=255, db_comment='Name of the deck the tarot card belongs to')
    type = models.CharField(max_length=255, db_comment='Type identifier for the front or back')
    version = models.CharField(max_length=50, db_comment='Version identifier for the deck or card')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of record creation')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of last record update')

    # Override delete method
    # def delete(self, *args, **kwargs):
    #     # Delete the file associated with the image field if it exists
    #     if self.image:
    #         self.image.delete(save=False)
    #     # Return the result of the superclass delete method
    #     return super().delete(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'conai_tarot_service_cards_info_mst'
        unique_together = (('name', 'deck_name', 'version', 'card_index'),)
        db_table_comment = 'Table to store tarot card details for Conai Tarot Service'


class ConaiTarotServiceCardsInfoMstMod(models.Model):
    conai_tarot_service_cards_info_mst_id = models.UUIDField(primary_key=True, db_comment='Primary key and unique identifier for each tarot card')
    name = models.CharField(max_length=255, db_comment='English name of the tarot card')
    korean_name = models.CharField(max_length=255, blank=True, null=True, db_comment='Korean name of the tarot card')
    card_index = models.IntegerField(unique=True, db_comment='Index of the tarot card within the deck')
    image_url = models.TextField(blank=True, null=True, db_comment='Path to the tarot card image')
    image = models.ImageField(upload_to=tarot_upload_to ,db_comment='Full path for image')
    reference_urls = models.JSONField(blank=True, null=True, db_comment='JSONB field for storing additional reference URLs related to the tarot card')
    deck_name = models.CharField(max_length=255, db_comment='Name of the deck the tarot card belongs to')
    type = models.CharField(max_length=255, db_comment='Type identifier for the front or back')
    version = models.CharField(max_length=50, db_comment='Version identifier for the deck or card')
    # created_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of record creation')
    # updated_at = models.DateTimeField(blank=True, null=True, db_comment='Timestamp of last record update')

    class Meta:
        managed = False
        db_table = 'conai_tarot_service_cards_info_mst'
        unique_together = (('name', 'deck_name', 'version', 'card_index'),)
        db_table_comment = 'Table to store tarot card details for Conai Tarot Service'
