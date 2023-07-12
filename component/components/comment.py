from component.models import Comment
from django_unicorn.components import UnicornView, QuerySetType
from django.contrib import messages


class CommentView(UnicornView):
    content: str = ""
    comments: QuerySetType[Comment] = Comment.objects.none()
    comment_id: int = None

    def mount(self):
        self.comments = Comment.objects.all()

    def add_comment(self):
        if self.comment_id:
            # Update existing comment
            comment = Comment.objects.get(id=self.comment_id)
            comment.content = self.content
            if self.content:
                comment.save()
            else:
                print("no comment")
                messages.error(self.request, "comment body is none")
                comment = Comment.objects.get(id=self.comment_id)

        else:
            # Create new comment
            Comment.objects.create(content=self.content)
        self.content = ""
        self.comment_id = None
        self.comments = Comment.objects.all()

    def delete_comment(self, id):
        comment = Comment.objects.get(id=id)
        comment.delete()
        self.comments = Comment.objects.all()

    def delete_all(self):
        Comment.objects.all().delete()
        self.comments = Comment.objects.none()

    def edit_comment(self, id):
        mycomment = Comment.objects.get(id=id)
        self.content = str(mycomment)
        self.content = mycomment.content
        self.comment_id = id
