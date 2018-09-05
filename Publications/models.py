from django.db import models


class Base_User (models.Model):
    class Meta:
        abstract = True
        username = models.CharField(max_length=50)
        password = models.CharField(max_length=50)
        email = models.CharField(max_length=50)
        first_name = models.CharField(max_length=50)
        second_name = models.CharField(max_length=50)

class Base_Publication (models.Model):
    class Meta:
        abstract = True
        author = models.ForeignKey(Base_User)  # Как добавить ссылку на поле  name?
        body = models.TextField()
        pub_date = models.DateTimeField()

# Этот класс вроде и не нужен
# class User (Base_User):
        # user_group = models.ForeignKey(Group) # Как устранить эту ошибку? unresolved reference


class Group (models.Model):
    user = models.ForeignKey(Base_User)
    user_group = models.CharField(max_length=50)


class UserBrowserDetails (models.Model):
    name = models.ForeignKey(Base_User) # Как добавить ссылку на поле  name?
    ip = models.CharField(max_length=50)
    mac = models.CharField(max_length=50)
    browser_type = models.CharField(max_length=50)


class Publication (Base_Publication):
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=50)
    url_publication = models.CharField()


class Rating (models.Model):
    publication_rating = models.CharField() # Не знаю какой тип модели выбрать для рейтинга
    publication_details = models.ForeignKey(Publication)


class Comment (Base_Publication):
    link_to_publication = models.ForeignKey(Publication) # Нужно только поле URL


class Article (Base_Publication):
    url_original = models.CharField() # Какая-то ерунда


class ArticleType (models.Model):
    article = models.ForeignKey(Article)
    article_type = models.CharField()


class ArticleSection (models.Model):
    article = models.ForeignKey(Article)
    article_section = models.CharField()


class ArticleSectionGroup (models.Model):
    article_section = models.ForeignKey(ArticleSection)
    article_section_group = models.CharField()


class Image (models.Model):
    image = models.CharField() # Не знаю какой тип
    link_to_publication = models.ForeignKey(Publication)


class EmbeddedObject (models.Model):
    link_to_publication = models.ForeignKey(Publication)
    embedded_object = models.CharField() # Не знаю какой тип


class EmbeddedObjectType (models.Model):
    embedded_object = models.ForeignKey(EmbeddedObject)
    embedded_object_type = models.CharField()









