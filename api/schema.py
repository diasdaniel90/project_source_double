from datetime import datetime
import graphene
import pytz
from django.conf import settings
from api.models import ServerResult, UserResult, ControlBetResult, GoControlBetResult


class GoControlBetResultType(graphene.ObjectType):
    ID_bet = graphene.String()
    timestamp = graphene.Float()
    timestamp_signal = graphene.Float()
    color = graphene.Int()
    source = graphene.String()
    win = graphene.Boolean()
    status = graphene.String()
    gale = graphene.Int()
    amount = graphene.Float()
    balanceWin = graphene.Float()
    datetime = graphene.DateTime()
    datetime_signal = graphene.DateTime()

    def resolve_datetime(self, info, **kwargs):
        return datetime.fromtimestamp(self.timestamp).astimezone(
                pytz.timezone('America/Sao_Paulo')
            )

    def resolve_datetime_signal(self, info, **kwargs):
        return datetime.fromtimestamp(self.timestamp_signal).astimezone(
                pytz.timezone('America/Sao_Paulo')
            )


class UserResultType(graphene.ObjectType):
    ID_bet = graphene.String()
    ID_bet_uniqa = graphene.String()
    timestamp = graphene.Int()
    datetime = graphene.DateTime()
    color = graphene.Int()
    amount = graphene.Float()
    currency_type = graphene.String()
    user = graphene.String()
    simulations = graphene.List(GoControlBetResultType)

    def resolve_simulations(self, info, **kwargs):
        return GoControlBetResult.objects.filter(ID_bet=self.ID_bet)

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
    simulations = graphene.List(GoControlBetResultType)

    def resolve_simulations(self, info, **kwargs):
        return GoControlBetResult.objects.filter(ID_bet=self.ID_bet)
    
    def resolve_user_results(self, info, **kwargs):
        return UserResult.objects.filter(ID_bet=self.ID_bet)

    def resolve_datetime(self, info, **kwargs):
        return datetime.fromtimestamp(self.timestamp)     


class Query:
    version = graphene.String()
    def resolve_version(self, info, **kwargs):
        return settings.VERSION

    go_control_bet_results = graphene.List(
        GoControlBetResultType,
        ID_bet=graphene.String(description='Filter by bet id'),
        ID_bet__in=graphene.List(
            graphene.String,
            description='Filter by listed bet ids'
        ),
        color=graphene.Int(description='Filter by bet color'),
        color__in=graphene.List(
            graphene.Int,
            description='Filter by bet colors listed'
        ),
        source=graphene.String(description='Filter by bet source'),
        status=graphene.String(description='Filter by bet status'),
        win=graphene.Boolean(description='Filter by win result'),
        gale=graphene.Int(
            description='Filter by bet gale'
        ),
        gale__in=graphene.List(
            graphene.Int,
            description='Filter by listed gales'
        ),
        amount=graphene.Float(description='Filter by amount spent'),
        amount__lte=graphene.Float(description='Filter by amount lesser or equal inputed value'),
        amount__gte=graphene.Float(description='Filter by amount spent greater or equal inputed value'),
        balanceWin=graphene.Float(description='Filter by win balance'),
        datetime__gte=graphene.DateTime(description='Filter by bet starting datetime'),
        datetime__lte=graphene.DateTime(description='Filter by bets up to datetime')
    )
    def resolve_go_control_bet_results(self, info, **kwargs):
        dt_gte = kwargs.pop('datetime__gte', None)
        dt_lte = kwargs.pop('datetime__lte', None)
        if dt_gte:
            kwargs['timestamp__gte'] = datetime.timestamp(dt_gte)
        if dt_lte:
            kwargs['timestamp__lte'] = datetime.timestamp(dt_lte)
        return GoControlBetResult.objects.filter(**kwargs)


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
    


