# let's import tkinter module to create GUTs
import tkinter as tk
#lets use dir() (dir=directory)function to see whats inside the  tkinter module
# print(dir(tkinter))_____________________for check only

# lets create an empty GUT / root gui
# use Tk so we get basic gui and store it in root named variable
root = tk.Tk()
#lets define functions
def add():
    print('Adding task to the list')
    #lets get the text inside the entry widget
    data=entry.get()
    #lets check first if data is empty or not
    if data:
        #if data is not empty then shift that data into listbox
        #arguments: indext no.(0..>first element)
        # task_list.insert(0,data)
        task_list.insert(tk.END,data)
        
        
        #lets clean the entry wedget
        entry.delete(0,tk.END)
        
def delete():
    print('delete the task')    
    
    #lets delete the active element
    task_list.delete(tk.ACTIVE)




#lets define is size
#lrts define the width and height of gi function
root.geometry('400x400')

root.resizable(width=False, height=False)
# if we use false them so it will not get resizeble

#lets change the title
root.title('grecy To Do List')

#lets add entry widget/ component
entry = tk.Entry(root)
#we pack it and give specings
entry.pack(padx=30,pady=10, fill='x')
# let's add a button ...> add task
#in command we ony put the function name
add_button = tk.Button(root, text='Add task', width=20,command=add)
add_button.pack()

#lets add the task list
task_list = tk.Listbox(root)
task_list.pack(fill='x', padx=20, pady=10)
# lets add one more button ...>delete task
delete_button=tk.Button(root, text='Delete task',width=20,command=delete)
delete_button.pack()


#lets call the main root function
# mainloop disply the continuous gui 
# it listens for any events on gui

root.mainloop()

