Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class BankAccount:
  import requests, json
i = 1
while i > 0:
  print("Welcome to your weather information")
  print("Enter your zip code for weather updates")
  zip_code = input()
  if int(zip_code) > 99999:
      print("Invalid Zip Code")
  url = "api.openweathermap.org/data/2.5/weather?zip="
  api_key = "e01edca2f2ae0c287a0f0c87c27b726e"
  complete_url = url + zip_code +"&appid=" + api_key
  response = requests.get(complete_url).json

  today_sunrise  = current.sunrise
  today_sunset = current.sunset
  print("Today the sun rose at " + today_sunrise + " and the sun will go down at " + today_sunset)
  current_temp = current.weather
  print("The current tempature is " + current_temp)
  print("Would you like to look up another zip code? y/n")
  user_continue = input()
  if user_continue == "n":
    break
print("Have a wonderful day!") 
