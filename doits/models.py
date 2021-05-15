from django.db import models
from core import models as core_models
from django.urls import reverse
# Create your models here.

"""
Here are the models you have to create:
- Movie:
  title ->제목
  year -> 날짜
  cover_image -> 사진
  category (ManyToMany => categories.Category) -> 카테고리(무슨대회인지)
"""


class Doit(core_models.TimeStampedModel):

  Bloop = "Bloop"
  BrainF = "BrainF"
  QBasic = "QBasic"
  Erlang = "Erlang"
  Next_js = "Next.js"
  TypeScript = "TypeScript"
  Dart = "Dart"
  Crystal = "Crystal"
  Lua = "Lua"
  Deno = "Deno"
  Clojure = "Clojure"
  Haskell = "Haskell"
  F_ = "F#"
  React = "React"
  Kotlin = "Kotlin"
  Rust = "Rust"
  Node_js = "Node.js"
  Objective_c = "Objective-C"
  Assembly_language = "Assembly language"
  Ruby = "Ruby"
  Swift = "Swift"
  Go = "Go"
  SQL = "SQL"
  R = "R"
  PHP = "PHP"
  JavaScript = "JavaScript"
  C_ = "C#"
  C__ = "C++"
  Java = "Java"
  Python = "Python"
  C = "C"

  Web = "Web"
  Ai = "Ai"
  Game = "Game"
  App = "App"
  Etc = "Etc"

  CATEGORY_CHOICES = (
      (Ai, "AI"),
      (App, "APP"),
      (Web, "WEB"),
      (Game, "GAME"),
      (Etc, "ETC")
  )

  LANGUAGE_CHOICES = (
      (C, "C"),
      (Java, "Java"),
      (Python, "Python"),
      (C_, "C#"),
      (C__, "C++"),
      (JavaScript, "JavaScript"),
      (React, "React"),
      (TypeScript, "TypeScript"),
      (PHP, "PHP"),
      (Kotlin, "Kotlin"),
      (Node_js, "Node.js"),
      (Swift, "Swift"),
      (Assembly_language, "Assembly_Language"),
      (Bloop, "Bloop"),
      (BrainF, "BrainF"),
      (QBasic, "QBasic"),
      (Erlang, "Erlang"),
      (Next_js, "Next.js"),
      (Dart, "Dart"),
      (Crystal, "Crystal"),
      (Lua, "Lua"),
      (Deno, "Deno"),
      (Clojure, "Clojure"),
      (Haskell, "Haskell"),
      (F_, "F#"),
      (Rust, "Rust"),
      (Objective_c, "Objective-C"),
      (Ruby, "Ruby"),
      (Go, "Go"),
      (SQL, "SQL"),
      (R, "R"),
  )


  title = models.CharField(max_length=120) 
  image = models.ImageField()   
  category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
  개발자 = models.CharField(max_length=10)
  explain = models.TextField(max_length=1000)
  Programing_Language = models.CharField(choices=LANGUAGE_CHOICES, max_length=20, blank=True, null=True)
  user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, blank=True)
  link = models.URLField(max_length=70)

  
  def __str__(self):
    return self.title  
  
  def get_absolute_url(self):
      return reverse('core:doit')
  
   
  @property
  def get_photo_url(self):
      if self.image:
          return self.image.url
      else:
          return "/static/images/user.jpg"

#학년, 제목, 카테고리, 장르, 유저, 깃허브주소 유저

    