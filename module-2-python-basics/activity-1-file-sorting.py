"""
Module 2 — Activity: File Sorting with os and shutil
Student: Mancion, John David Q.
Date: Sept 27, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]
first it gets the file directory then prints the paht of the list after that
it ask for the file text file to be sorted then that file will be according to what it ends with


============================================
KEY VOCABULARY
============================================
- os module: it lets us interact with the OS
- shutil module: used when dealing with high level file operating where we need to copy and etc.
- file path: a string of text where we can find the location of the file
- directory: technical term for calling a folder on a computer
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

# --- paste your existing code here ---
list_of_files = os.listdir()
print(list_of_files)


filename = input("enter file: ")
if os.path.exists(filename):
    print("it exists")

else:
    print("it does not exist")


#counter
img = 0
doc = 0
vid = 0
other = 0

for filename in os.listdir("."):
    if filename.endswith(".txt"):
        os.rename(filename, os.path.join("doc", filename))
        print(f"Moved: {filename} -> doc/")
        doc +=1
    elif filename.endswith(".pptx"):
        os.rename(filename, os.path.join("doc", filename))
        print(f"Moved: {filename} -> doc/")
        doc +=1
    elif filename.endswith(".png"):
        os.rename(filename, os.path.join("img", filename))
        print(f"Moved: {filename} -> img/")
        img += 1
    elif filename.endswith(".jpeg"):
        os.rename(filename, os.path.join("img", filename))
        print(f"Moved: {filename} -> img/")
        img += 1
    elif filename.endswith(".mp4"):
        os.rename(filename, os.path.join("vid", filename))
        print(f"Moved: {filename} -> vid/")
        vid +=1
    elif filename.endswith(".mov"):
        os.rename(filename, os.path.join("vid", filename))
        print(f"Moved: {filename} -> vid/")
        vid +=1

print(f"="*30)
print("Folder Summary")
print(f"Images moved: {img}")
print(f"Documents moved: {doc}")
print(f"Videos moved: {vid}")
print(f"Others moved: {other}")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]
what tripped me up probably when i dont know how to use the module but there is an documentation above the 
instructions

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
