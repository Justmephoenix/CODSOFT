class TodoList:
    def __init__(self):
        self.tasks = []
        
    def addTask(self,task):
        self.tasks.append(task)
        print(f"{task} added successfully.")
        
    def updateTask(self,old_task,new_task):
        if old_task in self.tasks:
            i=self.tasks.index(old_task)
            self.tasks[i]=new_task
            print(f"Succesfully changes old task : {old_task} to new rask : {new_task}")
        else:
            print(f"{old_task} task not found !!! please enter a valid task .")
            
    def deleteTask(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"{task} delete Successfully.")
        else:
            print(f"{task} task not found !!! please enter a valid task .")
        
    def viewTask(self):
        if self.tasks:
            print("Tasks are :")
            print()
            for i,task in enumerate(self.tasks,start=1):
                print(f"{i}. {task}")
        else:
            print("No Tasks to display ")
        
        
        
def myApp():
    task=TodoList()
    
    while True:
        print('\n Menu :')
        print("1- Enter The New Task")
        print("2- Update/Edit the Existing Task")
        print("3- Delete The Task")
        print("4- View The Tasks") 
        print("5- Exit")
        print()
        choice=input("Enter Your Choice:  ")
        print()
        if choice=="1":
            t=input("\n Enter Your Task: ")
            task.addTask(t)
        elif choice=="2":
            old_task=input("\n Enter The Task for Update/Edit ")
            new_task=input("\n Enter The New Task")
            task.updateTask(old_task,new_task)
            
        elif choice=="3":
            del_task=input("\n Enter The task for deletion  ")
            task.deleteTask(del_task)
            
        elif choice=="4":
            task.viewTask()
            
        elif choice=="5":
            print("Thanks For Using us ")
            print("Exiting from App !!!! ")
            break
        else:
            print("Pleae !!! Enter a valid choice from above option ")
            
            
            
             
        
        
if __name__=='__main__':
    myApp()