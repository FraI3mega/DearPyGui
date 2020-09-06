from dearpygui.dearpygui import *
add_button("Press Me", callback="callback")
def callback(sender, data):
    print("Button Pressed")
start_dearpygui()
