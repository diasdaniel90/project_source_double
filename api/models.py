from django.db import models

# Create your models here.
#blRLaZym1O,1678404899.28,rolling,2,13,2023-03-09T20:34:59

class ServerResult(models.Model):
    ID_bet = models.CharField(max_length=12, null=False, blank=False)
    timestamp = models.FloatField(null=False)
    bet_status = models.CharField(max_length=25, null=False, blank=False)
    bet_color = models.IntegerField(null=False)
    bet_roll = models.IntegerField(null=False)
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
    first_id_gale =  models.CharField(max_length=12, null=False, blank=False)
    color = models.IntegerField(null=False)
    source = models.CharField(max_length=35, null=False, blank=False)
    amount = models.FloatField(null=False)
    score_bet = models.FloatField(null=False)
    amount_return = models.FloatField(null=False)
    gale = models.IntegerField(null=False)
    status_bet = models.CharField(max_length=16, null=True, blank=True)
    win = models.IntegerField(null=False)
    win_status = models.IntegerField(null=False)
    result_color = models.IntegerField(null=False)
    result_id = models.CharField(max_length=12, null=False, blank=False)

class UserResult(models.Model):
    ID_bet = models.CharField(max_length=12, null=False, blank=False)
    ID_bet_uniqa = models.CharField(max_length=16, null=True, blank=True)
    timestamp = models.FloatField(null=False)
    color = models.IntegerField(null=False)
    amount = models.FloatField(null=False)
    currency_type = models.CharField(max_length=3, null=False, blank=False)
    user = models.CharField(max_length=12, null=False, blank=False)

class GoControlBetResult(models.Model):
    ID_bet = models.CharField(max_length=12, null=False, blank=False)
    timestamp = models.FloatField(null=False)
    timestamp_signal = models.FloatField(null=False)
    color = models.IntegerField(null=False)
    source = models.CharField(max_length=35, null=False, blank=False)
    win = models.BooleanField(null=False)
    status = models.CharField(max_length=16, null=True, blank=True)
    gale = models.IntegerField(null=False)
    amount = models.FloatField(null=False)
    balanceWin = models.FloatField(null=False)
