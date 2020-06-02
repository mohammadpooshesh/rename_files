import os
import argparse 
from os import listdir
from os.path import isfile, join

#function for get arguments path and word
def get_arguments():

    # Initialize parser 
    parser = argparse.ArgumentParser() 
  
    # Adding folder path argument 
    parser.add_argument("-p", "--path", help = "base folder path") 

    # Adding word argument 
    parser.add_argument("-w", "--word", help = "word that you want delete from file name") 
    
    # Read arguments from command line 
    args = parser.parse_args() 
    
    #check enter folder path argument
    if not args.path: 

        print("enter path !!!")
    
    #check enter word argument
    if not args.word: 

        print("enter word !!!")
    
    return args

#function for change names of files in  forders
def change_files_name(args):

    #variable for check rename all files without asking
    allow_all = False

    #variable for check file is found with this word or not
    find_file = False

    #loop for walk in path and get sub dirs path
    for root, dirs, files in os.walk(args.path, topdown=False):

        #loop for walk in dirs
        for dir_name in dirs:
            
            #loop for walk in a dir and get list of files (inside dir)
            for file in os.listdir(join(root, dir_name)):
               
                #check file name is contain word 
                if args.word in file:

                    find_file = True
                    
                    #check rename all files without asking 
                    if allow_all:

                        #rename file command
                        os.rename(join(root, dir_name,file), join(root, dir_name,file).replace(args.word, ''))

                    else:

                        #ask for rename the file
                        allow_one_file = input("are you sure for rename " + str(file) + "(y/n)")

                        if allow_one_file in ["y","Y"]:
                            
                            #check for rename all files
                            allow_all_file = input("Do you want to rename all the files without asking you?(y/n)")

                            if allow_all_file in ["y","Y"]:

                                allow_all = True

                            #rename file command
                            os.rename(join(root, dir_name,file), join(root, dir_name,file).replace(args.word, ''))

    if not find_file : 
        print("file with this word not found")
    else:
        print("rename files successful :)")

try:
    args = get_arguments()
    change_files_name(args)
except:
    print("Error performing operations !!!")