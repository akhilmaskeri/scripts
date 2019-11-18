"""


	Androd device controller based on adb
	The keys have to be mapped manually
	Please refer the constants to get the key

	process provides 2 modes command and search
	in command mode you move around
	in search mode you type into the search bar

	the command mode key map has to be manually defined
	this one works well with mac

	esc to search mode -> type in the text -> ENTER

"""

import tty
import sys
import termios
import subprocess
import threading

from enum import Enum

# change to your adb location
ADB_PATH="/Users/hokusai/Library/Android/sdk/platform-tools/adb"

class ANDROID(Enum):

	KEYCODE_DPAD_CENTER = 23
	KEYCODE_DPAD_DOWN = 20
	KEYCODE_DPAD_LEFT = 21
	KEYCODE_DPAD_RIGHT = 22
	KEYCODE_DPAD_UP = 19

	KEYCODE_BACK = 4
	KEYCODE_ENTER = 66
	KEYCODE_HOME = 3
	KEYCODE_SEARCH = 84

	KEYCODE_MEDIA_PLAY_PAUSE = 85
	KEYCODE_VOLUME_DOWN = 25
	KEYCODE_VOLUME_MUTE = 164
	KEYCODE_VOLUME_UP = 24

	KEYCODE_SLEEP = 223
	KEYCODE_WAKEUP = 224



class KeyBoard():

	# command mode key map
	KEY_MAP = {

		ord('h')  : ANDROID.KEYCODE_DPAD_LEFT,
		ord('l')  : ANDROID.KEYCODE_DPAD_RIGHT,
		ord('j')  : ANDROID.KEYCODE_DPAD_DOWN,
		ord('k')  : ANDROID.KEYCODE_DPAD_UP,
		ord('\r') : ANDROID.KEYCODE_ENTER,
		127       : ANDROID.KEYCODE_BACK,     # backspace to back
		ord('H')  : ANDROID.KEYCODE_HOME,
		ord('S')  : ANDROID.KEYCODE_SEARCH,
		ord(' ')  : ANDROID.KEYCODE_MEDIA_PLAY_PAUSE,
		ord('-')  : ANDROID.KEYCODE_VOLUME_DOWN,
		ord('=')  : ANDROID.KEYCODE_VOLUME_UP,
		ord(')')  : ANDROID.KEYCODE_VOLUME_MUTE,
	}


	@staticmethod
	def getch():
		""" detect key press """

		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)

		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)

		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

		return ch

	@staticmethod
	def getKeyEvent(key):
		return KeyBoard.KEY_MAP[ord(key)]


class adb():
	""" provides adb shell object """

	@staticmethod
	def communicate(*command):
		subprocess.call(command)

	@staticmethod
	def input_keyevent(key_code):
		command = [ ADB_PATH, "shell", "input", "keyevent" ,str(key_code)]
		executionThread = threading.Thread(target=adb.communicate, args=(command) )
		executionThread.start()

	@staticmethod
	def input_text(text):

		print(f"sending {text}")
		text = text.replace(" ","%s")
		command = [ ADB_PATH, "shell", "input", "text" , text]
		print(" ".join(command))

		executionThread = threading.Thread(target=adb.communicate, args=(command) )
		executionThread.start()
		executionThread.join()

		adb.input_keyevent(ANDROID.KEYCODE_ENTER.value)


def navigate():

	print(f"press CTRL+C to exit")

	while True:

		key = KeyBoard.getch()

		if ord(key) == 3:
			print("gracefull exiting CTRL+C")
			break

		elif ord(key) == 27:
			text = str(input("[ str ] "))
			adb.input_text(text)

		else:

			try:
				key_code = KeyBoard.getKeyEvent(key)
				print(f"[cmd] pressed {key} mapped to {key_code}")
				adb.input_keyevent(key_code.value)

			except Exception:
				print(f"[cmd] pressed {key}:{ord(key)} but its not mapped")

if __name__ == "__main__":
	navigate()
