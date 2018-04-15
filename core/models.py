import random

from django.db import models


class Item(models.Model):
  name = models.CharField(max_length=200)
  price_min = models.IntegerField()
  price_max = models.IntegerField()

  def get_random_price(self):
      return random.randint(self.price_min, self.price_max)

  def __repr__(self):
      return self.name

  def __str__(self):
      return self.name


class Game(models.Model):
    game_uuid = models.UUIDField(primary_key=True)
    day = models.IntegerField(default=0)
    cash = models.IntegerField(default=2000)
    debt = models.IntegerField(default=5500)

    def __repr__(self):
        return "Game {} (day: {})".format(
            self.game_uuid,
            self.day)

  
class PriceList(models.Model):
  name = models.CharField(max_length=200)
  items = models.ManyToManyField(Item, through='ItemPrice')
  game = models.ForeignKey(Game, on_delete=models.CASCADE)


class ItemPrice(models.Model):
  item = models.ForeignKey(Item, on_delete=models.PROTECT)
  pricelist = models.ForeignKey(PriceList, on_delete=models.CASCADE)
  price = models.IntegerField()
  
  class Meta:
    unique_together = ['item', 'pricelist']

  def save(self, *args, **kwargs):
    if self.id is None:
      self.price = self.item.get_random_price()
    return super(ItemPrice, self).save(*args, **kwargs)    


class Backpack(models.Model):
    items = models.ManyToManyField(Item, through='ItemQuantity')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class ItemQuantity(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    backpack = models.ForeignKey(Backpack, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ['item', 'backpack']
