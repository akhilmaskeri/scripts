export ZSH="/Users/hokusai/.oh-my-zsh"
ZSH_THEME="robbyrussell"
HYPHEN_INSENSITIVE="true"
DISABLE_UPDATE_PROMPT="true"
DISABLE_LS_COLORS="true"
ENABLE_CORRECTION="true"
COMPLETION_WAITING_DOTS="true"
DISABLE_UNTRACKED_FILES_DIRTY="true"

plugins=(
	git
	zsh-autosuggestions
	osx
	brew
	z
    docker
    docker-compose
    vi-mode
)

source $ZSH/oh-my-zsh.sh

if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='mvim'
fi

bindkey -s '^o' 'remote login\n'

alias python=/usr/local/bin/python3.7
alias pip=/usr/local/bin/pip3
alias airport=/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport

test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh"
