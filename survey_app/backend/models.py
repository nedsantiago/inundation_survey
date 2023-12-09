import uuid
from django.db import models

# Create your models here.
class Survey(models.Model):
    """A classs that encapsulates a survey instance:
    a unique combination of address/location, and respondent"""

    # fields
    survey_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    survey_address = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    interviewer_name = models.CharField(max_length=100, blank=True, null=True)
    survey_date = models.DateField(blank=True, null=True)
    respondent_age = models.IntegerField(blank=True, null=True)
    respondent_name = models.CharField(max_length=100, blank=True, null=True)
    respondent_tenure = models.IntegerField(blank=True, null=True)
    respondent_education = models.CharField(max_length=100, blank=True, null=True)
    respondent_residency_type = models.CharField(max_length=100, blank=True, null=True)
    respondent_occupation = models.CharField(max_length=100, blank=True, null=True)
    respondent_civil_status = models.CharField(max_length=100, blank=True, null=True)
    respondent_ethnicity = models.CharField(max_length=100, blank=True, null=True)
    respondent_religion = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    # string to represent model
    def __str__(self):
        return f"{self.respondent_name} at {self.survey_address}"

class StormExperienced(models.Model):
    """A class that enccapsulates a storm experience instance"""

    # fields
    storm_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    storm_name = models.CharField(max_length=100, blank=True, null=True)
    survey_encode_datetime = models.DateTimeField(blank=True, null=True)
    encoder_email_ad = models.EmailField(blank=True, null=True)
    storm_duration = models.FloatField(blank=True, null=True)
    storm_originate = models.CharField(max_length=100, blank=True, null=True)
    storm_warning = models.CharField(max_length=100, blank=True, null=True)
    storm_did_evacuate = models.CharField(max_length=100, blank=True, null=True)
    storm_evacuate_loc = models.CharField(max_length=100, blank=True, null=True)
    storm_evacuate_floodtime = models.CharField(max_length=100, blank=True, null=True)
    storm_transpo = models.CharField(max_length=100, blank=True, null=True)
    storm_disease = models.CharField(max_length=100, blank=True, null=True)
    storm_loss = models.CharField(max_length=100, blank=True, null=True)
    storm_work_school = models.CharField(max_length=100, blank=True, null=True)
    storm_days_no_ws = models.IntegerField(blank=True, null=True)
    storm_walkability = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    survey_details = models.ForeignKey('Survey', on_delete=models.RESTRICT, null=True)

    # string to represent model
    def __str__(self):
        return f"{self.name} as lived by {self.survey_details}"