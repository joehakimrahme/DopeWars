import uuid

from django.shortcuts import render

from core.models import Backpack
from core.models import Game
from core.models import Item
from core.models import ItemPrice
from core.models import ItemQuantity
from core.models import PriceList


def index(request):
    g = Game.objects.all()[:10]
    return render(request, 'core/index.html', {'new_game_id': uuid.uuid1(),
                                               'game': g,})

def display(request, game_id):
    g, created = Game.objects.get_or_create(game_uuid=game_id)
    if created:
        market = PriceList.objects.create(name="Game {} - day 0".format(game_id), game=g)
        backpack = Backpack.objects.create(game=g)
        for i in Item.objects.all():
            ip = ItemPrice.objects.create(item=i, pricelist=market)
            iq = ItemQuantity.objects.create(item=i, quantity=0, backpack=backpack)
        
    return render(request, 'core/game.html',
                  {'game': g,
                   'pricelist': g.pricelist_set.first(),
                   'backpack': g.backpack_set.first(),
                   'score': g.cash - 2 * g.debt})
