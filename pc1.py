# coding: utf-8

#インポートしておく
import re

#アルファベットをリストにつめる
chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#print chars[0]
mach = {}
#print "Please enter the uppercase letters"
print u"アルファベットを大文字で三文字入力いれて下さい。"


#添字とる
for i,keys in enumerate(chars):
	if i==24:
		mach[keys] = chars[0]
	if i==25:
		mach[keys] = chars[1]

	if i<=23:

		num = i+2
		mach[keys] = chars[num]


#print "The first character?"
#key1=raw_input()
#print "Two-th character?"
#key2=raw_input()
#print "Three-th character?"
#key3=raw_input()

#正規表現でしぼる
key=raw_input()
pattern = re.compile('[A-Z]{3.3}')
if pattern.match(key):          #key in chars: #and key==[A-Z]+[A-Z]+[A-Z]:  len(key)==3 and 
	
	words = list(key)
	key1=words[0]
	key2=words[1]
	key3=words[2]
else :
	#print u"三文字のアルファベットを入力してください"
	#メッセージを出して終了する
	 exit(u"三文字の大文字アルファベット以外のものが入力されたので終了します！！") 


	
#結果を出力する
print mach[key1]+mach[key2]+mach[key3]




	