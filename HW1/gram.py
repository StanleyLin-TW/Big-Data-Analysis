from operator import itemgetter
F=open("test.txt",'r',encoding="UTF-8")
Output1=open("result.txt",'w')
Output2=open("freq_japan_6.txt",'w')
#print(F.read())
#smylist="睡覺囉"
def list2freqdict(mylist):
    mydict=dict()
    for ch in mylist:
        mydict[ch]=mydict.get(ch,0)+1
    return mydict
#print(type(F.read()))

sentence=filter(str.isalpha, F.read()) 
#print(sentence)
#print(type(sentence))
#x=0
chlist=[ch for ch in sentence]
def list2bigram(mylist):
	print("progressing")
	return [mylist[i:i+6] for i in range(0,len(mylist)-5)]
def bigram2freqdict(mybigram):
    mydict=dict()
    print("freq")
    for (ch1,ch2,ch3,ch4,ch5,ch6) in mybigram:
        mydict[(ch1,ch2,ch3,ch4,ch5,ch6)]=mydict.get((ch1,ch2,ch3,ch4,ch5,ch6),0)+1
    return mydict
def freq2report(freqlist):
    chs=str()
    for (token,num) in freqlist:
        for ch in token:
            chs=chs+ch
        a=chs
        b=str(num)
        Output1.write(a)
        Output2.write(b)
        Output1.write('\n')
        Output2.write('\n')
        chs=''
    return
chbigram=list2bigram(chlist)
print(chbigram)


chbifreq=bigram2freqdict(chbigram)
print(chbifreq)

bigramfreqsorted=sorted(chbifreq.items(), key=itemgetter(1), reverse=True)
bigramfreqsorted=bigramfreqsorted[:1000]
print(bigramfreqsorted)
result=freq2report(bigramfreqsorted)
#chtrigram=list2trigram(chlist)
print(result)
