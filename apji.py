COLORS = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    
    'bg_black': '\033[40m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_yellow': '\033[43m',
    'bg_blue': '\033[44m',
    'bg_magenta': '\033[45m',
    'bg_cyan': '\033[46m',
    'bg_white': '\033[47m',
    
    'bold': '\033[1m',
    'underline': '\033[4m',
    'blink': '\033[5m',
    'reverse': '\033[7m',
    'conceal': '\033[8m',
    
    'reset': '\033[0m',
}

def c(text, *styles):
    result = ''
    for style in styles:
        if style in COLORS:
            result += COLORS[style]
    result += text
    if styles:
        result += COLORS['reset']
    return result

import sys, time, os, requests

def at(text, delay=0.05, fast=False):
    if fast:
        delay = 0.01
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

version = '0.1a'

def update_script():
    try:
        url = "https://github.com/nyantvar/archperfection/blob/main/apji.py"
        response = requests.get(url)
        response.raise_for_status()
        
        current_content = open(__file__, 'r').read()
        if current_content == response.text:
            return False
        
        with open(__file__, 'w') as f:
            f.write(response.text)
        
        return True
    except:
        return False

print('-')
at(c('APji - ArchPerfection','green','bold'),delay=0.020)
at(c('Юзер-френдли интерфейс для конфигурации и кастомизации Арчподобных-систем','cyan'),delay=0.010)
at(c('-\nhelp - список команд.','bold'),delay=0.015)
while True:
    user = input('> ')
    if user == 'help':
        print(c('- Системное','green','bold'))
        print(c('psyu - обновление пакетов','yellow','bold'))
        print(c('cache -clear - очистка кэша','yellow','bold'))
        print(c('ongp - оптимизация gnome-desktop','yellow','bold'))
        print(c('- Авто-установочник','green','bold'))
        print(c('eiyay - установить yay','yellow','bold'))
        print(c('- Настройки','green','bold'))
        print(c('update - обновить скрипт','yellow','bold'))
        print(c('bye - выйти','yellow','bold'))
    elif user == 'update':
        print(f'Текущая версия: {version}')
        print('Выполняю обновление..')
        if update_script():
            print(c('Скрипт обновлен. Перезапустите для применения изменений.','green','bold'))
        else:
            print(c('Обновление не требуется!.','green','bold'))
    elif user == 'bye':
        sys.exit()
    elif user == 'eiyay':
        os.system('sudo pacman -S --needed git base-devel')
        os.system('sudo mkdir -p /yay')
        os.system('sudo git clone https://aur.archlinux.org/yay.git')
        os.system('sudo cd /yay')
        os.system('makepkg -si')
        os.system('sudo echo "[multilib]" > /etc/pacman.conf')
        os.system('sudo echo "Include = /etc/pacman.d/mirrorlist" > /etc/pacman.conf')
        os.system('sudo pacman -Syu')
    elif user == 'ongp':
        print(c('Секунду..','yellow','bold'))
        os.system('sudo systemctl disable geoclue-agent')
        os.system('sudo systemctl mask tracker-extract-3.service tracker-miner-fs-3.service tracker-miner-rss-3.service tracker-writeback-3.service tracker-xdg-portal-3.service')
    elif user.startswith('cache'):
        if user == 'cache':
            print(c('И что ты предлагаешь мне с этим делать?','red','bold'))
        elif user == 'cache -clear':
            print(c('Секунду..','yellow','bold'))
            os.system('rm -rf ~/.cache/gdm')
            os.system('rm -rf ~/.cache/gnome-*')
            os.system('rm -rf ~/.cache/*')
            os.system('rm -rf ~/.cache/yay/')
            os.system('sudo pacman -Sc')
    elif user == 'psyu':
        os.system('sudo pacman -Syu')
    elif user == '':
        print(c('Пустая строка, серьёзно?','red','bold'))
    else:
        print(c('Команда не найдена.','red','bold'))
