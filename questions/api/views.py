from rest_framework import viewsets, generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from questions.models import Question, Answer
from questions.api.serializers import QuestionSerializer, AnswerSerializer
from questions.api.permissions import IsAuthorOrReadOnly


class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        question = get_object_or_404(Question, slug=kwarg_slug)

        if question.answers.filter(author=request_user).exists():
            raise ValidationError("You have already answer this questions!")
        
        serializer.save(author=request_user, question=question)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)