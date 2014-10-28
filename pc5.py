# coding: utf-8

#インポートしておく
import urllib2
import pickle
import sys

#リクエストをなげて取得する
response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
sos = response.read()

#print sos
#sos = str(sos)
#sos.replace(" ","")
#sys.stdout.write(sos)

#ファイルをひらいて書き込む(なかったら作成する)
#il = open('pickle2.txt', 'w+')
#pickle.dump(sos,fil)
#fil.close()

#ロードする
mlt = pickle.loads(sos)

#fil = open('pickle.txt')
#lod = pickle.load(fil)
#fil.close()

#print 

#print lt[1]

#lt2 = set(lt)

#一つずつ取り出して掛け算リストごとに改行
for nlt in mlt:
	#print nlt
	for i in  nlt:
		ans = i[0]*int(i[1])
		sys.stdout.write(ans)
	else:
		print ("\n")

#print lt2


