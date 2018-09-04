from django.db import models

class User (models.Model):
    name = models.CharField(max_length=50)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    user_group = models.ForeignKey(Group) # Как устранить эту ошибку? unresolved reference

class Group (models.Model):
    user = models.ForeignKey(User)
    user_group = models.CharField(max_length=50)

class UserBrowserDetails (models.Model):
    name = models.ForeignKey(User) # Как добавить ссылку на поле  name?
    IP = models.CharField(max_length=50)
    MAC = models.CharField(max_length=50)
    browser_type = models.CharField(max_length=50)

class Rating (models.Model):
    publication_rating = models.CharField() # Не знаю что выбрать для рейтинга
    publication_details = models.ForeignKey(Publication)
    users_rating = models.CharField()
    user_details = models.ForeignKey(User)

# Автор, заголовок, текст, жанр, время и дата создания
class Publication (models.Model):
    author = models.ForeignKey(User) # Как добавить ссылку на поле  name?
    title = models.CharField(max_length=150)
    body = models.TextField()
    genre = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    publication_rating = models.ForeignKey(Rating)


class Comment (Publication):
    comment_body = models.TextField()

class Article (Publication):




