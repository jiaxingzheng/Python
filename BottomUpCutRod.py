#coding=utf-8
file=open("result.txt","w")
""
import random
n=20
data=[]
for i in range(n):
    data.append(random.randint(0,10000))
""


data=[1,5,8,9,10]
file.write("������1��"+str(len(data))+"�ĸ����ļ۸�ֱ�Ϊ:"+str(data)+"\n")

s=[0 for i in range(len(data)+1)]
def bottomUpCutRod(p):
    r=[-1 for i in range(len(p)+1)]
    r[0]=0
    for j in range(1,len(p)+1):
        for i in range(1,j+1):
            if r[j]<p[i-1]+r[j-i]:
                r[j]=p[i-1]+r[j-i]
                s[j]=i
    return r[len(p)]
            
file.write("�������Ϊ��"+str(bottomUpCutRod(data))+"\n")

length=[]
def detail(total,cut):
    if total==cut:
        return 0
    if detail(cut,s[cut])==0:
        length.append(cut)
    if detail(total-cut,s[total-cut])==0:
      	length.append(total-cut)    
    return 1
       
if detail(len(data),s[len(data)])==0 :
    file.write("���и�")
else:
    file.write("�и���ĸ�������Ϊ�ֱ�:"+str(length))
file.close()
