from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.Serializer):
    question_text = serializers.CharField()
    pub_date = serializers.DateTimeField()
    '''def update_question(request, pk):
        """
        Get the list of questions on our website
        """
        questions = Question.objects.get(id=pk)
        serializer = QuestionSerializer(questions, data=request.data, partial=True)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(status=400, data=serializer.errors)'''
    def create(self, validated_data):
        """
        Create and return a new `Question` instance, given the validated data
        """
        return Question.object.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Question` instance, given the validated data
        """
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.save()
        return instance

