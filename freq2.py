import requests
  
url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
r = requests.get( url)
print(r)  
data = r.text 
list1=data.split('\n')
ipcount={}

for i in range(len(list1)):
    list2=list1[i].split("- -")
    if(list2[0] in ipcount):
        count=ipcount.get(list2[0])
        ipcount[list2[0]]=count+1
    else:
        ipcount[list2[0]]=1
j=0
str1=""
for ip,count1 in ipcount.items():
    if count1>j:
        j=count1
        str1=ip
print(str1)
print(j)



      

    

