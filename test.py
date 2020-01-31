import requests

url = 'https://reqres.in/api/users?page=2'
r = requests.get( url)
print(r)
data = r.text
Dict=eval(data)
list1=Dict['data']
#print(list1[1])
for i in range(len(list1)):
    print(list1[i]['first_name']+' '+list1[i]['last_name'])


    
