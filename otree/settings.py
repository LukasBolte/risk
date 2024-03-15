from os import environ

SESSION_CONFIGS = [
    dict(
        name='risk',
        app_sequence=['risk'],
        num_demo_participants=3,
        development=False
    ),
    dict(
        name='risk_development',
        app_sequence=['risk'],
        num_demo_participants=3,
        development=True
    ),
]


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['treatment','colorS','colorOK','colorOKN','start_time', 'end_time','choice_s','choice_ok','choice_okn','browser','cqOK_who_mistakes','cqOK_what_mistakes','cqOK_find_out_mistakes','cqOKN_who_mistakes','cqOKN_what_mistakes','cqOKN_find_out_mistakes','explain_ok','explain_okn','agreement_emotions','agreement_outcomes','find_out','feedback','feedback_difficulty','feedback_understanding','feedback_satisfied','feedback_pay']

SESSION_FIELDS = ['prolific_completion_url']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4062875054604'
