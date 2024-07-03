from django.db import models

from django.db import models

class College(models.Model):

    id = models.AutoField(primary_key=True)
    rank = models.IntegerField(null=True)
    logo_url = models.CharField(max_length=255, null=True)
    cn_name = models.CharField(max_length=128, null=True)
    en_name = models.CharField(max_length=256, null=True)
    tags = models.CharField(max_length=32, null=True)
    province = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=36, null=True)
    score = models.FloatField(null=True)
    level = models.FloatField(null=True)

    class Meta:
        db_table = 'college'