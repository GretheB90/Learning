import csv      #Helps read CSV files (which are like spreadsheets)
import os       #Helps your program talk to your computer, like asking "Where am I?" or "What files are here?"

print("Current working directory:", os.getcwd())    #"Hey computer, where are we?" → it prints the current folder.
print("Files in current directory:", os.listdir())  #"What's in this folder?" → it lists the files (like dogs.csv if it exists).


#Define a class to represent each dog:
class Dog:
    def __init__(self, name, age, playtime_hours):
        self.name = name
        self.age = age
        self.playtime_hours = playtime_hours
    
    def __str__(self): #the __str__ Part just tells how to print it nicely. Like: Max (Age: 3, Playtime: 2.5 hrs/day)
        return f"{self.name} (Age: {self.age}, Playtime: {self.playtime_hours} hrs/day)"
    
#function to load dogs from a csv file:
def load_dogs_from_csv(filename):   #This code starts a function called load_dogs_from_csv.
    dogs = []                       #Takes the name of a file and creates an empty list called dogs, ready to fill it with dog info from that file!
    with open(filename, mode='r') as file:  #Opens a file like dogs.csv.
        reader = csv.DictReader(file)       #Reads each row.
        for row in reader:
            name = row['name']
            age = int(row['age'])
            playtime_hours = float(row['playtime_hours'])
            dogs.append(Dog(name, age, playtime_hours)) #It creates a Dog for each line!
    return dogs     #It puts all the dogs into a list (like a group or collection), and returns it.


#Load the dogs:
dogs = load_dogs_from_csv('dogs.csv')   #This calls the function, giving it the file 'dogs.csv'.

#Print all the dogs:
print("All Dogs:\n")
for dog in dogs:
    print(dog)  #Then, it prints every dog nicely using the __str__ we made earlier.
    
#Filter dogs that play more than 2 hours:
active_dogs = [dog for dog in dogs if dog.playtime_hours > 2]   #“Give me only the dogs that play more than 2 hours a day!”

print("\n Dogs that play more than 2 hours a day\n")
for dog in active_dogs:
    print(dog)
    
#Calculates average age and playtime:
total_age = sum(dog.age for dog in dogs)                    #All the dog ages (like 3 + 5 + 2 = 10)
total_playtime = sum(dog.playtime_hours for dog in dogs)    #All the playtimes (like 2.5 + 1.0 + 3.0 = 6.5)

average_age = total_age / len(dogs)                         #Then we divide by how many dogs to get the average:
average_playtime = total_playtime / len(dogs)

print("\n Averages:")
print(f"Average Age: {average_age:.2f} years")                  #The :.2f part means: only show 2 digits after the decimal, like 2.67.
print(f"Average playtime: {average_playtime:2f} hours a day")   #It prints the average age and playtime.
