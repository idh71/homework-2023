import requests


# url = 'http://localhost:5000/predict'

customer_id = 'deabeat'
# client =  {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}

url = 'http://localhost:9696/predict'
client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
# requests.post(url, json=client).json()




response = requests.post(url, json=client).json()
print(response)

if response['churn'] == True:
    print('Congratulations! You have been approved,  %s' % customer_id)
else:
    print("Sorry %s, you don't qaulify.  Hit the bricks. " % customer_id)