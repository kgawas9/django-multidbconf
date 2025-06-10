from django.db import models

# Create your models here.
class I3lBotmaster(models.Model):
    taskId = models.UUIDField(primary_key=True, db_column='taskid')
    createdAt = models.DateField(db_column='createdat')
    useCaseName = models.CharField(max_length=200, db_column='usecasename')
    taskName = models.CharField(max_length=500, db_column='taskname')
    department = models.CharField(max_length=200, db_column='department')
    processTrack = models.CharField(max_length=100, db_column='processtrack')
    goLiveAt = models.DateField(null=True, db_column='goliveat')
    updatedAt = models.DateTimeField(null=True, db_column='updatedat')
    isActive = models.CharField(max_length=20, default='yes', db_column='isactive')

    class Meta:
        db_table = 'i3l_botmaster'
        managed = False
        app_label = 'i3l_automation'  # Important to match the app label used in router
