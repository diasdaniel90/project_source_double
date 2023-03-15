from datetime import datetime
import graphene 
from django.conf import settings
from api.models import ServerResult


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
    
    server_results = graphene.List(
        ServerResultType,
        bet_color=graphene.Int(),
        bet_color__in=graphene.List(graphene.Int),
        total_red_eur_bet__gte=graphene.Int(),
        total_red_eur_bet__lte=graphene.Int(),
        total_black_eur_bet__gte=graphene.Int(),
        total_black_eur_bet__lte=graphene.Int(),
        total_white_eur_bet__gte=graphene.Int(),
        total_white_eur_bet__lte=graphene.Int(),
        total_red_bets_placed__gte=graphene.Int(),
        total_red_bets_placed__lte=graphene.Int(),
        total_black_bets_placed__gte=graphene.Int(),
        total_black_bets_placed__lte=graphene.Int(),
        total_white_bets_placed__gte=graphene.Int(),
        total_white_bets_placed__lte=graphene.Int(),
        total_eur_bet__gte = graphene.Int(),
        total_eur_bet__lte = graphene.Int(),
        total_bets_placed__gte = graphene.Int(),
        total_bets_placed__lte = graphene.Int(),
        total_retention_eur__gte = graphene.Int(),
        total_retention_eur__lte = graphene.Int(),
        datetime__gte=graphene.DateTime(),
        datetime__lte=graphene.DateTime()
    )
    def resolve_server_results(self, info, **kwargs):
        dt_gte = kwargs.pop('datetime__gte', None)
        dt_lte = kwargs.pop('datetime__lte', None)
        if dt_gte:
            kwargs['timestamp__gte'] = datetime.timestamp(dt_gte)
        if dt_lte:
            kwargs['timestamp__lte'] = datetime.timestamp(dt_lte)
        return ServerResult.objects.filter(**kwargs)
