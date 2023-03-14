from django.db import models

# Create your models here.
#blRLaZym1O,1678404899.28,rolling,2,13,2023-03-09T20:34:59

class ServerResult(models.Model):
    ID_bet = models.CharField(max_length=12, null=False, blank=False)
    timestamp = models.FloatField(null=False)
    bet_status = models.CharField(max_length=25, null=False, blank=False)
    bet_color = models.IntegerField(null=True)
    bet_roll = models.IntegerField(null=True)
    total_red_eur_bet = models.FloatField(null=True)
    total_red_bets_placed = models.FloatField(null=True)
    total_white_eur_bet = models.FloatField(null=True)
    total_white_bets_placed = models.FloatField(null=True)
    total_black_eur_bet = models.FloatField(null=True)
    total_black_bets_placed = models.FloatField(null=True)
    total_bets_placed = models.FloatField(null=True)
    total_eur_bet = models.FloatField(null=True)
    total_retention_eur = models.FloatField(null=True)
    
class ControlBetResult(models.Model):
    ID_bet = models.CharField(max_length=12, null=False, blank=False)
    timestamp = models.FloatField(null=False)
    bet_color = models.IntegerField(null=True)
    
# {
#   "id": 1678819445.061336,
#   "first_id_gale": 1678819445.061336,
#   "color": 2,
#   "source": "channel_1",
#   "amount": 1.6,
#   "score_bet": 0,
#   "amount_return": 0,
#   "gale": 0,
#   "status_bet": null,
#   "win": -1.0,
#   "win_status": -1,
#   "result_color": 1,
#   "created_ajust": "2023-03-14T18:44:05"
# }