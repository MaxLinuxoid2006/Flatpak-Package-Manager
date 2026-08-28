import os
import tkinter
from tkinter import *
window = Tk()
window.title('Flatpak Package Manager')
window.geometry('350x380')
lbl = Label(window, text='Welcome to program: Flatpak Package Manager')
lbl.grid(column=0, row=0)
lbl = Label(window, text='Select operation:')
lbl.grid(column=0, row=1)
def flatpakupdate():
    os.system('flatpak update')
bt1 = Button(window, text='Update', command=flatpakupdate)
bt1.grid(column=0, row=2)
def install():
    print('Enter the command “flatpak install package_name”')
bt2 = Button(window, text='Install', command=install)
bt2.grid(column=0, row=3)
def remove():
    print('Enter the command “flatpak remove package_name”')
bt3 = Button(window, text='Remove')
bt3.grid(column=0, row=4)
def flatpaklist():
    os.system('flatpak list')
bt4 = Button(window, text='List', command=flatpaklist)
bt4.grid(column=0, row=5)
def run():
    print('Enter the command “flatpak run package_name”')
bt5 = Button(window, text='Run')
bt5.grid(column=0, row=6)
def flatpak():
    window = Tk()
    window.title('Select Package Manager')
    window.geometry('200x200')
    lbl = Label(window, text='Select Package Manager:')
    lbl.grid(column=0, row=0)
    def apt():
        os.system('sudo apt install flatpak')
    bt1 = Button(window, text='APT', command=apt)
    bt1.grid(column=0, row=1)
    def dnf():
        os.system('sudo dnf install flatpak')
    bt2 = Button(window, text='DNF', command=dnf)
    bt2.grid(column=0, row=2)
    def pacman():
        os.system('sudo pacman -S flatpak')
    bt3 = Button(window, text='PACMAN', command=pacman)
    bt3.grid(column=0, row=3)
    def emerge():
        os.system('emerge --ask --verbose sys-apps/flatpak')
    bt4 = Button(window, text='EMERGE', command=emerge)
    bt4.grid(column=0, row=4)
    def zypper():
        os.system('sudo zypper install flatpak')
    bt5 = Button(window, text='ZYPPER', command=zypper)
    bt5.grid(column=0, row=5)
bt6 = Button(window, text='Install Flatpak', command=flatpak)
bt6.grid(column=0, row=7)
def plugin():
    window = Tk()
    window.title('Select DE')
    window.geometry('100x100')
    lbl = Label(window, text='Select DE:')
    lbl.grid(column=0, row=0)
    def gnome():
        os.system('sudo apt install gnome-software-plugin-flatpak')
    bt1 = Button(window, text='GNOME', command=gnome)
    bt1.grid(column=0, row=1)
    def kde():
        os.system('sudo apt install plasma-discover-backend-flatpak')
    bt2 = Button(window, text='KDE', command=kde)
    bt2.grid(column=0, row=2)
bt7 = Button(window, text='Install Plugin', command=plugin)
bt7.grid(column=0, row=8)
def repository():
    os.system('flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo')
bt8 = Button(window, text='Add Repository Flathub')
bt8.grid(column=0, row=9)
def about():
    window = Tk()
    window.title('About Program')
    window.geometry('300x130')
    lbl = Label(window, text='Name Program: Flatpak-Package-Manager')
    lbl.grid(column=0, row=0)
    lbl = Label(window, text='Version: 1.0')
    lbl.grid(column=0, row=1)
    lbl = Label(window, text='Language & Version: Python 3.13.5')
    lbl.grid(column=0, row=2)
    lbl = Label(window, text='Lisence: Free & Open Source GNU GPL')
    lbl.grid(column=0, row=3)
    lbl = Label(window, text='Develop: MaxLinuxoid2006')
    lbl.grid(column=0, row=4)
bt9 = Button(window, text='About Program', command=about)
bt9.grid(column=0, row=10)
lbl = Label(window, text='Developer: MaxLinuxoid2006')
lbl.grid(column=0, row=11)
window.mainloop()