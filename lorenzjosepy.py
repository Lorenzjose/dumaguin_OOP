from tkinter import *
import sqlite3

# Create the main application window
root = Tk()
root.title("My CRUD Project")
root.geometry("500x500")

# Database setup
conn = sqlite3.connect('loren.sqbpro')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS myinformation (
                firstname TEXT,
                lastname TEXT,
                middlename TEXT,
                address TEXT)''')

# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

m_name = Entry(root, width=30)
m_name.grid(row=2, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=3, column=1, padx=20)

# Create submit function for database
def submit():
    # Insert into table
    c.execute("INSERT INTO myinformation (firstname, lastname, middlename, address) VALUES (?, ?, ?, ?)",
              (f_name.get(), l_name.get(), m_name.get(), address.get()))
    conn.commit()
    
    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    m_name.delete(0, END)
    address.delete(0, END)

# Create submit button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=4, column=1, pady=10)

# Create query function to show records
def query():
    c.execute("SELECT * FROM myinformation")
    records = c.fetchall()
    
    # Clear the previous records displayed (if any)
    for widget in display_frame.winfo_children():
        widget.destroy()
    
    # Display records
    for index, record in enumerate(records):
        Label(display_frame, text=f"{record}").grid(row=index, column=0)

# Create a frame to display records
display_frame = Frame(root)
display_frame.grid(row=6, column=1)

# Create query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=5, column=1, pady=10)

#Create delete button
query_btn=Button(root,text="Delete Record",command=delete)
query_btn.grid(row=12,column=0,columnspan=2,pady=30)
query_btn=Button(root,text="enter id number",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)
#Create function to delete
def delete():
#database
    conn=sqlite3.connect()

# Run the application
root.mainloop()

# Close the connection when the application exits
conn.close()
