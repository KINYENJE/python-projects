import tkinter as tk
from tkinter import messagebox

class CandyStack:
    def __init__(self, root):
        self.root = root
        self.root.title("Candy Stack")
        self.root.geometry("300x400") # width x height

        self.candy_frame = tk.Frame(self.root) # Frame to hold the candy stack label
        self.candy_frame.pack(pady=20) # pady is padding in y direction

        self.candy_label = tk.Label(self.candy_frame, text="Candy Stack") # Label to display the candy stack
        self.candy_label.pack()

        self.stack_canvas = tk.Canvas(self.root, width=150, height=200, bg="white")
        self.stack_canvas.pack()

        self.candies = []  # List to store candy items (represented as ovals)

        self.pop_button = tk.Button(self.root, text="Pop Candy", command=self.pop_candy) # command is the function to call when the button is clicked
        self.pop_button.pack(pady=10) # pady is padding in y direction

        self.push_button = tk.Button(self.root, text="Push Candy", command=self.push_candy) # command is the function to call when the button is clicked
        self.push_button.pack(pady=10) # pady is padding in y direction

    def push_candy(self):
        x = 75
        y = 40
        radius = 10
        candy = self.stack_canvas.create_oval(
            x - radius, y - radius,
            x + radius, y + radius,
            fill="blue"
        )
        self.candies.append(candy) # Add the candy to the list of candies

    def pop_candy(self):
        if self.candies:
            candy_to_pop = self.candies.pop()
            self.stack_canvas.delete(candy_to_pop)
        else:
            messagebox.showinfo("Candy Stack", "No more candies in the stack!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CandyStack(root)
    root.mainloop()

