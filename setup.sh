# commandland setup

if [ "$(uname)" == "Darwin" ]; then

	# install xcode
	xcode-select --install

	# install brew
	ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

	# setting up brew
	brew doctor

	# installing brew-cask
	brew install caskroom/cask/brew-cask
	brew install iterm2

	brew install blueutil

fi

# oh my zsh
curl https://raw.githubusercontent.com/akhilmaskeri/shell-it/master/zshrc > ~/.zshrc
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# setup vim
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
curl https://raw.githubusercontent.com/akhilmaskeri/shell-it/master/vimrc > ~/.vimrc
