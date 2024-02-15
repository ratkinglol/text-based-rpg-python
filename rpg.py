import time
import random

# game config
start_screen = 0
settings = 0

# settings config
ASCII_Art = 1

def start1():
  print("starting game...")
  time.sleep(1)
  print("")
  stat_thing = input("")

#actual game
def start():
  global start_screen, settings
  start_screen = 1
  settings = 0
  while True:
    start__settings_input = input("Start the game? (type settings to enter settings and start/s to start) : ")
    print("")
    if start__settings_input.lower() == "start" or start__settings_input.lower() == "s":
      start1()
      break
    elif start__settings_input.lower() == "settings" or start__settings_input.lower() == "setting":
      settings = 1
      settings_select__input = input("There are 3 setting types, UI, Save Menu, and Controls (type ui/u for ui, type save/save menu/s for save menu, or type control/controls/c for controls) : ")
      print("")
      if settings_select__input.lower() == "ui" or settings_select__input.lower() == "u":
        if ASCII_Art = 1:
          ui_input = input("Currently there is 1 UI setting, would you like to disable ASCII Art? : ")
          if ui_input.lower() == "y" or ui_input.lower() == "yes" or ui_input.lower() == "yea" or ui_input.lower() == "ye":
            ASCII_Art = 0
        elif ASCII_Art == 1:
          ui_input = input("Currently there is 1 UI setting, would you like to enable ASCII Art? : ")
          if ui_input.lower() == "y" or ui_input.lower() == "yes" or ui_input.lower() == "yea" or ui_input.lower() == "ye":
            ASCII_Art = 1
      elif settings_select__input.lower() == "save" or settings_select__input.lower() == "save menu" or settings_select__input.lower() == "s":
        save_input = print("Currently there are no save menu option(s)")
      elif settings_select__input.lower() == "control" or settings_select__input.lower() == "controls" or settings_select__input.lower() == "s":
        print("Currently there are no control(s) settings")
      elif settings_select__input.lower() == "q" or settings_select__input.lower() == "quit" or settings_select__input.lower() == "x" or settings_select__input.lower() == "exit" or settings_select__input.lower() == "exit settings":
        settings = 0
      else:
        settings = 0

start()

