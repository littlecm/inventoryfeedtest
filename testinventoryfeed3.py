
# Ask for Vehicle Stock #
vehicle_stock_num = input("Please enter a vehicle stock number: ")

# Ask for Dealership Name
dealership_name = input("Please enter the dealership name: ")

# Save the information as parameters
parameters = {
    "vehicle_stock_num": vehicle_stock_num,
    "dealership_name": dealership_name
}

# Submit the parameters as a webhook
import requests
import json

url = "https://hook.us1.make.com/wj43bhw8jbw2gjjoy1b7x7dtocfmknr5"

payload = json.dumps({
  "vehicle_stock_num": "vehicle_stock_num",
  "dealership_name": "dealership_name"
})
headers = {
  'Content-Type': 'application/json',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
