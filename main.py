import phonenumbers
import folium
import pywhatkit as kit 
import time 
import webbrowser
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

number = input("Enter the phone number with country code (e.g., +14155552671): ")

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print("Location:", location)

service_provider = carrier.name_for_number(pepnumber, "en")
print("Service Provider:", service_provider) 

key = "Your OpenCage API"
geocoder = OpenCageGeocode(key)

query = str(location)
results = geocoder.geocode(query)

if results:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(f"Coordinates: {lat}, {lng}")

    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)
    myMap.save("mylocation.html")

    message = f"Phone Number Tracked: {number}\nLocation: {location}\nCoordinates: {lat}, {lng}\nService Provider: {service_provider}"

    recipient_number = "The number you want the location to be delivered at"
    print(f"Sending location details to {recipient_number} via WhatsApp...")

    kit.sendwhatmsg_instantly(recipient_number, message)
    time.sleep(10)
    webbrowser.open("https://web.whatsapp.com")
else:
    print("Location not found.")
