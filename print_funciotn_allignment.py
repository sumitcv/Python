"""
Discription: 
This code is used to print string value to the right side left sice and center.
Allignment can be change of print message. 

os.get_termianl_size()  function is gives the terminal size according to the system terminal. 
in windows we have command : "mode"
in  linux we have command : 
"""
import os
t_w = os.get_terminal_size().columns
str_name = "Python learning"
print(str_name.center(t_w))
print(str_name.rjust(t_w))
print(str_name.ljust(t_w))
