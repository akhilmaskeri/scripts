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

import subprocess
import threading

from getkey import getkey, keys

from enum import Enum

# change to your adb location
ADB_PATH="/Users/akhil/Library/Android/sdk/platform-tools/adb"

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
	KEYCODE_CLEAR = 28

	KEYCODE_MEDIA_PLAY_PAUSE = 85
	KEYCODE_VOLUME_DOWN = 25
	KEYCODE_VOLUME_MUTE = 164
	KEYCODE_VOLUME_UP = 24

	KEYCODE_SLEEP = 223
	KEYCODE_WAKEUP = 224
	KEYCODE_BUTTON_A = 96
	KEYCODE_BUTTON_B = 97
	KEYCODE_BUTTON_X = 99
	KEYCODE_BUTTON_Y = 100

class ACTION_METHOD():

	@staticmethod
	def swipe_down():

		command = [ADB_PATH, "shell", "input", "swipe" ] + "200 0 200 500 100".split(" ")
		adb.call(command)
		

	@staticmethod
	def swipe_up():

		command = [ADB_PATH, "shell", "input", "swipe" ] + "200 500 200 0 100".split(" ")
		adb.call(command)


class KeyBoard():

	# command mode key map
	KEY_MAP = {
		keys.H  : ANDROID.KEYCODE_DPAD_LEFT,
		keys.L  : ANDROID.KEYCODE_DPAD_RIGHT,
		keys.J  : ANDROID.KEYCODE_DPAD_DOWN,
		keys.K  : ANDROID.KEYCODE_DPAD_UP,
		keys.ENTER : ANDROID.KEYCODE_ENTER,
		keys.BACKSPACE : ANDROID.KEYCODE_BACK,               # backspace to back
		keys.SHIFT_H  : ANDROID.KEYCODE_HOME,
		keys.SHIFT_S  : ANDROID.KEYCODE_SEARCH,
		keys.SPACE  : ANDROID.KEYCODE_MEDIA_PLAY_PAUSE,
		keys.MINUS  : ANDROID.KEYCODE_VOLUME_DOWN,
		keys.EQUALS  : ANDROID.KEYCODE_VOLUME_UP,
		keys.CLOSE_PAREN  : ANDROID.KEYCODE_VOLUME_MUTE,
		keys.SHIFT_C  : ANDROID.KEYCODE_CLEAR,
		keys.A : ANDROID.KEYCODE_BUTTON_A,
		keys.X : ANDROID.KEYCODE_BUTTON_X,
		keys.B : ANDROID.KEYCODE_BUTTON_B,
		keys.Y : ANDROID.KEYCODE_BUTTON_Y,
		keys.DOWN : ACTION_METHOD.swipe_down,
		keys.UP : ACTION_METHOD.swipe_up
	}

	@staticmethod
	def getch():
		""" detect key press """
		return getkey()

	@staticmethod
	def getKeyEvent(key):
		return KeyBoard.KEY_MAP[key]


class adb():
	""" provides adb shell object """

	@staticmethod
	def call(command):
		subprocess.call(command)		

	@staticmethod
	def communicate(*command):
		subprocess.call(command)

	@staticmethod
	def input_keyevent(key_code):

		if type(key_code) is ANDROID:
			command = [ ADB_PATH, "shell", "input", "keyevent" ,str(key_code.value)]
			executionThread = threading.Thread(target=adb.communicate, args=(command) )
			executionThread.start()

		else:
			key_code()

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

	@staticmethod
	def execute_command(command):

		command = command.split(' ')

		if command[0] == "ls" or  command[0] == "list":
			adb.list_packages()
		elif command[0] == 's' or command[0] == "search":
			adb.search_package(command[1])
		elif command[0] == 'a' or command[0] == "open":
			adb.open_app(command[1])
		else:
			print(command, "no such command found")

	@staticmethod
	def list_packages():

		command = [ ADB_PATH, "shell", "pm" , "list", "packages", "-f", "|", "awk", "-F=", "'{print $NF}'"] 

		process = subprocess.Popen(command, stdout=subprocess.PIPE)
		out = process.communicate()[0]

		print(out.decode('utf-8'))

	@staticmethod
	def search_package(search_str):

		command = [ ADB_PATH, "shell", "pm" , "list", "packages", "-f", "|", "awk", "-F=", "'{print $NF}'"] 

		process = subprocess.Popen(command, stdout=subprocess.PIPE)
		out = process.communicate()[0].decode('utf-8')

		print(f"searching {search_str}")

		for pkg in out.split('\n'):
			if search_str in pkg:
				print(pkg)

	@staticmethod
	def open_app(search_str):

		command = [ ADB_PATH, "shell", "pm" , "list", "packages", "-f", "|", "awk", "-F=", "'{print $NF}'"] 

		process = subprocess.Popen(command, stdout=subprocess.PIPE)
		out = process.communicate()[0].decode('utf-8')

		print(f"searching {search_str}")

		for pkg in out.split('\n'):
			if search_str in pkg:
				command = [ ADB_PATH, "shell", "monkey", "-p", pkg, "-c", "android.intent.category.LAUNCHER", "1" ]
				process = subprocess.Popen(command, stdout=subprocess.PIPE)
				process.communicate()[0].decode('utf-8')

def navigate(key):

	try:
		key_code = KeyBoard.getKeyEvent(key)
		print(f"pressed {keys.name(key)} mapped to {key_code}")
		adb.input_keyevent(key_code)

	except Exception:
		print(f"pressed {key}:{ord(key)} but its not mapped")


def main():

	print("press CTRL_C to quit")

	while True:

		try:

			k = KeyBoard.getch()


			if k == keys.ESC:
				text = str(input("[ str ] "))
				adb.input_text(text)

			elif k == keys.COLON:
				command = str(input("[ cmd ] "))
				adb.execute_command(command)

			else:
				print("[ nav ]", end=" ")
				navigate(k)

		except KeyboardInterrupt:
			print("gracefull exiting CTRL+C")
			exit(0)

if __name__ == "__main__":
	main()
