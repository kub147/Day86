import tkinter as tk
from tkinter import simpledialog
import time
import random

SENTENCES = {
    "English": [
        "The quick brown fox jumps over the lazy dog. This is a common pangram. It contains every letter of the English alphabet.",
        "Python is a versatile programming language. It is widely used in data science, automation, and web development.",
        "Typing fast requires practice and patience. The more you practice, the better you become. Accuracy is just as important as speed.",
        "Artificial Intelligence is transforming the world. Many industries rely on AI for automation and decision-making.",
        "A journey of a thousand miles begins with a single step. Every great achievement starts with a small effort."
    ],
    "Polski": [
        "Szybki brązowy lis przeskakuje nad leniwym psem. To popularne zdanie zawiera wszystkie litery polskiego alfabetu.",
        "Python to wszechstronny język programowania. Jest szeroko stosowany w nauce danych, automatyzacji i tworzeniu stron internetowych.",
        "Szybkie pisanie wymaga praktyki i cierpliwości. Im więcej ćwiczysz, tym lepszy się stajesz. Dokładność jest równie ważna jak szybkość.",
        "Sztuczna inteligencja zmienia świat. Wiele branż polega na AI w zakresie automatyzacji i podejmowania decyzji.",
        "Podróż tysiąca mil zaczyna się od pierwszego kroku. Każde wielkie osiągnięcie zaczyna się od małego wysiłku."
    ]
}

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x450")

        self.language = self.choose_language()
        self.start_time = None
        self.sentence = random.choice(SENTENCES[self.language])

        # Title
        self.label_title = tk.Label(root, text="Typing Speed Test" if self.language == "English" else "Test Szybkości Pisania", font=("Arial", 18, "bold"))
        self.label_title.pack(pady=10)

        # Display Sentence
        self.label_sentence = tk.Label(root, text=self.sentence, font=("Arial", 14), wraplength=650, justify="center")
        self.label_sentence.pack(pady=10)

        # Progress Label
        self.progress_label = tk.Label(root, text="Progress: 0%" if self.language == "English" else "Postęp: 0%", font=("Arial", 12))
        self.progress_label.pack()

        # Text Entry
        self.text_entry = tk.Text(root, font=("Arial", 14), height=5, width=70)
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<KeyPress>", self.start_timer)
        self.text_entry.bind("<KeyRelease>", self.update_speed)

        # Result Label
        self.result_label = tk.Label(root, text="WPM: 0 | Accuracy: 0%" if self.language == "English" else "Słowa/min: 0 | Dokładność: 0%", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

        # Restart Button
        self.restart_button = tk.Button(root, text="Restart" if self.language == "English" else "Restartuj", font=("Arial", 12), command=self.restart_test)
        self.restart_button.pack(pady=10)

    def choose_language(self):
        """Asks the user to select a language at the beginning."""
        lang = simpledialog.askstring("Language Selection", "Choose a language (English / Polski):", initialvalue="English")
        return "Polski" if lang and lang.lower().startswith("p") else "English"

    def start_timer(self, event):
        """Starts the timer when the user begins typing."""
        if self.start_time is None:
            self.start_time = time.time()

    def update_speed(self, event):
        """Calculates and updates WPM and accuracy in real time."""
        if self.start_time is None:
            return

        elapsed_time = max(time.time() - self.start_time, 1)  # Avoid division by zero
        typed_text = self.text_entry.get("1.0", tk.END).strip()

        # Calculate words per minute
        word_count = len(typed_text.split())
        wpm = round((word_count / elapsed_time) * 60, 2)

        # Calculate accuracy
        original_words = self.sentence.split()
        typed_words = typed_text.split()
        correct_words = sum(1 for a, b in zip(original_words, typed_words) if a == b)
        accuracy = round((correct_words / max(len(original_words), 1)) * 100, 2)

        # Progress percentage
        progress = round((len(typed_text) / len(self.sentence)) * 100, 1)

        self.result_label.config(text=f"WPM: {wpm} | Accuracy: {accuracy}%" if self.language == "English" else f"Słowa/min: {wpm} | Dokładność: {accuracy}%")
        self.progress_label.config(text=f"Progress: {progress}%" if self.language == "English" else f"Postęp: {progress}%")

    def restart_test(self):
        """Resets the test with a new sentence."""
        self.start_time = None
        self.sentence = random.choice(SENTENCES[self.language])
        self.label_sentence.config(text=self.sentence)
        self.text_entry.delete("1.0", tk.END)
        self.result_label.config(text="WPM: 0 | Accuracy: 0%" if self.language == "English" else "Słowa/min: 0 | Dokładność: 0%")
        self.progress_label.config(text="Progress: 0%" if self.language == "English" else "Postęp: 0%")
        self.text_entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
