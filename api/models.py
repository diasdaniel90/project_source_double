from django.db import models

# Create your models here.
#blRLaZym1O,1678404899.28,rolling,2,13,2023-03-09T20:34:59

class ServerResult(models.Model):
    ID_bet = models.CharField(max_length=12, null=False, blank=False)
    timestamp = models.IntegerField(null=False)
    bet_status = models.CharField(max_length=25, null=False, blank=False)
    bet_color = models.IntegerField(null=True)
    bet_roll = models.IntegerField(null=True)
    total_red_eur_bet = models.IntegerField(null=True)
    total_red_bets_placed = models.IntegerField(null=True)
    total_white_eur_bet = models.IntegerField(null=True)
    total_white_bets_placed = models.IntegerField(null=True)
    total_black_eur_bet = models.IntegerField(null=True)
    total_black_bets_placed = models.IntegerField(null=True)
    total_bets_placed = models.IntegerField(null=True)
    total_eur_bet = models.IntegerField(null=True)
    total_retention_eur = models.IntegerField(null=True)