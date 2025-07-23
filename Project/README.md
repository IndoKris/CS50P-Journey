# 📘 EduMaze – Personalized CLI Quiz Generator from Wikipedia

**EduMaze** is a command-line Python application that lets you generate personalized multiple-choice quizzes from any topic using real-time Wikipedia content. Whether you're preparing for exams, testing your general knowledge, or exploring new topics, EduMaze makes learning fun through interactive quizzes — all from your terminal.

---

## 🎯 Features

- 🔍 **Topic-Based Quiz Generation**  
  Input any topic (e.g., "Photosynthesis", "Albert Einstein") and instantly get a custom quiz.

- 🧠 **Wikipedia Integration**  
  Pulls factual data directly from Wikipedia summaries using the `wikipedia` module.

- 🎮 **Interactive CLI Quiz Experience**  
  Presents multiple-choice questions with randomized options and real-time feedback.

- 🧾 **Scoring System**  
  Tracks and displays your final score after each quiz session.

- 🎨 **Optional CLI Styling**  
  Uses `colorama` or `rich` for colored output and enhanced terminal UX.

---

## 🛠️ Technologies Used

| Technology       | Purpose                                      |
|------------------|----------------------------------------------|
| **Python 3**     | Core programming language                    |
| `wikipedia`      | Fetches topic summaries from Wikipedia       |
| `random`         | Randomizes quiz options                      |
| `re`, `textwrap` | Text parsing and CLI formatting              |
| `colorama`       | (Optional) Adds color to terminal output     |
| `rich` (optional)| (Alternative) Advanced CLI visuals           |

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/edumaze.git
cd edumaze

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# Run the app
python edumaze.py

