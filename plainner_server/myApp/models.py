from django.db import models

class Todo( models.Model ):
    # id = models.PositiveIntegerField() AUTO_INCREMENT,
    username = models.CharField( max_length = 32 )
    nickname = models.CharField( max_length = 32 )
    password = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

class User( models.Model ):
    content = models.CharField( max_length = 256 )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_completed = models.BooleanField()
    user_id = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    is_deleted = models.BooleanField()