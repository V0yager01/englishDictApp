from django.db import models


class RusVersion(models.Model):
    word = models.CharField(max_length=256,
                            blank=False,
                            null=False)
    
    def save(self, *args, **kwargs):
          self.word = self.word.lower()
          super().save(*args, **kwargs)
    
    def __str__(self):
            return self.word

class EngVersion(models.Model):
    word = models.CharField(max_length=256,
                            blank=False,
                            null=False)
    
    def save(self, *args, **kwargs):
          self.word = self.word.lower()
          super().save(*args, **kwargs)
    
    def __str__(self):
            return self.word
    
class Category(models.Model):
      slug = models.SlugField(verbose_name='Назвачение слага',
                              max_length=256,
                              unique=True)
      name = models.CharField(verbose_name='Название категории',
                              max_length=256,
                              unique=True)
      
      def __str__(self):
            return self.name
      

class RuToEng(models.Model):
    category = models.ManyToManyField(Category,
                                      max_length=256)
    ru_word = models.ForeignKey(RusVersion, on_delete=models.SET_NULL, null=True)
    eng_word = models.ForeignKey(EngVersion, on_delete=models.SET_NULL, null=True)
    win_rate = models.IntegerField(default=0)
    lose_rate = models.IntegerField(default=0)
        
    def __str__(self):
            return self.ru_word.word + "-" + self.eng_word.word
    
    class Meta:
          ordering=['eng_word__word']
          
