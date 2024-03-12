import tkinter as tk
from tkinter import messagebox

def vote(option):
    print("Voted for option:", option)

def main():
    root = tk.Tk()
    root.title("Voting System")
    
    # Set background color
    root.configure(bg="#f0f0f0")  # Light gray background color
    
def main():
    root = tk.Tk()
    icon_path = "/home/levi/Downloads/voting-box.ico"
    root.iconbitmap(icon_path)
    root.mainloop()

class VotingSystem:
    def __init__(self):
        self.candidates = {
            "Ashik": 0,
            "Farhan": 0,
            "Hufais": 0,
            "Salvio": 0
        }
        self.log = []
    
    def add_candidate(self, name):
        pass

    def vote(self, name):
        if name in self.candidates:
            self.candidates[name] += 1
            self.log.append(f"{name} received a vote.")
            messagebox.showinfo("Vote Registered", f"Vote for {name} registered successfully.")
        else:
            messagebox.showerror("Invalid Candidate", f"Candidate {name} does not exist.")

    def display_results(self):
        messagebox.showinfo("Vote Counts", "\nCurrent Vote Counts:\n")
        for candidate, votes in self.candidates.items():
            messagebox.showinfo("Vote Counts", f"{candidate}: {votes}\n")
        messagebox.showinfo("Election Log", "\nElection Log:\n" + "\n".join(self.log))


def main():
    voting_system = VotingSystem()

    window = tk.Tk()
    window.title("Voting System")
    window.geometry("400x300")

    def add_candidate():
        pass

    def vote():
        name = entry_vote.get()
        voting_system.vote(name)
        entry_vote.delete(0, tk.END)

    def display_results():
        voting_system.display_results()

    label_vote = tk.Label(window, text="Vote for Candidate:")
    label_vote.pack()
    entry_vote = tk.Entry(window)
    entry_vote.pack()
    button_vote = tk.Button(window, text="Vote", command=vote)
    button_vote.pack()

    button_results = tk.Button(window, text="Display Results", command=display_results)
    button_results.pack()

    window.mainloop()


if __name__ == "__main__":
    main()