import random
import json
import itertools
import time
from otree.api import *

doc = """
risk
Lukas Bolte: lukas.bolte@outlook.com. 
"""


class C(BaseConstants):
    NAME_IN_URL = 'risk'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5
    EXP_TIME = 10 # in minutes
    LOTTERY_DATA =  json.dumps([
        { 'lottery': 'LOTTERY A', 'lowPayoff': '$28', 'highPayoff': '$28' },
        { 'lottery': 'LOTTERY B', 'lowPayoff': '$24', 'highPayoff': '$36' },
        { 'lottery': 'LOTTERY C', 'lowPayoff': '$20', 'highPayoff': '$44' },
        { 'lottery': 'LOTTERY D', 'lowPayoff': '$16', 'highPayoff': '$52' },
        { 'lottery': 'LOTTERY E', 'lowPayoff': '$12', 'highPayoff': '$60' },
        { 'lottery': 'LOTTERY F', 'lowPayoff': '$2', 'highPayoff': '$70' }
    ])
    

class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    if subsession.round_number == 1:

        page_sequence = [
            ['intro','OK', 'middle', 'OKN','outro'],
            ['intro','OKN', 'middle', 'OK','outro']
        ]

        colors = ['blue','brown','dark']

        permutation_colors = list(itertools.permutations(colors))

        arrays = [page_sequence, permutation_colors]
        treatments = list(itertools.product(*arrays))
        # random.shuffle(treatments)
        treatments = itertools.cycle(treatments)


        for p in subsession.get_players():
            el = next(treatments)
            p.participant.treatment = el[0]
            p.participant.colorS = el[1][0]
            p.participant.colorOK = el[1][1]
            p.participant.colorOKN = el[1][2]
            p.participant.cqOK_who_mistakes = 0
            p.participant.cqOK_what_mistakes = 0
            p.participant.cqOK_find_out_mistakes = 0
            p.participant.cqOKN_who_mistakes = 0
            p.participant.cqOKN_what_mistakes = 0
            p.participant.cqOKN_find_out_mistakes = 0
            

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    data_dummy = models.StringField(blank=True)

    cqOK_who = models.IntegerField(blank=True,
        choices=[
            [1, 'Myself'],
            [2, 'Another participant']
        ],
        widget=widgets.RadioSelect,
        label='<strong>Who receives the lottery payoff?</strong>'
        )
    
    cqOK_what = models.IntegerField(blank=True,
        choices=[
            [1, 'Someone recruited on Prolific is choosing a lottery from the list of lotteries above'],
            [2, 'Nothing']
        ],
        widget=widgets.RadioSelect,
        label='<strong>What does the other participant know?</strong>'
        )
    
    cqOK_find_out = models.IntegerField(blank=True,
        choices=[
            [1, 'Yes'],
            [2, 'No']
        ],
        widget=widgets.RadioSelect,
        label='<strong>If DECISION 2 is implemented, will you find out whether the coin comes up "HIGH" or "LOW"? In other words, will you find out the payoff of the other participant?</strong>'
        )
    
    cqOKN_who = models.IntegerField(blank=True,
        choices=[
            [1, 'Myself'],
            [2, 'The OTHER PARTICIPANT from DECISION 2'],
            [3, 'A different OTHER PARTICIPANT']
        ],
        widget=widgets.RadioSelect,
        label='<strong>Who receives the lottery payoff?</strong>'
        )
    
    cqOKN_what = models.IntegerField(blank=True,
        choices=[
            [1, 'Someone recruited on Prolific is choosing a lottery from the list of lotteries above'],
            [2, 'Nothing']
        ],
        widget=widgets.RadioSelect,
        label='<strong>What does the other participant know?</strong>'
        )
    
    cqOKN_find_out = models.IntegerField(blank=True,
        choices=[
            [1, 'Yes'],
            [2, 'No']
        ],
        widget=widgets.RadioSelect,
        label='<strong>If DECISION 3 is implemented, will you find out whether the coin comes up "HIGH" or "LOW"? In other words, will you find out the payoff of the other participant?</strong>'
        )
    

    explainOK = models.LongStringField(blank=True,
        label='<strong>Please explain why in 2&ndash;3 sentences.</strong>'
        )
    
    explainOKN = models.LongStringField(blank=True,
        label='<strong>Please explain why in 2&ndash;3 sentences.</strong>'
        )
    

    agreement_emotions = models.IntegerField(blank=True,
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal,
        label='Please answer on a scale of 1 to 10, with 10 being "Agree the most."')
    
    agreement_outcomes = models.IntegerField(blank=True,
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal,
        label='Please answer on a scale of 1 to 10, with 10 being "Agree the most."')
    

    find_out = models.IntegerField(blank=True,
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal,
        label='Please answer on a scale of 1 to 10, with 10 being "Strongly prefer to find out."')
    
    feedback = models.LongStringField(label='<strong>Feedback:</strong>', blank=True)
    
    feedback_difficulty = models.IntegerField(label="How clear were the instructions? Please answer on a scale of 1 to 10, with 10 being the clearest.",
        blank=True,
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal)
    
    feedback_understanding = models.IntegerField(label="How well did you understand what you were asked to do? Please answer on a scale of 1 to 10, with 10 being the case when you understood perfectly.",
        blank=True,
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal)
    
    feedback_satisfied = models.IntegerField(label="How satisfied are you with this study overall? Please answer on a scale of 1 to 10, with 10 being the most satisfied.",
        blank=True,
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal)
    
    feedback_pay = models.IntegerField(label="How appropriate do you think the payment for this study is relative to other ones on Prolific? Please answer on a scale of 1 to 10, with 10 being the most appropriate.",
        blank=True,
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal)
    

###############################################  FUNCTIONS   ###########################################################


def get_lottery(player,lottery):
    lottery_data = json.loads(C.LOTTERY_DATA)
    for el in lottery_data:
        if el['lottery'] == lottery:
            return el
        
######################################################  PAGES   ########################################################


class Welcome(Page):
    form_model = 'player'
    form_fields = ['data_dummy']

    @staticmethod
    def vars_for_template(player):
        player.participant.start_time = time.time()
        pass

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.browser = player.data_dummy
        pass 

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='intro'


class Consent(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='intro' 


class About(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='intro' 


class InstructionsS(Page):
    @staticmethod
    def vars_for_template(player):
        return {
            'LOTTERY_DATA': C.LOTTERY_DATA
        }
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='intro' 


class ChoiceS(Page):
    form_model = 'player'
    form_fields = ['data_dummy']

    @staticmethod
    def vars_for_template(player):
        return {
            'LOTTERY_DATA': C.LOTTERY_DATA
        }
    
    @staticmethod
    def error_message(player, values):
        if values['data_dummy'] is None or values['data_dummy'] == '':
            return 'Please select a lottery.'               
    

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.choice_s = player.data_dummy
        pass

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='intro' 


class TransitionS(Page):
    pass

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='intro' 


class InstructionsOK(Page):
    @staticmethod
    def vars_for_template(player):
        return {
            'LOTTERY_DATA': C.LOTTERY_DATA
        }
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='OK' 


class OtherOK(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='OK' 


class CQOK(Page):
    form_model = 'player'
    form_fields = ['cqOK_who', 'cqOK_what', 'cqOK_find_out']

    @staticmethod
    def error_message(player, values):
        if not player.session.config['development']:
            solutions = dict(
                cqOK_who=2,
                cqOK_what=1,
                cqOK_find_out=1
                )
            error_messages = dict()
            for field_name in solutions:
                if values[field_name] is None:
                    error_messages[field_name] = 'Please, answer the question'
                elif values[field_name] != solutions[field_name]:
                    error_messages[field_name] = 'Please, correct your answer!'
                    name = 'player.participant.' + str(field_name) + '_mistakes'
                    exec("%s += 1" % name)
            return error_messages

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='OK'
     

class ChoiceOK(Page):
    form_model = 'player'
    form_fields = ['data_dummy']

    @staticmethod
    def vars_for_template(player):
        return {
            'LOTTERY_DATA': C.LOTTERY_DATA
        }
    
    @staticmethod
    def error_message(player, values):
        if values['data_dummy'] is None or values['data_dummy'] == '':
            return 'Please select a lottery.'               
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.choice_ok = player.data_dummy
        pass

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='OK' 


class TransitionOK(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='middle' 


class InstructionsOKN(Page):
    @staticmethod
    def vars_for_template(player):
        return {
            'LOTTERY_DATA': C.LOTTERY_DATA
        }
    
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='middle' 
    
class InstructionsDifference(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='middle' 
    



class CQOKN(Page):
    form_model = 'player'
    form_fields = ['cqOKN_who', 'cqOKN_what', 'cqOKN_find_out']

    @staticmethod
    def error_message(player, values):
        if not player.session.config['development']:
            solutions = dict(
                cqOKN_who=3,
                cqOKN_what=1,
                cqOKN_find_out=2
                )
            error_messages = dict()
            for field_name in solutions:
                if values[field_name] is None:
                    error_messages[field_name] = 'Please, answer the question'
                elif values[field_name] != solutions[field_name]:
                    error_messages[field_name] = 'Please, correct your answer!'
                    name = 'player.participant.' + str(field_name) + '_mistakes'
                    exec("%s += 1" % name)
            return error_messages

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='OKN' 
    

class ChoiceOKN(Page):
    form_model = 'player'
    form_fields = ['data_dummy']

    @staticmethod
    def vars_for_template(player):
        return {
            'LOTTERY_DATA': C.LOTTERY_DATA
        }
    
    @staticmethod
    def error_message(player, values):
        if values['data_dummy'] is None or values['data_dummy'] == '':
            return 'Please select a lottery.'               
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.choice_okn = player.data_dummy
        pass

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='OKN' 
    

class Explain(Page):
    form_model = 'player'
    form_fields = ['explainOK', 'explainOKN']

    @staticmethod
    def vars_for_template(player):

        lottery_s = get_lottery(player,player.participant.choice_s)
        lottery_ok = get_lottery(player,player.participant.choice_ok)
        lottery_okn = get_lottery(player,player.participant.choice_okn)
        
        text_s = player.participant.choice_s + ' (with low payoff of ' + lottery_s['lowPayoff'] + ' and high payoff of '+lottery_s['highPayoff'] + ') '
        text_ok = player.participant.choice_ok + ' (with low payoff of ' + lottery_ok['lowPayoff'] + ' and high payoff of '+lottery_ok['highPayoff'] + ') '
        text_okn = player.participant.choice_okn + ' (with low payoff of ' + lottery_okn['lowPayoff'] + ' and high payoff of '+lottery_okn['highPayoff'] + ') ' 

        print(player.participant.choice_s,player.participant.choice_ok,player.participant.choice_okn)

        print(text_s,text_ok,text_okn)


        return {
            'text_s': text_s,
            'text_ok': text_ok,
            'text_okn': text_okn
            # 'LOTTERY_DATA': C.LOTTERY_DATA
        }
    
    # @staticmethod
    # def error_message(player, values):
    #     if values['data_dummy'] is None or values['data_dummy'] == '':
    #         return 'Please select a lottery.'               
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.explain_ok = player.explainOK
        player.participant.explain_okn = player.explainOKN
        pass

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='outro' 
    


 

class Agreement(Page):
    form_model = 'player'
    form_fields = ['agreement_emotions', 'agreement_outcomes']

    @staticmethod
    def error_message(player, values):
        if not player.session.config['development']:
            error_messages = dict()
            for field_name in ['agreement_emotions', 'agreement_outcomes']:
                if values[field_name] is None:
                    error_messages[field_name] = 'Please, answer the question'
            return error_messages

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.agreement_emotions = player.field_maybe_none('agreement_emotions')
        player.participant.agreement_outcomes = player.field_maybe_none('agreement_outcomes')
        pass 


    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='outro' 


class FindOut(Page):
    form_model = 'player'
    form_fields = ['find_out']

    @staticmethod
    def error_message(player, values):
        if not player.session.config['development']:
            error_messages = dict()
            for field_name in ['find_out']:
                if values[field_name] is None:
                    error_messages[field_name] = 'Please, answer the question'
            return error_messages

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.find_out = player.field_maybe_none('find_out')
        pass 

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='outro' 
    

class Outcome(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='outro' 


class Feedback(Page):
    form_model = 'player'
    form_fields = ['feedback', 'feedback_difficulty', 'feedback_understanding', 'feedback_satisfied', 'feedback_pay']

    @staticmethod
    def vars_for_template(player):
        return {
            # 'LOTTERY_DATA': C.LOTTERY_DATA
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.feedback = player.field_maybe_none('feedback')
        player.participant.feedback_difficulty = player.field_maybe_none('feedback_difficulty')
        player.participant.feedback_understanding = player.field_maybe_none('feedback_understanding')
        player.participant.feedback_satisfied = player.field_maybe_none('feedback_satisfied')
        player.participant.feedback_pay = player.field_maybe_none('feedback_pay')

        pass

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='outro' 



class Finished(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='outro' 


class Redirect(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment[player.round_number-1]=='outro' 


page_sequence = [
    Welcome,
    Consent,
    About,
    InstructionsS,
    ChoiceS,
    TransitionS,
    InstructionsOK,
    OtherOK,
    CQOK,
    ChoiceOK,
    TransitionOK,
    InstructionsOKN,
    InstructionsDifference,
    CQOKN,
    ChoiceOKN,
    Explain,
    Agreement,
    FindOut,
    Outcome,
    Feedback,
    Finished,
    Redirect
]
