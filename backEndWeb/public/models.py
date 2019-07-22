from django.db import models

class Member1Model(models.Model):
    state_choices = (('Y','正常'),('F','冻结'),)
    time_stamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    user_id = models.IntegerField(null=False)
    name = models.CharField(max_length=256, null=False)
    phone = models.CharField(max_length=128, null=True)
    state = models.CharField(max_length=3, choices=state_choices, default='Y')
    
    class Meta:
        db_table = "member1model"
    
    def __str__(self):
        return self.name