import tkinter as tk
import sqlite3

# Function to submit a new record to the database
def submit():
    conn = sqlite3.connect("lorenz.sqlite3")
    c = conn.cursor()

    # Insert data into the database
    c.execute("INSERT INTO STUDENT_INFORMATION (Name, Address, Date_of_Birth, Email) VALUES (:Name, :Address, :Date_of_Birth, :Email)",
              {
                  'Name': Name.get(),
                  'Address': Address.get(),
                  'Date_of_Birth': Date_of_Birth.get(),
                  'Email': Email.get()
              })
    conn.commit()
    conn.close()

    # Clear the input fields
    Name.delete(0, tk.END)
    Address.delete(0, tk.END)
    Date_of_Birth.delete(0, tk.END)
    Email.delete(0, tk.END)

# Function to query all records from the database
def query():
    conn = sqlite3.connect("lorenz.sqlite3")
    c = conn.cursor()

    # Retrieve all records
    c.execute("SELECT * FROM STUDENT_INFORMATION")
    records = c.fetchall()

    # Format records for display
    print_records = ''
    for record in records:
        print_records += f"{record[0]} {record[1]} {record[2]} {record[3]} {record[4]}\n"

    query_label = tk.Label(root, text=print_records)
    query_label.grid(row=20, column=0, columnspan=2)

    conn.close()

# Function to delete a record by ID
def delete():
    conn = sqlite3.connect("lorenz.sqlite3")
    c = conn.cursor()

    # Delete a record based on the ID
    c.execute("DELETE FROM STUDENT_INFORMATION WHERE oid = ?", (delete_box.get(),))

    conn.commit()
    conn.close()

    # Clear the delete box
    delete_box.delete(0, tk.END)

# Function to query a record by its ID
def query_jr():
    conn = sqlite3.connect("lorenz.sqlite3")
    c = conn.cursor()

    # Retrieve a record based on the provided ID
    c.execute("SELECT * FROM STUDENT_INFORMATION WHERE oid = ?", (delete_box.get(),))
    records = c.fetchall()

    # Format records for display
    print_records = ''
    for record in records:
        print_records += f"{record[0]} {record[1]} {record[2]} {record[3]} {record[4]}\n"

    query_label = tk.Label(root, text=print_records)
    query_label.grid(row=25, column=0, columnspan=2)

    conn.commit()
    conn.close()

# Create the main window
root = tk.Tk()
root.title("STUDENT INFORMATION")
root.geometry("500x500")

# Create a database connection and cursor
conn = sqlite3.connect("lorenz.sqlite3")
c = conn.cursor()

# Create the database table if it doesn't exist
c.execute("""
CREATE TABLE IF NOT EXISTS STUDENT_INFORMATION (
    Name TEXT,
    Address TEXT,
    Date_of_Birth TEXT,
    Email TEXT
)
""")

conn.commit()
conn.close()

# Create the input fields for Name, Address, Date of Birth, and Email
Name = tk.Entry(root, width=30)
Name.grid(row=0, column=1, padx=20)

Address = tk.Entry(root, width=30)
Address.grid(row=1, column=1, padx=20)

Date_of_Birth = tk.Entry(root, width=30)
Date_of_Birth.grid(row=2, column=1, padx=20)

Email = tk.Entry(root, width=30)
Email.grid(row=3, column=1, padx=20)

# Create labels for the input fields
Name_label = tk.Label(root, text="Name")
Name_label.grid(row=0, column=0)

Address_label = tk.Label(root, text="Address")
Address_label.grid(row=1, column=0)

Date_of_Birth_label = tk.Label(root, text="Date of Birth")
Date_of_Birth_label.grid(row=2, column=0)

Email_label = tk.Label(root, text="Email")
Email_label.grid(row=3, column=0)

# Create buttons for submitting, querying, and deleting records
submit_btn = tk.Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = tk.Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

delete_box = tk.Entry(root, width=30)
delete_box.grid(row=10, column=1, padx=30)

delete_btn = tk.Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

query_jr_btn = tk.Button(root, text="Query Record by ID", command=query_jr)
query_jr_btn.grid(row=15, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Run the main loop
root.mainloop()
