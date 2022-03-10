from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import backendSQL as sqlFuncs

window = Tk()
### Naviagtion Functions #####################################################################################################################################################################################################################################
# Navigation in Membership Menu
def destroyMemMenu(): # Ensure Membership Window is destroyed
    memMenu.destroy();
def navFromMemToCreateMem(): # Go to CreateMem
    memberCreation();
    destroyMemMenu();
    createMemMenu.lift()
def navFromMemToDelMem(): # Go to deleteMem
    memberDeletion()
    destroyMemMenu();
    deleteMemMenu.lift()
def navFromMemToUpdateMem(): # Go to updateMem
    memberUpdateLandingMenu();
    destroyMemMenu();
    updateInputId.lift()
def navReturnToMain(): # Return to Main Menu
    window.destroy()
    import landingPage

# Navigation in Delete Menus
def destroyDeleteMenu():
    deleteMemMenu.destroy();
def navFromDeleteToMemMenu(): # Return to Membership Menu
    membershipMenu();
    destroyDeleteMenu();
    memMenu.lift()
    
###################################################################################################################
### EDIT YOUR FUNCTIONS BELOW HERE ONWARDS




memberDeletion();
