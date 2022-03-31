from django.db import models

class BibleKorhrv(models.Model):
    book = models.IntegerField()
    chapter = models.IntegerField()
    verse = models.IntegerField() 
    content = models.TextField()
    fake_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'bible_korHRV'
        constraints = [
            models.UniqueConstraint(fields=['book', 'chapter', 'verse'], name='unique')
        ]