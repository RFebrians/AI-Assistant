# Asistente de voz | jarvis -> Iza
untuk menghasilkan tindakan melalui perintah suara, mengimplementasikan raspberry pi dan integrasi REST API

## Hubungkan pengeras suara dengan Bluetooth.
        systemctl is-enabled bluetooth.service
        bluetoothctl
        power on
        agent on
        scan on
        pair <F3:16:E9:1E:CC:5B>
        trust  <F3:16:E9:1E:CC:5B>
        paired-devices
        connect <F3:16:E9:1E:CC:5B>

## Environment
- Buat Environment untuk memuat Flask
        
        python -m venv env
        source env/bin/activate

- kemudian install.

        sudo apt-get install libffi-dev

        sudo apt-get install libssl-dev

        sudo apt-get install libzbar-dev libzbar0

        python -m pip install --upgrade google-assistant-library google-assistant-sdk[samples]

        python -m pip install --upgrade google-auth-oauthlib[tool]

        google-oauthlib-tool --client-secrets cred.json --scope https://www.googleapis.com/auth/assistant-sdk-prototype --scope https://www.googleapis.com/auth/gcm --save --headless

        sudo apt-get install libportaudio2

        chromium-browser --disable-web-security --user-data-dir '/home/pi'

## Hubungkan Local ke Raspberry
> The scp command uses SSH to transfer data from one host to another, and uses the same authentication and security provided by SSH.

        scp -r  app  pi@192.168.1.79:Documents/IoT/flask_api

### Pyenv ref
        https://www.liquidweb.com/kb/how-to-install-pyenv-on-ubuntu-18-04/