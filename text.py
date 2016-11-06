import curses

'''
Each text object is a tuple, stored as ("text", UID, "POS").

"UID" is a three-digit number that allows you to access the text to change its properties and position other text relative to it:
    - 000 is a reserved (and unused) UID.
    - UIDs with low numerical values are generally reserved for static text
    - If the text is part of the player's input and feedback, then * is placed at the front of it.
        This indicates that whenever the user presses enter it is to scroll up with the rest of the text.

"POS" is the position of the text, and is formatted with special characters:
    ! indicates absolute number of characters away,
    % indicates percentage of the screen away.
    The position is written as !y!x, !y%x, %y!x, or %y%x.
    You can indicate that this is positioned relative to another string by placing ^UID at the front of the string,
        where UID is the string being positioned from's UID.

Text formats are stored in strings with special characters:
    !text!  indicates bold text,
    /text/  indicates italic text,
    _text_  indicates underlined text,
    #XXXXXX indicates a hex color for all following text (the default is #000000)

OBVIOUS DO-NOTS:
    - Do not position text relative to itself
    - Close all your formats!
'''

#TODO: great, now implement it.

#this keeps track of all the text that we have onscreen
_onScreenText = []

#resets the display to a blank slate
#the maxUID parameter instructs the display to keep all text with a UID below what is specified.
def clear_display(maxUID = 999):
    pass

#refreshes the display
#if the terminal window is resized, this updates all positions with percentage values
#unconditionally removes all objects that are entirely off-screen.
def refresh_display():
    #first updates text whose position is NOT relative, and then text whose position is relative.
    pass

#Adds a string to the display.
#If the position is left as default, it treats it like a print command and scrolls the rest of the text up a line
def add_string(text, uid, pos = "0x0x0"):
    pass

#Removes a string from the display.
def remove_string(uid):
    pass

#Changes a string's position in the display
def change_string_position(uid):
    pass

#Changes a string's text in the display
def change_string_text(uid):
    pass

#Gets all the UIDs of the string objects. Used for functions in the same vein as clear_display(maxUID)
def get_all_uids():
    pass

#Get user input for commands, etc.
def user_input():
    pass
