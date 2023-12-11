import tkinter as tk

class Node:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.next = None

    def __str__(self):
        return f"Patient: {self.name} Priority: {self.priority}"

class PriorityQueue:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def push(self, item, priority):
        newNode = Node(item, priority)
        if self.isEmpty():
            self.head = newNode
        else:
            if newNode.priority > self.head.priority:
                newNode.next = self.head
                self.head = newNode
            else:
                previous = None
                current = self.head
                while ((current is not None) and newNode.priority <= current.priority):
                    previous = current
                    current = current.next

                if current is not None:
                    previous.next = newNode
                    newNode.next = current
                else:
                    previous.next = newNode

    def pop(self):
        if self.isEmpty():
            return 'Queue is empty'
        else:
            result = f"Processing: {self.head}"
            self.head = self.head.next
            return result

    def peek(self):
        return f"Next patient: {self.head.name}" if self.head else "Queue is empty"
    
    def update(self, item, priority):
        if self.isEmpty():
            return 'Queue is empty'
        else:
            current = self.head
            while current is not None:
                if current.name == item:
                    current.priority = priority
                    return f"Patient {item} priority updated to {priority}"
                current = current.next
            return f"Patient {item} not found"
    
    
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return f"Number of patients is {count}"

    def printQueue(self):
        current = self.head
        result = "=================================\n\n"
        result += str(current) + "\n"
        while current.next is not None:
            current = current.next
            result += str(current) + "\n"
        result += "\n================================="
        return result

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("ER Check-In System")

        self.patientQueue = PriorityQueue()

        self.output_text = tk.Text(master, height=20, width=100)
        self.output_text.pack(pady=10)

        self.name_entry = tk.Entry(master, width=20)
        self.name_entry.pack(pady=5)


        self.priority_entry = tk.Entry(master, width=20)
        self.priority_entry.pack(pady=5)

        self.add_button = tk.Button(master, text="Add Patient", command=self.add_patient)
        self.add_button.pack(pady=5)

        self.process_button = tk.Button(master, text="Process Patient", command=self.process_patient)
        self.process_button.pack(pady=5)

        self.peek_button = tk.Button(master, text="Peek at Next Patient", command=self.peek_patient)
        self.peek_button.pack(pady=5)

        self.length_button = tk.Button(master, text="Number of Patients", command=self.length_patient)
        self.length_button.pack(pady=5)


        self.update_button = tk.Button(master, text="Update Priority", command=self.update_patient)
        self.update_button.pack(pady=5)

        self.close_button = tk.Button(master, text="Close", command=master.quit)

    def add_patient(self):
        name = self.name_entry.get()
        priority = int(self.priority_entry.get())
        self.patientQueue.push(name, priority)
        self.update_display()
        

    def process_patient(self):
        result = self.patientQueue.pop()
        self.update_display(result)

    def peek_patient(self):
        result = self.patientQueue.peek()
        self.update_display(result)

    def length_patient(self):
        result = f"Number of patients: {self.patientQueue.size()}"
        self.update_display(result)

    def update_patient(self):
        name = self.name_entry.get()
        priority = int(self.priority_entry.get())
        result = self.patientQueue.update(name, priority)
        self.update_display(result)


    def update_display(self, result=""):
        result += "\n" + self.patientQueue.printQueue()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)


if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
