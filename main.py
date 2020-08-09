#import the regex module
import re
import time
#Prompt for user input to open the file
src = input("Enter the filename:")
#open the file
with open("Data/" + src + ".txt", "r") as f:
    song = f.read()
#Split the text into blocks
parts = re.split("\n\n", song)
#Remove unnecessary characters
for i in range(len(parts)):
  parts[i] = re.sub("\|", "", parts[i])
  parts[i] = re.sub("LH:|RH:", "", parts[i])
  parts[i] = re.split("\n", parts[i])

#A dictionary of notes from 2nd to 6th octave
Notes = {
  "1": {
    "c": 33,
    "C": 35,
    "d": 37,
    "D": 39,
    "e": 41,
    "f": 44,
    "F": 46,
    "g": 49,
    "G": 52,
    "a": 55,
    "A": 58,
    "b": 62,
  },
  "2": {
    "c": 65,
    "C": 69,
    "d": 73,
    "D": 78,
    "e": 82,
    "f": 87,
    "F": 93,
    "g": 98,
    "G": 104,
    "a": 110,
    "A": 117,
    "b": 124,
  },
  "3": {
    "c": 131,
    "C": 139,
    "d": 147,
    "D": 156,
    "e": 167,
    "f": 175,
    "F": 185,
    "g": 196,
    "G": 208,
    "a": 220,
    "A": 233,
    "b": 247,
  },
  "4": {
    "c": 262,
    "C": 277,
    "d": 294,
    "D": 311,
    "e": 330,
    "f": 350,
    "F": 370,
    "g": 392,
    "G": 415,
    "a": 440,
    "A": 466,
    "b": 493,
  },
  "5": {
    "c": 523,
    "C": 554,
    "d": 587,
    "D": 622,
    "e": 659,
    "f": 699,
    "F": 740,
    "g": 784,
    "G": 830,
    "a": 880,
    "A": 932,
    "b": 988,
  },
  "6": {
    "c": 1047,
    "C": 1109,
    "d": 1175,
    "D": 1245,
    "e": 1319,
    "f": 1397,
    "F": 1480,
    "g": 1568,
    "G": 1661,
    "a": 1760,
    "A": 1865,
    "b": 1976,
  },
  "7": {
    "c": 2093,
    "C": 2218,
    "d": 2349,
    "D": 2489,
    "e": 2637,
    "f": 2794,
    "F": 2960,
    "g": 3136,
    "G": 3323,
    "a": 3520,
    "A": 3729,
    "b": 3951,
  }
}

#Coolstuff
def coolstuff(string):
  string = re.split(" ", string)
  print("\n")
  for word in string:
    print(word + "...")
    time.sleep(0.5)
  print("\n")
#coolstuff("This text is here just to make the program look cooler")
#Parsing the text
music=[]
for part in parts:
  firsttime = True
  for line in part:
    octave = line[0]
    line = re.sub("\d", "", line)
    i = parts.index(part) * len(line)
    for ch in line:
      #firsttime is used to create the list on first iteration
      if firsttime:
        if ch == "-":
          music.append(0)
        else:
          music.append(Notes[octave][ch])
      else:
        #priority is given to the higher octaves
        if ch == "-":
          i+=1         
          continue
        elif music[i] == 0:
          #print(ch)
          music[i] = Notes[octave][ch]  
        i+=1
    #Demo
    #print(line)
    #print(music[parts.index(part) * len(line):i+len(line)])
    firsttime = False
#Adding the 0 note at the end
music.append(-1)
if(len(music)>400):
  print("The array is too long")
#Printing the result
print("Parsing complete: \n")
time.sleep(1)
print("-----" * 18)
print(music)
print("-----" * 18)
print("Length of the list is {} elements".format(len(music)))



