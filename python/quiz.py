import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QGroupBox, QRadioButton, QMessageBox
from PyQt5.QtCore import Qt


class QuizGameApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quiz Game")
        self.setGeometry(100, 100, 400, 300)

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Paris", "Berlin", "Rome"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is closest to the sun?",
                "options": ["Mars", "Venus", "Mercury", "Jupiter"],
                "correct_answer": "Mercury"
            },
            {
                "question": "What is 5 + 3?",
                "options": ["6", "8", "10", "12"],
                "correct_answer": "8"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
                "correct_answer": "Leonardo da Vinci"
            },
            {
                "question": "Which of the following compiled ‘Encyclopedia of Astronomy’?",
                "options": ["Cloudius Ptolemy", "Galen", "Celsus", " Pliny"],
                "correct_answer": "Cloudius Ptolemy"
            },
            {
                "question": "Which city is the host of the ‘ODI Cricket World Cup 2023’??",
                "options": ["Chennai", "Mumbai", "Ahmedabad", "Kolkata"],
                "correct_answer": "Ahmedabad"
            },
            {
                "question": "Jizai Arms is developed in which country?",
                "options": ["India","Japan","South Korea", "USA"],
                "correct_answer": "Japan"
            },
            {
                "question": "Which country’s kabaddi team won the Asian Championships title?",
                "options": ["Pakistan"," Bangladesh","South Korea", "India"],
                "correct_answer": "India"
            
                
            }
        ]

        self.current_question = None
        self.score = 0
        self.question_index = 0

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.question_label = QLabel()
        layout.addWidget(self.question_label)

        self.answer_group = QGroupBox("Options")
        self.answer_layout = QVBoxLayout()
        self.answer_group.setLayout(self.answer_layout)
        layout.addWidget(self.answer_group)

        self.next_button = QPushButton("Next Question")
        self.next_button.clicked.connect(self.next_question)
        layout.addWidget(self.next_button)
        self.next_button.setEnabled(False)

        self.setLayout(layout)
        self.show_question()

    def show_question(self):
        if self.question_index >= len(self.questions):
            self.show_result()
            return

        self.current_question = random.choice(self.questions)
        self.questions.remove(self.current_question)

        self.question_label.setText(self.current_question["question"])

        self.clear_options()
        for option in self.current_question["options"]:
            radio_button = QRadioButton(option)
            radio_button.toggled.connect(self.enable_next_button)
            self.answer_layout.addWidget(radio_button)

        self.question_index += 1

    def clear_options(self):
        for i in reversed(range(self.answer_layout.count())):
            widget = self.answer_layout.itemAt(i).widget()
            self.answer_layout.removeWidget(widget)
            widget.deleteLater()

    def enable_next_button(self):
        self.next_button.setEnabled(True)

    def next_question(self):
        selected_option = None
        for i in range(self.answer_layout.count()):
            radio_button = self.answer_layout.itemAt(i).widget()
            if radio_button.isChecked():
                selected_option = radio_button.text()
                break

        if selected_option == self.current_question["correct_answer"]:
            self.score += 1
            self.show_feedback("Correct!", QMessageBox.Information)
        else:
            self.show_feedback("Incorrect! The correct answer is: " + self.current_question["correct_answer"], QMessageBox.Warning)

        self.show_question()

    def show_feedback(self, message, icon):
        feedback_box = QMessageBox(self)
        feedback_box.setIcon(icon)
        feedback_box.setWindowTitle("Feedback")
        feedback_box.setText(message)
        feedback_box.setStandardButtons(QMessageBox.Ok)
        feedback_box.exec_()

    def show_result(self):
        result_message = f"You scored {self.score} out of {self.question_index}!"
        result_message += "\nWell done!" if self.score >= self.question_index / 2 else "\nKeep practicing!"

        result_box = QMessageBox(self)
        result_box.setIcon(QMessageBox.Information)
        result_box.setWindowTitle("Quiz Result")
        result_box.setText(result_message)
        result_box.setStandardButtons(QMessageBox.Ok)
        result_box.exec_()

        play_again = QMessageBox.question(self, "Play Again", "Do you want to play again?", QMessageBox.Yes | QMessageBox.No)
        if play_again == QMessageBox.Yes:
            self.reset_game()
            self.show_question()
        else:
            self.close()

    def reset_game(self):
        self.score = 0
        self.question_index = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = QuizGameApp()
    game.show()
    sys.exit(app.exec_())
