#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bcrypt
import sqlite3
import tweepy
import sys, os, time, getopt

usage = """\
tweeter.py - a command line tweeter!

Author: Rob Greene
Date: 18th June 2014

USAGE:	tweeter.py -u <username> | --user=<username> -m <status> | --message=<status>

Arguments:
Name	Long name	Type	Comments
==============================================================================
-u	--username	String	The username, complete with '@' sign, for the account.

-m	--message	String	The message, or status, to post on Twitter

Note: access and authentication keys should be added to tweeters.db using the 
"add_tweeter.py" script.
"""

def showUsage(reason=""):
	print(usage)
	if reason:
		print(reason)

def validateUser(user):
	if not user.startswith("@"):
		showUsage(reason="The username must start with @")
	
	conn = sqlite3.connect("tweeters.db")
	c = conn.cursor()
	c.execute("""SELECT consumer_key, consumer_secret, access_token, access_secret FROM `tweeters` WHERE `user`="%s" LIMIT 1""" % user)

	credentials = c.fetchone()

	conn.close()

	credDict = {
				"consumer_key":credentials[0], 
				"consumer_secret":credentials[1],
				"access_token":credentials[2],
				"access_secret":credentials[3]
			   }

	return credDict

def tweetMessage(credentials, message):
	auth = tweepy.OAuthHandler(credentials["consumer_key"], credentials["consumer_secret"])
	auth.set_access_token(credentials["access_token"], credentials["access_secret"])

	api = tweepy.API(auth)

	api.update_status(message)

	return True
	
def main():
	optlist, args = getopt.getopt(sys.argv[1:], "hu:m:", ["user=", "message="])

	user = None
	message = None

	for o,a in optlist:
		if o in ("-h", "--help"):
			showUsage(reason="")
		elif o in ("-u", "--user"):
			if a:
				user = a
			else:
				showUsage(reason="You must provide a username")
		elif o in ("-m", "--message"):
			if a:
				message = a
			else:
				showUsage(reason="You must provide a message of max 140 characters")
		else:
			showUsage(reason="Unhandled option '%s'" % o)
	
	if len(message) > 140:
		showUsage(reason="Message is too long. Messages must be maximum 140 characters")

	credentials = validateUser(user)

	if not credentials:
		showUsage(reason="User doesn't exist.")

	if tweetMessage(credentials, message):
		print("Tweet successfully posted!")
	else:
		print("There was an error tweeting the message...")
	
if __name__ == "__main__":
	main()
