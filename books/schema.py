import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import *



class BookType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ('id','title','excerpt','timeStamp')


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id','name','timeStamp')

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ('id','title','category','timeStamp')


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('id','technique','title','difficulty','is_active','timeStamp')


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ('id','question','answerText','timeStamp')


# ============================================================================
'''Query >>> for fetching data'''
# ============================================================================
class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)

    def resolve_all_books(root,info):
        return Books.objects.all()
        # return Books.objects.filter(title__startswith='God')
# ----------------------------------------------------------------------------
class Query(graphene.ObjectType):
    all_category = graphene.List(CategoryType)

    def resolve_all_category(root,info):
        return Category.objects.all()
# ============================================================================
'''SCHEMA TO ACCESS MODEL DATA'''
# ============================================================================
schema = graphene.Schema(query=Query)

