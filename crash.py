import urllib
import sys, getopt
import random
import string
import urllib2
def makePassword(minLength=8,maxLength=15):
    length=random.randint(minLength,maxLength)
    letters=string.ascii_letters+string.digits
    return ''.join([random.choice(letters) for _ in range(length)])
loopTimes=100+1
showCtrl=1
try:
    options,args = getopt.getopt(sys.argv[1:],"ht:d")
    for opt, arg in options:
        if opt == '-h':
            print 'crash.py -t loop times, default 100 times;\n         -d disable show received data, default show'
            sys.exit()
        elif opt == '-t':
            loopTimes=int(arg)+1
        elif opt=='-d':
            showCtrl=0
           # print showCtrl
except getopt.GetoptError :
    loopTimes=100+1#default loop times
for i in range(1,loopTimes):
    userId=random.randint(1000000000,2000000000);
    userPsd=makePassword()
    postData = {'u':str(userId),'p':userPsd,'verifycode':''}
    postEncode=urllib.urlencode(postData)
    
    reqUrl="http://qinhuangdao.edeng.cn.w.kunlunea.com/yiti/ht/save3.asp"
    
    req=urllib2.Request(url=reqUrl,data=postEncode)
    #print str(showCtrl)+"  sctrl\n"
    if(showCtrl==1) :
        print "loop times "+str(i)+" : \nrandom userId :"+str(userId)+"  random password :"+userPsd
    
    resData=urllib2.urlopen(req)
    res=resData.read()
    if(showCtrl==1):
        print res+"\n"
