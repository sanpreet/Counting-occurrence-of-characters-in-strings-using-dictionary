# ******************Count the occurence of characters in the strings using the concept of dictionary
# **************************************************************************************************************
def character_count(string): #this is the function used for performing the counting operation
    string=string.lower().strip(":")     #converting the string into lower case
    #if there is any : or, in the string, these statements will remove it. If not it will go to finally statement
    try:
        string= string.split(",")
        string = "".join(string)
    finally:
        #converting the string into list
        string=list(string)
        #at the initial stage the dictionary is empty
        dictionary ={}
        for i in string:
            #it checks whether the passed character is alphabet or not
            if i.isalpha():
                if i in dictionary:
                    dictionary[i] +=1;
                else:
                    #IF not repeated it is counted only once
                    dictionary[i]=1;
         #loop will return to the caaling function
        return dictionary
# Input the value:
string=input("Enter the string, you may use : and , also: Please see try and finally statement:")
output = character_count(string)
#output will come in the form of counting each character in the string or occurence of each character:
print("Count of every letter in string {} = ".format(string),output)


