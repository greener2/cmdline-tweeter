#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import sys, os

def dieIfNot(parameter, name):
	if not parameter:
		print("No %s provided. No action taken. Exiting...")
		sys.exit(-1)

def createTweetersTable():
	conn = sqlite3.connect("tweeters.db")
	c = conn.cursor()
	
	c.execute("""CREATE TABLE `tweeters` (`user`, `consumer_key`, `consumer_secret`, `access_token`, `access_secret`)""")

	conn.commit()

	conn.close()

def addToTweetersDB(user, consumer_key, consumer_secret, access_token, access_secret):
	if not os.path.exists("tweeters.db"):
		createTweetersTable()
	
	conn = sqlite3.connect("tweeters.db")
	c = conn.cursor()

	c.execute("""INSERT INTO `tweeters` (`user`, `consumer_key`, `consumer_secret`, `access_token`, `access_secret`) VALUES("%s", "%s", "%s", "%s", "%s")""" % (user, consumer_key, consumer_secret, access_token, access_secret))

	conn.commit()

	conn.close()

def main():
	user = raw_input("Please enter username: ")
	consumer_key = raw_input("Please input your Twitter authentication (consumer) key: ")
	consumer_secret = raw_input("Please input your Twitter authentication (consumer) secret: ")
	access_token = raw_input("Please input your Twitter access token: ")
	access_secret = raw_input("Please input your Twitter access token secret: ")

	dieIfNot(user, "username")
	dieIfNot(consumer_key, "consumer key")
	dieIfNot(consumer_secret, "consumer secret")
	dieIfNot(access_token, "access token")
	dieIfNot(access_secret, "access token secret")

	addToTweetersDB(user, consumer_key, consumer_secret, access_token, access_secret)

	print("Thanks.")

if __name__ == "__main__":
	main()
