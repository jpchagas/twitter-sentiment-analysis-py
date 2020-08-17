from libs_app import tw

# keys
with open('kt/kt.txt') as file:
    CKey = file.readline().strip('\n')
    CSKey = file.readline().strip('\n')


# Connection
auth = tw.OAuthHandler(CKey, CSKey)


# API Access
api = tw.API(auth, wait_on_limit = True, wait_on_rate_limit_notify = True, timeout = 120)