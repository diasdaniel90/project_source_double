import graphene 
from django.conf import settings
from api.models import ServerResult
from datetime import datetime

class ServerResultType(graphene.ObjectType):
    ID_bet = graphene.String()
    timestamp = graphene.Int()
    bet_status = graphene.String()
    bet_color = graphene.Int()
    bet_roll = graphene.Int()
    datetime = graphene.DateTime()
    total_red_eur_bet = graphene.Int()
    total_red_bets_placed = graphene.Int()
    total_white_eur_bet = graphene.Int()
    total_white_bets_placed = graphene.Int()
    total_black_eur_bet = graphene.Int()
    total_black_bets_placed = graphene.Int()
    total_eur_bet = graphene.Int()
    total_bets_placed = graphene.Int()
    total_eur_bet = graphene.Int()
    total_retention_eur = graphene.Int()
    
    
    def resolve_datetime(self, info, **kwargs):
        return datetime.fromtimestamp(self.timestamp)     

class Query:
    version = graphene.String()
    def resolve_version(self, info, **kwargs):
        return settings.VERSION
    
    server_results = graphene.List(ServerResultType)
    def resolve_server_results(self, info, **kwargs):
        return ServerResult.objects.filter(**kwargs)

