from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    photo = models.ImageField(blank= True, null = True, upload_to = 'blog_photo')
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length = 200) # 댓글 
    date = models.DateTimeField(auto_now_add = True) # 댓글 달린 날짜
    post = models.ForeignKey(Blog, on_delete= models.CASCADE)
    # 어떤 게시물에 달려있는 댓글인지 알 수 있는, 댓글이 달린 그 게시물이 쓰임
    # post는 블로그 객체를 참조하는 외래키로 만들어야 함!
    # 게시물이 삭제되면 댓글도 덩달아 삭제되어야 하므로 CASCADE를 해줘야함.
    def __str__(self):
        return self.comment