from django.db import models

# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=100)
    # Adding search class or re-use Categories
    def __str__(self):
        return self.title

class Authors(models.Model):
    name = models.CharField(max_length=100)
    post_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Posts(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    author = models.ForeignKey(Authors, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    published_at = models.DateTimeField(auto_now_add=True)
    time_to_read = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class ResentlyPosteds(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    def __str__(self):
        return self.post

    
class Popular(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)


class Featured(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)


class TopAuthors(models.Model):
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)

    
class TodaysUpdates(models.Model):
    new_posts = models.ForeignKey(Posts, on_delete=models.CASCADE)

    visitors = models.IntegerField(default=0)
    subscribers = models.IntegerField(default=0)
    blog_read = models.IntegerField(default=0)