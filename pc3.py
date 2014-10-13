# coding: utf-8

#インポートしておく
import re
import sys  


#ファイルを読み込む
fl = open('yukamu2.txt')
fil=fl.read()
fl.close()

#サーチして出力
pattern = re.compile('[a-z][A-Z]{3,3}[a-z][A-Z]{3,3}[a-z]')
#fid=pattern.search(fil)
fid=pattern.findall(fil)
#if fid:
	#print fid.group(0)
	#print fid.group(1)
	#print fid

#リストに入ってるものを一個ずつ取り出して改行なしで出力
for i in fid:
    #print(i[4]),
    #ans=i[4]
    #str(ans)
    sys.stdout.write(i[4])