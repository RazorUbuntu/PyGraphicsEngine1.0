# INFO: Error Handling for self defined functions and classes

from sys import exit

ERROR_DICT = {
    # ERROR: blah {} blah {} , number of arguments
    
    # Error group 101: refers to type error or class error
    101_01: ("Error: 101.01:", ", type must be ", 2),
    101_02: ("Error: 101.02:", ", class must be ", 2),
    
    # Error group 110: refers to errors in number of Arguments allowed
    110_01: ("Error: 101.03: Unmatched arguments:", 1)

    
}


class ErrorHandling3D:
    def __init__(self, error_code: int):
        self.ErrorCode = error_code
        self.arg_num = ERROR_DICT[error_code][-1]

    def error(self, *args):
        return ''.join([item + f' {args[idx]} ' for idx, item in enumerate(ERROR_DICT[self.ErrorCode][:-1])])


###############################
#       ERROR Functions       #
###############################

def show_error_n_exit(error):
    print(error)
    exit()


###############################
#      ERROR Declaration      #
###############################

UnmatchedArgs = ErrorHandling3D(11001)
TypeOfError = ErrorHandling3D(10101)
         