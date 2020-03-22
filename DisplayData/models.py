
# Create your models here.

from django.db import models
from DisplayData.document import QuestionIndex

# Create your models here.

# to ask that user id and simple id is char or have to be primary key
class QuestionModel(models.Model):
    Id = models.IntegerField(primary_key=True)
    post_type_id=models.IntegerField(blank=False)
    CreationDate=models.DateTimeField(auto_now_add=True)
    Score=models.IntegerField(default=0)
    Body=models.TextField()
    ViewCount=models.IntegerField(default=0)

    OwnerUserId=models.CharField(max_length=20, blank=False)
    LastActivityDate=models.DateTimeField(auto_now_add=True)
    Title=models.TextField()
    Tags=models.TextField()
    AnswerCount=models.IntegerField(default=0)
    CommentCount=models.IntegerField(default=0)



    class Meta:
        db_table = "question_table"

    def indexing(self, **kwargs):
        obj = QuestionIndex(
            meta={'id': self.id},
            id=self.id,
            post_type_id=self.post_type_id,
            CreationDate = self.CreationDate,
            Body = self.Body,
            ViewCount = self.ViewCount,

            OwnerUserId =self.OwnerUserId,
            LastActivityDate = self.LastActivityDate,
            Title = self.Title,
            Tags = self.Tags,
            AnswerCount = self.AnswerCount,
            CommentCount = self.CommentCount,

        )
        obj.save(**kwargs)
        return obj.to_dict(include_meta=True)


class AnswerModel(models.Model):
    Id = models.IntegerField(primary_key=True)
    post_type_id=models.IntegerField(blank=False)
    parent= models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    CreationDate=models.DateTimeField(auto_now_add=True)
    Score=models.IntegerField()
    Body=models.TextField()
    OwnerUserId=models.CharField(max_length=20, blank=False)
    LastActivityDate=models.DateTimeField(auto_now_add=True)

    CommentCount=models.IntegerField(default=0)

    class Meta:
        db_table = "answer_table"


