
#스티브잡스의 연설문에 긍정단어가 몇개 있는지 확인하는 코드
#스티브 잡스의 연설문을 단어 단위로 끊어서 읽어오기
stev=open("d:\\data\\jobs.txt",encoding='UTF8')
stev2=stev.read().split()

#긍정단어 리스트 만들기
positive=open("d:\\data\\positive-words.txt")
pos=positive.read().split()

#스티브 잡스의 연설문에 긍정 단어가 몇개인지 확인하기
cnt=0
for i in stev2:
    if i.lower() in pos:
        cnt+=1
print(cnt)