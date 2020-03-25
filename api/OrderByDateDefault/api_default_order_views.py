from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DisplayData.DisplayAllFacade import DisplayAllQuestionFacade
from DisplayData.models import QuestionModel


'''
This is GET request api for the display of the data which is default according to the order by Creation date

Endpoint for viewcount - http://127.0.0.1:8000/order_by_default/


'''
class DefaultOrder(APIView):
    def get(self, request):
        defaultOrderObject = QuestionModel.objects.order_by('-CreationDate')
        allData = defaultOrderObject.values()
        dataToSend = []
        for question in allData:
            if question["CreationDate"] == None:
                continue
            questionid = question["Id"]
            print(questionid)
            questionData = DisplayAllQuestionFacade.getData(questionID=questionid)
            dataToSend.append(questionData)
        data_dic = {
            "msg": "success",
            "data": dataToSend
        }
        return Response(data=data_dic, status=status.HTTP_200_OK)
