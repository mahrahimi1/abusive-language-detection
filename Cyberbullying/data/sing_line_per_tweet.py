from __future__ import print_function
import getopt
import logging
import os
import sys

if __name__ == '__main__':
	idfilepath = 'data'
	with open(idfilepath, 'r') as idfile:
		for line in idfile:
			user_id, label, tweet_ids = line.split('\t')
			tweet_ids = tweet_ids.strip()
			tweet_id_list = tweet_ids.split(',')
			for tweet_id in tweet_id_list:
				print('%s,%s,%s' % (user_id, label, tweet_id))
