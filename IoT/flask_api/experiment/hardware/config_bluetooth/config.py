import os
import subprocess
import inquirer

class ConfigBluetooth:
    
    @staticmethod
    def apply_comand(comand:str, response:bool=True) -> None:
        if response:
            res = os.popen(comand.split(',')).read()
            return res.strip()
        os.popen(comand)
    
    def active_internal_device(self) -> bool:
        res = self.apply_comand('systemctl is-enabled bluetooth.service')
        if res  == 'enabled':
            while True:
                r = self.apply_comand('bluetoothctl,power on, agent on , scan on')
                print(r)
            return True
        return False
 

    def manage(self):
        active = self.active_internal_device()


def main() -> None:
    blue = ConfigBluethoot()
    blue.manage()


if __name__=='__main__':
    main()
