from django.conf import settings

# Used to limit the number of unique IPs that can vote on a single object+field.
#   useful if you're getting rating spam by users registering multiple accounts
RATINGS_VOTES_PER_IP = getattr(settings, 'RATINGS_VOTES_PER_IP', 3)

RATINGS_USER_MODEL = getattr(settings, 'RATINGS_USER_MODEL', 'auth.User')
