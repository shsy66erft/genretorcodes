import ctypes

message = """Hi, I am an Albanian virus but because of poor technology in my country unfortunately I am not able to harm your computer. 
Please be so kind to delete one of your important files yourself and then forward me to other users.
Many thanks for your cooperation!
Best regards,
Albanian Virus"""

ctypes.windll.user32.MessageBoxW(0, message, "Virus Alert!", 0x40 | 0x1)
