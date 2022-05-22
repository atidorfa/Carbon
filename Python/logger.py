# noinspection PyUnresolvedReferences
import unreal
import os

print('getcwd:      ' + os.getcwd())
print('__file__:    ' + __file__)
unreal.log("hello world!")
unreal.log_warning("this is a warning!")
unreal.log_error("this is an error!!!")
