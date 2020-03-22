from datetime import datetime
from elasticsearch_dsl import Document, Date, Nested,token_filter, Boolean, \
    analyzer, InnerDoc, Completion, Keyword, Text,connections,Integer,Short,Float,Double,tokenizer, Long, analysis


from DisplayData.models import QuestionModel
from DisplayData.models import AnswerModel


data_analyzer= analyzer(
    'data_analyzer',
    tokenizer=tokenizer(
        'whitespace',
        'edge_ngram',
        min_gram=1,
        max_gram=10,
    ),
    filter=[
        'lowercase',
        token_filter('asciifolding')
    ]
)

class QuestionIndex(Document):
    Id = Integer()
    post_type_id = Integer()
    CreationDate = Date()
    Score =Integer()
    Body = Text(analyzer=data_analyzer, fields={'keyword': Keyword()})
    ViewCount =Integer()

    OwnerUserId = Integer()
    LastActivityDate = Date()
    Title = Text(analyzer=data_analyzer, fields={'keyword': Keyword()})
    Tags = Text(analyzer=data_analyzer, fields={'keyword': Keyword()})
    AnswerCount = Integer()
    CommentCount =Integer()

    class Index:
        name="questions_index"
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }