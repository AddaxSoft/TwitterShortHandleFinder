#!/bin/python

import http.client
import time

def getServerResponsForUser(usr):
    # Clear-text HTTP is no longer supported - you must use HTTPS
    usr = "/" + ''.join(usr)
    
    # Twitter replies with HTTP status 404 if user does not exis
    try:
        conn = http.client.HTTPSConnection("twitter.com")
        conn.request("HEAD", usr)
        return conn.getresponse().status
    except BaseException:
        print("Network/Twitter Blockage Error .. Zzzing for sometime and retrying again")
        time.sleep(5) #Sleeps for 2 secs
        getServerResponsForUser(usr)
        ################################################################
	# in future versions this should cache current results and quit#
	# then resume later after user relaunch                        #
	################################################################
        return None


def lastCase (lst):
    for i in range(0, len(lst)):
        if ( lst[i] != '_' ):
            return False
    return True
    
    
l = [''] * 4
l[0] = '0'
index = 0

while ( not lastCase(l) ):
    
    if ( ord(l[index]) > ord('_') ):
        l[index] = '0'
        index += 1
        while( l[index] == '_' ):
            l[index] = '0'
            index += 1
        if (l[index] == ''):
            l[index] = '0'
    
    

    #print(''.join(l))
    user = ''.join(l)
    if ( getServerResponsForUser(user) == "404" ):
        print(" >>> " + user)

    l[index] = chr(ord(l[index]) +1)
    
    if ( ord(l[index]) > ord('9') and ord(l[index]) < ord('A') ):
        l[index] = 'A'
    elif ( ord(l[index]) > ord('Z') and ord(l[index]) < ord('_')  ): 
        l[index] = '_'
    
    index = 0
    
# print (''.join(l))
user = ''.join(l)
if ( getServerResponsForUser(user) == "404" ):
        print(" >>> " + user)

