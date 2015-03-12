#coding=utf-8
file=open("result.txt","w")

import random
n=50
i=0
data=[]
while(i<n):
    data.append(random.randint(0,10000))
    i+=1
file.write("排序前的数列:"+str(data)+"\n")


def mergeSort(l,temp,left,right):  
    if left==right:
        return
    mid=(left+right)/2
    mergeSort(l,temp,left,mid)
    mergeSort(l,temp,mid+1,right)
    temp=list(l)
    i1=left
    i2=mid+1
    file.write("待合并的两子数列分别为："+str(l[left:mid+1])+"和"+str(l[mid+1:right+1])+"\n")
    for curr in range(left,right+1):
              if i1 == mid+1 :
                  l[curr]=temp[i2]
                  i2+=1
              elif i2>right :
                  l[curr]=temp[i1]
                  i1+=1
              elif temp[i1]<temp[i2]:
                  l[curr]=temp[i1]
                  i1+=1
              else:
                  l[curr]=temp[i2]
                  i2+=1
    file.write("合并后的数列为:"+str(l[left:right+1])+"\n")
t=[]
mergeSort(data,t,0,n-1)
file.write("排序后的数列:"+str(data)+"\n")
file.close()
