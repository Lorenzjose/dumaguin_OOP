import tkinter as tk

# Function to add an item to the listbox
def add_item():
    item = entry.get()
    if item:  # Only add the item if it's not empty
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)  # Clear the entry field after adding the item

# Function to remove the selected item from the listbox
def remove_item():
    selected_index = listbox.curselection()  # Get selected item index
    if selected_index:  # Only delete if an item is selected
        listbox.delete(selected_index[0])

# Function to clear all items in the listbox
def clear_list():
    listbox.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Listbox Example")

# Create the entry field where the user types input
entry = tk.Entry(root)
entry.pack()

# Create the "Add" button and bind it to the add_item function
add_button = tk.Button(root, text="Add", command=add_item)
add_button.pack()

# Create the "Remove" button and bind it to the remove_item function
remove_button = tk.Button(root, text="Remove", command=remove_item)
remove_button.pack()

# Create the "Clear" button and bind it to the clear_list function
clear_button = tk.Button(root, text="Clear", command=clear_list)
clear_button.pack()

# Create the listbox to display the items
listbox = tk.Listbox(root)
listbox.pack()

# Run the main loop to keep the application open
root.mainloop()
