from lxml import etree as ET
from .models import AnswerModel
from .models import QuestionModel


import os

class XMLHandler:

#Here what I can do is
    def populate_questions(self):
        """Populate db with questions from bioinformatics_posts_se.xml."""
        file_name = "bioinformatics_posts_se.xml"
        file_path = os.path.abspath(os.path.join(file_name))

        tree = ET.parse(file_path)

        for elem in tree.xpath("./row[@PostTypeId='1']"):
            print(elem.attrib['Id'])

            QuestionModel(
                id=elem.attrib['Id'],
                CreationDate=elem.attrib['CreationDate'],
                Score=elem.attrib['Score'],
                post_type_id=elem.attrib['PostTypeId'],
                ViewCount=elem.attrib['ViewCount'],
                Body=elem.attrib['Body'],
                OwnerUserId=elem.attrib['OwnerUserId'],
                LastActivityDate=elem.attrib['LastActivityDate'],
                Title=elem.attrib['Title'],
                Tags=elem.attrib['Tags'],
                AnswerCount=elem.attrib['AnswerCount'],
                CommentCount=elem.attrib['CommentCount'],
            ).save()
            # new_question = Question(Id=elem.attrib['Id'],
            #                         CreationDate=elem.attrib['CreationDate'],
            #                         Score=elem.attrib['Score'],
            #                         ViewCount=elem.attrib['ViewCount'],
            #                         Body=elem.attrib['Body'],
            #                         OwnerUserId=elem.attrib['OwnerUserId'],
            #                         LastActivityDate=elem.attrib['LastActivityDate'],
            #                         Title=elem.attrib['Title'],
            #                         Tags=elem.attrib['Tags'],
            #                         AnswerCount=elem.attrib['AnswerCount'],
            #                         CommentCount=elem.attrib['CommentCount'])
            # # db.session.add(new_question)
            # db.session.commit()
    def populate_answers(self):
        file_name = "bioinformatics_posts_se.xml"
        file_path = os.path.abspath(os.path.join(file_name))
        tree = ET.parse(file_path)

        for elem in tree.xpath("./row[@PostTypeId='2']"):
            print(elem.attrib['Id'])
            AnswerModel(
                id=elem.attrib['Id'],
                CreationDate=elem.attrib['CreationDate'],
                Score=elem.attrib['Score'],
                post_type_id=elem.attrib['PostTypeId'],
                ViewCount=elem.attrib['ViewCount'],
                Body=elem.attrib['Body'],
                OwnerUserId=elem.attrib['OwnerUserId'],
                LastActivityDate=elem.attrib['LastActivityDate'],
                parent_id=elem.attrib['ParentId'],
                CommentCount=elem.attrib['CommentCount'],

            ).save()






