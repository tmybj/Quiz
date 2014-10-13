# coding: utf-8

from collections import Counter

#ファイルを読み込む
fl = open('yukamu.txt')
fil=fl.read()
words=list(fil)
fl.close()

#文字数をカウントする
counter = Counter(words)
for word, cnt in counter.most_common():
    print word, cnt


#print word 