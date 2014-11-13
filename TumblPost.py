#! /usr/bin/python

import pytumblr
import json

class TumblPost:
    def __init__( self, dateStr, titleStr, bodyStr ):
        self.dateStr = dateStr
        self.titleStr = titleStr
        self.bodyStr = bodyStr

        self.blogName = "lookatmeimdanny"
        self.state = "draft"
=======
    def PostToTumblr( self ):

        #get creds
        credFile = "TumblCreds.txt"
        f = open(credFile)
        OAUTH_KEY = f.readline()
        OAUTH_SECRET = f.readline()
        t = Tumblpy( OAUTH_KEY, OAUTH_SECRET )

        auth_props = t.get_authentication_tokens()
        auth_url = auth_props['auth_url']
        OAUTH_TOKEN_SECRET = auth_props['oauth_token_secret']

        t = Tumblpy(OAUTH_KEY,OAUTH_SECRET,
            OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    def PostToTumblr( self ):
        credentials = json.loads( open( 'TumblCreds.json', 'r' ).read() )
        client = pytumblr.TumblrRestClient( credentials['consumer_key'], \
                                                credentials['consumer_secret'], \
                                                credentials['oauth_token'], \
                                                credentials['oauth_token_secret'] )
        
        #print( client.info() )
        client.create_text( self.blogName, type="text", state=self.state, \
                            date=self.dateStr, format="html", \
                            title=self.titleStr, body=self.bodyStr )

        
                                                         
