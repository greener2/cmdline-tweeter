#Cmdline-tweeter

A simple command line tweet application. This was constructed mainly as a learning instrument, but I may expand it into something more useful.

#Usage Details

To make use of this app, first get your consumer key, consumer secret, access token and access token secret from the Twitter developers' site (dev.twitter.com). There's a different one per account.

To add a user account, run `python add_tweeter.py`. This will allow you to input your Twitter account name (complete with '@' symbol), and the keys/tokens/secrets outlined on the developers' page. This information is stored in tweeters.db in the same directory.

To actually tweet something, run the `tweeter.py` app as follows:

	`python tweeter.py --username=@TwitterUser --message="Here is my message to the world!"`

For full usage information on either of the scripts in the application, simply run the script with the `-h/--help` option.

#Credits
Author: Rob Greene
Email: greener2 -at- gmail.com
