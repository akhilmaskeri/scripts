if [ "$(uname)" == "Darwin" ]; then

	#install xcode
	xcode-select --install

	#install brew
	ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

	#setting up brew
	brew doctor

	#installing brew-cask
	brew install caskroom/cask/brew-cask

	#oh my zsh
	sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
	
fi
