Here's a **professional and detailed GitHub README** incorporating all the materials you have:  

---

### **📌 SIM Tracer - Phone Number Tracker & WhatsApp Notifier**  

A Python-based **SIM Tracer** that extracts **location, service provider, and geographic coordinates** of a phone number. The location details are automatically **sent via WhatsApp Web** to a predefined recipient.  

---

## **🚀 Features**  

✅ Tracks the location of a phone number  
✅ Identifies the telecom service provider  
✅ Fetches precise latitude and longitude coordinates using **OpenCage API**  
✅ Generates an interactive **map with the traced location**  
✅ Sends location details via **WhatsApp Web**  
✅ Works seamlessly on **Windows, macOS, and Linux**  

---

## **📂 Project Structure**  

```
📦 Sim-Tracer
 ┣ 📜 main.py                 # Main Python script
 ┣ 📜 requirements.txt         # Dependencies
 ┣ 📜 pyWhatKit_DB.txt         # WhatsApp message log file
 ┣ 📂 assets/                  # Screenshots & recordings
 ┃ ┣ 📜 run_to_message_sent.mp4  # Screen recording of execution
 ┃ ┣ 📜 traced_location.png     # Screenshot of traced location
 ┃ ┣ 📜 pyWhatKit_DB.png        # Screenshot of the WhatsApp log
 ┣ 📜 README.md                # Project documentation
```

---

## **📸 Screenshots & Demonstration**  

### **🎥 Full Execution Recording:**  
_A screen recording showing the script running from execution to WhatsApp message delivery._  
📌 ****  

### **📍 Traced Location Preview:**  
_A screenshot showing the location opened in Google Chrome._  
![Screenshot 2025-03-15 202226](https://github.com/user-attachments/assets/8b4f16b7-89f9-45d0-8a7c-34cdecefccc0)


### **📜 pyWhatKit Log File:**  
_A screenshot of `pyWhatKit_DB.txt` storing WhatsApp message logs._  
![Screenshot 2025-03-15 202243](https://github.com/user-attachments/assets/0ff06185-1f0f-4ea5-bdcc-a370f7193c43)
  

---

## **⚙️ Installation & Setup**  

### **🔹 Prerequisites**  
Ensure you have **Python 3.8+** installed. Install the required dependencies using:  
```sh
pip install -r requirements.txt
```

### **🔹 Dependencies**  
The following libraries are used in this project:  
```sh
pip install phonenumbers
pip install folium
pip install pywhatkit
pip install opencage
```

---

## **🛠 Usage**  

1️⃣ **Run the script:**  
```sh
python main.py
```
2️⃣ **Enter the phone number** (including country code):  
   ```
   Enter the phone number with country code (e.g., +14155552671):
   ```  
3️⃣ **The script fetches:**  
   - The country and region of the phone number  
   - The telecom provider  
   - The latitude and longitude  
4️⃣ **Generates a map** (`mylocation.html`)  
5️⃣ **Sends the details via WhatsApp Web**  

---

## **💡 Example Output**  

```
Location: California, United States
Service Provider: Verizon
Coordinates: 37.7749, -122.4194
Map saved as 'mylocation.html' — Open it in a browser to view.
Sending location details to +919354248891 via WhatsApp...
Message sent successfully!
```

---

## **🔐 API Configuration**  

This script uses **OpenCage API** for geolocation services.  

1. **Get an API key** from [OpenCage Geocoder](https://opencagedata.com/api)  
2. Replace `YOUR_OPENCAGE_API_KEY` in `main.py` with your key:  
   ```python
   key = "YOUR_OPENCAGE_API_KEY"
   ```

---

## **⚠️ Important Notes**  

🔹 This script **does not track real-time movement**, it fetches only the registered location of the number.  
🔹 The **WhatsApp Web session must be logged in** for automatic message sending.  
🔹 `pyWhatKit_DB.txt` stores logs of messages sent via WhatsApp.  

---

## **👨‍💻 Contributing**  

Want to enhance this project? Feel free to fork, improve, and submit a pull request! 🚀  

---

## **📜 License**  

This project is licensed under the **MIT License**.  

