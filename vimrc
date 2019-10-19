" make vim try to detect file types and load plugin for them
filetype on
filetype plugin on
filetype indent on

set encoding=utf-8 " encoding is utf-8
scriptencoding utf-8
set fileencoding=utf-8

set backspace=indent,eol,start
set hidden " unabandoned buffer
set cursorline " Highlight the current line
set fileformats=unix,dos " set unix line endings
set viminfo='100,f1 " save upto 100 marks , enable capital marks

set ruler
set background=dark
set nocompatible

set rnu

set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()

Plugin 'gmarik/Vundle.vim'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'scrooloose/syntastic'   "syntax checking
Plugin 'nvie/vim-flake8'	"static syntax and style checker
Plugin 'scrooloose/nerdtree'
Plugin 'ervandew/supertab'
Plugin 'raimondi/delimitmate'
Plugin 'ivalkeen/nerdtree-execute'
Plugin 'ctrlpvim/ctrlp.vim'
Plugin 'nathanaelkane/vim-indent-guides'
Plugin 'terryma/vim-expand-region'
Plugin 'danro/rename.vim'
Plugin 'vim-scripts/IndexedSearch'
Plugin 'mattn/emmet-vim'
Plugin 'othree/html5.vim'
Plugin 'hail2u/vim-css3-syntax'
Plugin 'ap/vim-css-color'
Plugin 'chrisbra/colorizer'
Plugin 'sirver/ultisnips'
Plugin 'itchyny/lightline.vim'
Plugin 'sjl/badwolf'
Plugin 'mizuchi/stl-syntax'
Plugin 'elzr/vim-json'
Plugin 'pangloss/vim-javascript'
Plugin 'Yggdroot/indentLine'

call vundle#end()

let python_highlight_all=1
let g:javascript_plugin_jsdoc = 1
let g:javascript_plugin_ngdoc = 1
let g:javascript_plugin_flow = 1


set runtimepath+=~/.vim/ultisnips_rep/

let g:lightline = {
      \ 'colorscheme': 'PaperColor',
      \ 'component': {
      \   'readonly': '%{&readonly?"\ue0a2":""}',
      \ 'active': {
      \   'left': [ ['readonly'] ,[ 'mode', 'paste' ], [ 'fugitive', 'filename' ], ['ctrlpmark'] ],
      \   'right': [ [ 'syntastic', 'lineinfo' ], ['percent'], [ 'fileformat', 'fileencoding', 'filetype' ] ]
      \ },
      \   'modified': '%{&filetype=="help"?"":&modified?"\u2756":&modifiable?"":"\u2796"}'
      \ },
      \ 'component_visible_condition': {
      \   'readonly': '(&filetype!="help"&& &readonly)',
      \   'modified': '(&filetype!="help"&&(&modified||!&modifiable))'
      \ },
      \ 'subseparator': { 'left': " \u20d2", 'right': " \u20d2" }
      \ }

" 		Currently, wombat, solarized, powerline, jellybeans, Tomorrow,
"       Tomorrow_Night, Tomorrow_Night_Blue, Tomorrow_Night_Eighties,
"    	PaperColor, seoul256, landscape, one, Dracula, Molokai and 16color are available.


set laststatus=2

" enable matchit plugin
runtime macros/matchit.vim

set autoread
set backupcopy=yes

set lazyredraw

set wildmenu

" Spell check on
set spell spelllang=en_us
setlocal spell spelllang=en_us

" Where it should get the dictionary files
let g:spellfile_URL = 'http://ftp.vim.org/vim/runtime/spell'


set foldenable
set foldlevelstart=10

" Set automatic indentation
set autoindent
set smartindent

" Tab = 4 spaces
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab

" Show matching [] and {}
set showmatch

set number

" Smart case sensitivity for searches (both required to work)
set ignorecase
set smartcase
set ruler
set showcmd

" Search live
set incsearch

syntax on

set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*


" Disable delimitMate auto-closing for <>
let delimitMate_matchpairs = "(:),[:],{:}"

let g:ctrlp_user_command = ['.git/', 'git --git-dir=%s/.git ls-files -oc --exclude-standard']

colorscheme badwolf 

" key - mappings 
"---------------

let mapleader = "\ "
"f1 toggle help text

"f3 toggles search highlighting
set hlsearch
noremap <F3> :set hlsearch!<CR>

"f4 toggles line numbers
noremap <F4> :set number!<CR>

"Disable bells
set visualbell
set t_vb=

" clear search markings
nnoremap <silent> <leader>x :noh<CR>
nnoremap <leader>d :%s/
nnoremap <leader>w :w<CR>
nnoremap <leader>q :x<CR>
nnoremap <leader>e :q!<CR>
nnoremap <leader>s :!
nnoremap <leader>a :r ~/code/snippets/
nnoremap <Leader>t :tabnew 
nnoremap <F8> :!open -a firefox %<CR>

nnoremap <leader>/ ^i//
 
nnoremap <leader>r :r 
map <S-Right> gt
map <S-Left> gT
map f <C-f>
map <C-l> gt
map <C-h> gT
map <C-n> :NERDTreeToggle<CR>

map <C-Down> :m .+1<CR>==
map <C-Up> :m .-2<CR>==

map H ^
map L $

iabbrev </ </<C-X><C-O>

inoremap jk <esc>

inoremap {      {}<Left>
inoremap {<CR>  {<CR>}<Esc>O}}
inoremap(       ()<Left>
noremap {{      {
noremap {}      {}

map <S-Down> <Esc>vj+
map <S-Up> <Esc>vk-

"inoremap  <Up>     <NOP>
"inoremap  <Down>   <NOP>
"inoremap  <Left>   <NOP>
"inoremap  <Right>  <NOP>
"noremap   <Up>     <NOP>
"noremap   <Down>   <NOP>
"noremap   <Left>   <NOP>
"noremap   <Right>  <NOP>
