from django.db import models

class actors(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    passwd = models.CharField(max_length=30)
    email = models.EmailField()
    rank = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    # TODO include a combobox to make possible for admin create more admins
    # python code have a permission type for it.

    class Meta:
        app_label = "account"

class research(models.Model):
    STATUS_CHOICES = (
        ('E', 'Editing'),
        ('A', 'Available'),
        ('X', 'Expired'),
    )

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    start_at = models.DateField()
    finish_at = models.DateField()
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    count = models.IntegerField(default=0)
    # TODO include a combobox to make possible for admin create more admins
    # python code have a permission type for it.

    class Meta:
        app_label = "account"
