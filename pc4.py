# coding: utf-8

#インポートしておく
import urllib2
import re

#リクエストをなげて取得する
response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
sos = response.read()

#print sos

#正規表現で数字だけ取り出す
pattern = re.compile('[0-9]+')
url = pattern.findall(sos)

#print url
#print url.group(0)
#400回繰り返す
for i in range(0, 400) :
	response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+url[0])
	sos = response.read()
	#数字だけ取り出す
	pattern = re.compile('[0-9]+')
	#前の数字とっておく
	url2 = url[0]
	
	#print type(url2)

	url = pattern.findall(sos)
	#print url
	#もし数字なかったら
	if not url :
		pattern2 = re.compile('two')
		two = pattern2.findall(sos)
		#twoが含まれてたら2で割る
		if two:
			#print "ない！"
			#print url2

			url2 = int(url2)
			#print url2/2
			url2 = url2/2
			url = str(url2)
		#そうでなかったら出力しておわり
		else : 
			print url2
			exit()
		
#else:
	#print url







