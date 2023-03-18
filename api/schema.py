from datetime import datetime
import graphene 
from django.conf import settings
from api.models import ServerResult, UserResult, ControlBetResult

class UserResultType(graphene.ObjectType):
    ID_bet = graphene.String()
    ID_bet_uniqa = graphene.String()
    timestamp = graphene.Int()
    datetime = graphene.DateTime()
    color = graphene.Int()
    amount = graphene.Float()
    currency_type = graphene.String()
    user = graphene.String()
    
    def resolve_datetime(self, info, **kwargs):
        return datetime.fromtimestamp(self.timestamp) 

class ControlBetResultType(graphene.ObjectType):
    ID_bet = graphene.String()
    timestamp = graphene.Int()
    datetime = graphene.DateTime()
    first_id_gale =  graphene.String()
    color = graphene.Int()
    source = graphene.String()
    amount = graphene.Float()
    score_bet = graphene.Float()
    amount_return = graphene.Float()
    gale = graphene.Int()
    status_bet = graphene.String()
    win = graphene.Int()
    win_status = graphene.Int()
    result_color = graphene.Int()
    result_id = graphene.String()
    
    def resolve_datetime(self, info, **kwargs):
        return datetime.fromtimestamp(self.timestamp)   
    
class ServerResultType(graphene.ObjectType):
    ID_bet = graphene.String()
    timestamp = graphene.Int()
    datetime = graphene.DateTime()
    bet_status = graphene.String()
    bet_color = graphene.Int()
    bet_roll = graphene.Int()
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
    user_results = graphene.List(UserResultType)
    
    def resolve_user_results(self, info, **kwargs):
        return UserResult.objects.filter(ID_bet=self.ID_bet)

    def resolve_datetime(self, info, **kwargs):
        return datetime.fromtimestamp(self.timestamp)     

class Query:
    version = graphene.String()
    def resolve_version(self, info, **kwargs):
        return settings.VERSION
    
    control_bet_result = graphene.List(
        ControlBetResultType,
        ID_bet = graphene.String(),
        timestamp = graphene.Int(),
        first_id_gale =  graphene.String(),
        color = graphene.Int(),
        source = graphene.String(),
        amount = graphene.Float(),
        score_bet = graphene.Float(),
        amount_return = graphene.Float(),
        gale = graphene.Int(),
        status_bet = graphene.String(),
        win = graphene.Int(),
        win_status = graphene.Int(),
        result_color = graphene.Int(),
        result_id = graphene.String(),
    )
    def resolve_control_bet_result(self, info, **kwargs):
        return ControlBetResult.objects.filter(**kwargs)
    
    user_result = graphene.List(
        UserResultType,
        ID_bet = graphene.String(),
        ID_bet_uniqa = graphene.String(),
        color = graphene.Int(),
        amount = graphene.Float(),
        currency_type = graphene.String(),
        user = graphene.String(), 
    )
    def resolve_user_result(self, info, **kwargs):
        return UserResult.objects.filter(**kwargs)
    
    server_results = graphene.List(
        ServerResultType,
        ID_bet=graphene.String(),
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
    


