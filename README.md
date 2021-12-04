# wireguard-disallow-ips

With this tool you can easily allow some traffic to bypass the VPN. There is no `DisallowedIPs` property in wireguard configs, but you can do this by specifying only the `AllowedIPs` property.

## Install
```
pip install -r requirements.txt
```

## Usage

1. Create `input.txt` file and write hosts to be processed without VPN:
   ```
   yandex.ru
   mail.yandex.ru
    
   google.com
   ```
   
2. Make sure that you have disabled your vpn and run the script.
   ```
   python3 main.py
   ```
3. Copy AllowedIPs from console of from `allowed.ips` file and paste it into your wireguard client config. Make sure that `Block untunneled traffic` is disabled.