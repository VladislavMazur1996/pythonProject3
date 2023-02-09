from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)

    def update_rating(self):
        post_rating = self.post_set.all().aggregate(rate_post=Sum('rating'))['rate_post'] * 6
        rating_comm_by = Comment.objects.filter(user=self.user).aggregate(Sum('rating'))['rating__sum']
        rating_comm_to = Comment.objects.filter(post__author__user=self.user).aggregate(Sum('rating'))['rating__sum']
        self.rating = rating_comm_to + rating_comm_by + post_rating
        self.save()
        return rating_comm_to + rating_comm_by + post_rating


class Category(models.Model):
    category = models.CharField(max_length=255, default='Разное', unique=True)


class Post(models.Model):
    news = 'NE'
    article = 'AR'

    RANK = [(news, 'Новость'),
            (article, 'Статья'),
            ]

    rank = models.CharField(max_length=2, choices=RANK, default=article)
    creating_dt = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.FloatField(default=0.0)
    category = models.ManyToManyField(Category, through='PostCategory')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[:124] if len(self.text)  > 124 else self.text}...'

    def __str__(self):
        return self.title.title()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    creating_dt = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()