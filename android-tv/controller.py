"""

    this script is just a controller
    you have to connect to tv before
    adb should have your tv in devices list

    keys have to mapped manually
    https://developer.android.com/reference/android/view/KeyEvent.html#KEYCODE_AT

    
    process provides 2 modes command and search 
    in command mode you move around
    in search mode you type into the search bar

    the command mode key map has to be manually defined
    this one works well with mac
    
"""

import tty
import sys
import termios
import subprocess
import threading

# change to your adb location
ADB_PATH="/Users/hokusai/Library/Android/sdk/platform-tools/adb"

# command mode key map
command_key_map = {
    ord('h')  : 21,
    ord('l')  : 22,
    ord('j')  : 20,
    ord('k')  : 19,
    ord('\r') : 66,     # enter
    127       :  4,     # backspace to back
    43        : 24,     # 
    95        : 25,     # home
    72        : 3,
    83        : 84

}

# insert mode key map
alphabets  = { c:(c-68) for c in range(ord('a'),ord('z')+1) }
numericals = { c:(c-42) for c in range(ord('0'),ord('9')+1) }
other_keys = {
     32 : 62, # space to space
    127 : 67, # backspace to delete
}
insert_key_map = {**alphabets, **numericals, **other_keys}


class KEY():

    def __init__(self):
        self.modes = {
            "command" : command_key_map,
            "search"  : insert_key_map
        }

        self.mode = "command"
    
    def toggleMode(self):
        """ toggle from command to search """
        if self.mode == "command":
            self.mode = "search"
        else:
            self.mode = "command"

    def getch(self):
        """ detect key press """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ch
    
    def getKeyCode(self,key):
        """ return keycode based on mode """
        return str( self.modes[self.mode][ord(key)] )


class adb():
    """ provides adb shell object """

    @staticmethod 
    def input(key_code):

        def communicate(*command):
            subprocess.call(command)

        command = [ ADB_PATH, "shell","input", "keyevent" ,str(key_code)]        
        executor = threading.Thread(target=communicate, args=(command) )
        executor.start()


def main():

    key   = KEY()
    shell = adb()

    print(f"press CTRL+C to exit")
    print(f"entered in [{key.mode}]")

    while True:

        x = key.getch()

        if ord(x) == 3:
            print("gracefull exiting CTRL+C")
            break
            
        elif ord(x) == 27:
            key.toggleMode()
            print(f"[{key.mode}]")
        else:
            try:        
                key_code = key.getKeyCode(x)
                shell.input(key_code)
                print(f"[ {key.mode} ] pressed {x}  {ord(x)}")
            except Exception:
                print("you pressed", ord(x), "but no such keys are mapped")

if __name__ == "__main__":
    main()