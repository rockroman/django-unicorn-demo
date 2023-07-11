from component.models import Comment
from django_unicorn.components import UnicornView, QuerySetType


class CommentView(UnicornView):
    content: str = ""
    comments: QuerySetType[Comment] = Comment.objects.none()

    def mount(self):
        self.comments = Comment.objects.all()

    def add_comment(self):
        Comment.objects.create(content=self.content)
        self.comments = Comment.objects.all()
        self.content = ""

    def delete_comment(self, id):
        comment = Comment.objects.get(id=id)
        comment.delete()
        self.comments = Comment.objects.all()

    def delete_all(self):
        Comment.objects.all().delete()
        self.comments = Comment.objects.none()
