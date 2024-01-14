from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StartupProgress(models.Model):
    Applicant_id=models.ForeignKey(User, on_delete=models.CASCADE)
    Registered_Startup=models.BooleanField(default=True)
    StartupIndia_Program=models.BooleanField(default=False)
    Program_Proof=models.ImageField(upload_to="Registration Proof",blank=True)
    CompletedStartupIndia_Program=models.BooleanField(default=False)
    Completion_Proof=models.ImageField(upload_to="Completion Certificates",blank=True)
    Application_Status=models.BooleanField(default=False)
    Application_StatusProof=models.ImageField(upload_to="Application Statuses",blank=True)
    StartupTest_Email=models.BooleanField(default=False)
    StartupTest_Appeared=models.BooleanField(default=False)
    Presentation_Email=models.BooleanField(default=False)
    Presentation_Appeared=models.BooleanField(default=False)
    Fund_Confirmed=models.BooleanField(default=False)
    CompanyRegistrationApplied=models.BooleanField(default=False)
    SeedFund_Received=models.BooleanField(default=False)
    
    def __str__(self):
        return self.Applicant_id.Name
    class Meta:
        db_table="Startups_Progress_Report"
