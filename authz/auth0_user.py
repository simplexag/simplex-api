from auth0.authentication import GetToken
from auth0.management import Auth0
from auth0.exceptions import Auth0Error
from django.conf import settings
import json

class Auth0User():
        domain = settings.AUTH0_DOMAIN
        non_interactive_client_id = settings.NON_INTERACTIVE_CLIENT_ID
        non_interactive_client_secret = settings.NON_INTERACTIVE_CLIENT_SECRET
        mgmt_api_token = None

        def __init__(self):
                get_token = GetToken(self.domain, self.non_interactive_client_id, client_secret=self.non_interactive_client_secret)
                token = get_token.client_credentials('https://{}/api/v2/'.format(self.domain))
                self.mgmt_api_token = token['access_token']
                

        def get_user_info(self, request):
                auth0 = Auth0(self.domain, self.mgmt_api_token)
                user_info = auth0.users.get(request.user.id)
                #users = auth0.users.list()
                return user_info           
        
        def update_user_metadata(self,request, metadata):
                auth0 = Auth0(self.domain, self.mgmt_api_token)
                try:
                        return auth0.users.update(
                                request.user.id,
                                {'user_metadata': metadata}
                                )
                except Auth0Error as e:
                        # Handle any errors if required
                        print('An error occurred:', e)
                        return None