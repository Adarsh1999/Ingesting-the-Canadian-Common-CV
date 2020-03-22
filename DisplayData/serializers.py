from rest_framework import serializers
from .models import QuestionModel
from .models import AnswerModel
# a serializer class for our models Upload
class CreateQuestionSerializer(serializers.ModelSerializer):
  class Meta():
    model = QuestionModel
    # the fields which needs to be serialized
    fields = (
    'id', 'post_type_id', 'CreationDate', 'Score', 'ViewCount', 'Body', 'OwnerUserId', 'LastActivityDate', 'Title',
    'Tags', 'AnswerCount', 'CommentCount')

class CreateAnswerSerializer(serializers.ModelSerializer):
  class Meta():
    model= AnswerModel
    fields=('id','post_type_id','parent_id','CreationDate','Score','Body','OwnerUserId','LastActivityDate', 'CommentCount')