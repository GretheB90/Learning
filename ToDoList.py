import os

def to_do_list(): #We’re opening the box and running all the code inside
    filename = "tasks.txt"
    tasks = [] #Start with an empty list
    
    #Load tasks from file at start
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    # Format: done|task_text
                    done, text = line.split("|", 1)
                    tasks.append({"text": text, "done": done == "1"})

    #Save tasks to file
    def save_tasks():
        with open(filename, "w") as file:
            for task in tasks:
                done = "1" if task["done"] else "0"
                file.write(f"{done}|{task['text']}\n")

    while True: #Shows us the options we can choose between. keep going forever.
        print("\nWhat would you like to do?") #The \n just makes a blank line for spacing
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Quit")
        print("5. Clear all tasks")
        print("6. Mark task as done/undone")
        choice = input("Enter your choice: ").strip() #.strip() removes spaces, tabs (\t), and newlines (\n) from both ends of the string.
        #If you only want to remove spaces from one side:
        #.lstrip() → removes from left
        #.rstrip() → removes from right

        #Add a task:
        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                tasks.append({"text": task, "done": False})  #Store as dictionary
                save_tasks()
                print(f"Task '{task}' added.")
            else:
                print("You didn't type anything!")
                
        #Remove a task:
        elif choice == "2":
            if not tasks:
                print("No tasks to remove.") #If your list is empty, it says so and goes back to the menu.
                continue
            for i, task in enumerate(tasks, 1):
                status = "✓" if task["done"] else "✗"
                print(f"{i}. [{status}] {task['text']}")
            try:
                task_num = int(input("Enter number: ").strip()) #It shows you your list with numbers, so you can pick a task to remove.
                if 1 <= task_num <= len(tasks): #You type the number next to the task you want to delete.
                    removed = tasks.pop(task_num - 1) #It removes it from the list — using .pop().
                    save_tasks()
                    print(f"Task '{removed['text']}' removed.")
                else:
                    print("That's not a valid number.") #If you type in a word (like “cat” instead of a number), it says “That’s not a valid number.”
            except ValueError:
                print("Please enter a valid number.")
        
        #Show all tasks:
        elif choice == "3":
            if tasks:
                print("Here are your tasks:") #If there are tasks, it shows them.
                for i, task in enumerate(tasks, 1):
                    status = "✓" if task["done"] else "✗"
                    print(f"{i}. [{status}] {task['text']}")
            else:
                print("Your to-do list is empty.") #If there’s nothing to do, it tells you the list is empty.
        
        #Quit the program:
        elif choice == "4":
            print("Goodbye!")
            break #If you pick 4, it says “Goodbye!” and break tells it to stop the loop and end the app.
        
        #Clear all tasks:
        elif choice == "5":
            if not tasks:
                print("Your list is already empty.") #If the list is already empty, it says so.
            else:
                confirm = input("Are you sure you want to delete all tasks? (yes/no): ").strip().lower() #If there are tasks, it asks you: “Are you really sure?”
                if confirm == "yes":
                    tasks.clear() #If you type yes, it deletes everything using .clear().
                    save_tasks()
                    print("All tasks have been cleared.")
                else:
                    print("Clear canceled.") #If you type anything else, it says “Okay, I didn’t delete anything.”
        
        #Mark a task as done/undone:
        elif choice == "6":
            if not tasks:
                print("No tasks to mark.")
                continue
            print("Which task do you want to mark as done or undone?")
            for i, task in enumerate(tasks, 1): #Enumerate = It adds numbers to the items in your list automatically, so you don't have to count them yourself.
                status = "✓" if task["done"] else "X"
                print(f"{i}. [{status}] {task['text']}")
            try:
                task_num = int(input("Enter number: ").strip())
                if 1 <= task_num <= len(tasks):
                    task = tasks[task_num - 1]
                    task["done"] = not task["done"]  #Toggle done/undone
                    save_tasks()
                    print(f"Task '{task['text']}' is now marked as {'done' if task['done'] else 'not done'}.")
                else:
                    print("That's not a valid number.")
            except ValueError:
                print("Please enter a valid number.")

        else:
            print("Please choose a valid option (1–6).")

#Run the to-do list program
to_do_list()

#Enumerate:
#The index (position in the list)
#The item (like a task or item)
#It loops through a list and gives you the item’s number at the same time.

#.append() adds something to the end of a list.
#Adding a new task to your tasks list
#That task is stored as a dictionary (with text and done status)
#Adds the item without replacing

#Difference between .append(), .insert() and .extend():
#.append(item) adds 1 item to the end of your list.     -my_list.append("cherry")
#.insert(index, item) adds 1 item to a specific spot.   -my_list.insert(1, "orange")
#.extend(list_of_items) adds multiple items at the end. -my_list.extend(["grape", "kiwi"])
