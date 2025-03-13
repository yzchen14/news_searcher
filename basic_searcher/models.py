from django.db import models

# Create your models here.




class KeywordGroup(models.Model):
    name = models.CharField(max_length=255)  # The name of the keyword group
    description = models.TextField(blank=True)  # Optional description of the group
    search_str = models.TextField(blank=True)  # String for search or crawling purposes

    def __str__(self):
        return self.name
    

class NewsRecord(models.Model):
    title = models.CharField(max_length=300)  # Title of the news record
    link = models.URLField()  # URL link to the full news article
    source = models.CharField(max_length=255)  # Source name or website of the article
    file_location = models.FileField(upload_to='news_files/', blank=True, null=True)  # Path to the file (optional)
    keyword_group = models.ForeignKey(KeywordGroup, related_name='news_records', on_delete=models.CASCADE)  # Link to the KeywordGroup
    doi_id = models.CharField(max_length=255, blank=True, null=True)
    affiliation = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.title



class CorrelationRecord(models.Model):
    new_record = models.ForeignKey(NewsRecord, on_delete=models.CASCADE)
    keyword_group = models.ForeignKey(KeywordGroup, on_delete=models.CASCADE)
    correlation = models.BooleanField(default=False)


class MailGroup(models.Model):
    name = models.CharField(max_length=255)  # The name of the subscription group
    mail_list = models.TextField()  # A list of email addresses, stored as a text
    main_group = models.CharField(max_length=15, blank=True, null=True)
    level = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name

class KeywordGroupSubscription(models.Model):
    keyword_group = models.ForeignKey(KeywordGroup, on_delete=models.CASCADE)
    subscription_group = models.ForeignKey(MailGroup, on_delete=models.CASCADE)

