# Smaug
Smaug is a simple in python written Reverse Shell

![demo](/images/demo.png)

## Installation

You need python installed to use this application

Clone the repository and cd in to it
```
git clone https://github.com/gokiimax/Smaug.git
cd Smaug
```

1. Install Requirements
```
python3 -m pip install -r requirements.txt
```

2. Configure [config.json](./config.json) and Create the payload
```
./start.bat

╭── [ Smaug@admin ]
╰──────# createpayload
```

3. Create exe from client.pyw
```
python3 -m pip install auto-py-to-exe
pyinstaller --noconfirm --onefile --console "./out/client.pyw"
```

4. Send Your new Exe file to your victim and Start the server
```
./start

╭── [ Smaug@admin ]
╰──────# start server
```

## TODO

- [x] - Config
- [x] - Create Payload
- [ ] - Obfuscation for bypass
- [ ] - Update Checker

# Credits
[![Twitter Link](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/gokimax_x)
