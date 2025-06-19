
NAME:SINDAYIGAYA SAMUEL
Reg no: 223004485
PROJECT TITLE:OOP Quiz Engine: Multiple User Quiz System
 How It Was Completed
Structures & Classes Used:
	struct Question: Represents each quiz question.
	class QuizUser (Abstract Class): Defines the interface for all user types.
	class RegisteredUser & class AnonymousUser: Implement QuizUser differently.
	class QuizEngine: Manages the quiz flow, questions, and users.
	Features Implemented:
	Dynamic arrays to store questions and users.
	Input validation for answers.
	Score tracking and result display.
	Use of virtual functions for polymorphic behavior.
Quiz Flow:
Users are added to the system.
Each user takes a quiz tailored to their type (Registered vs Anonymous).

are shown after each quiz.
 Code Overview
#include <iostream>
#include <cstring>
#include <iostream>`: Includes input/output functionality (e.g., `cin`, `cout`).
#include <cstring>`: Allows use of C-style string functions like `strcpy`, `strncpy`.
	Namespace Declaration
using namespace std;
 Makes all `std::` functions (like `cout`, `cin`) directly accessible.
Question Structure
struct Question {
   char prompt[100];
    char choices[4][40];
    int correctIdx;
};
Question`: Struct to hold a question and its answer choices.
prompt`: Stores the question text (up to 99 characters + null terminator).
choices[4][40]`: Stores 4 answer options, each up to 39 characters + null.
correctIdx`: Stores index (0–3) of the correct answer.
 Abstract Class - QuizUser
class QuizUser {
public:
    virtual int takeQuiz(Question* questions, int n) = 0;
    virtual ~QuizUser() {}
};
QuizUser`: Abstract base class for all quiz participants.
takeQuiz()`: A pure virtual function – **forces derived classes to implement quiz-taking behavior**.
QuizUser()`: Virtual destructor for proper memory cleanup when deleting polymorphic objects.
	RegisteredUser Class
class RegisteredUser : public QuizUser {
   char username[50];
RegisteredUser` inherits from `QuizUser`.
username`: Stores the registered user's name.
public:
    RegisteredUser(const char* name) {
        strncpy(username, name, 49);
        username[49] = '\0';
    }
 Constructor: Copies the user's name safely into `username`.
int takeQuiz(Question* questions, int n) {
        cout << "Registered User: " << username << " taking quiz.\n";
        int score = 0;
	Starts the quiz for a registered user and initializes score.

       for (int i = 0; i < n; ++i) {
            Question* q = questions + i;
            cout << q->prompt << "\n";
 Loops through all questions.
 `q' points to the current question.
Displays the question.
            for (int j = 0; j < 4; ++j) {
                cout << j + 1 << ". " << q->choices[j] << "\n";
            }
	Displays all four answer choices numbered from 1 to 4.
            int answer;
            while (true) {
                cout << "Your answer (1-4): ";
                cin >> answer;

•	Asks for user input and stores it in `answer.
 if (cin.fail() || answer < 1 || answer > 4) {
                    cin.clear();
                    cin.ignore(10000, '\n');
                    cout << "Invalid input. Try again.\n";
                } else {
                    cin.ignore(10000, '\n');
                    break;
                }
            }

•	Validates input to make sure it's a number from 1 to 4.

            if (answer - 1 == q->correctIdx) {
                cout << "Correct!\n";
                score++;
            } else {
                cout << "Wrong! Correct answer: " << q->choices[q->correctIdx] << "\n";
            }
            cout << "\n";
        }

 	Checks the answer and increments the score if correct.
 Shows feedback on each question.
  cout << "Score: " << score << " out of " << n << "\n";
        return score;
    }
};
At the end, the final score is displayed and returned.
 AnonymousUser Class
class AnonymousUser : public QuizUser {
public:
    int takeQuiz(Question* questions, int n) {
        cout << "Anonymous User taking quiz.\n";
        int score = 0;
•	Anonymous users do not have usernames.

        for (int i = 0; i < n; ++i) {
            Question* q = questions + i;
            cout << q->prompt << "\n";

            for (int j = 0; j < 4; ++j) {
                cout << (char)('A' + j) << ". " << q->choices[j] << "\n";
            }


•	Displays each question with options labeled A–D.

            char answer;
            while (true) {
                cout << "Your answer (A-D): ";
                cin >> answer;
                answer = toupper(answer);
	Accepts answer in letter form and converts to uppercase.
  if (answer < 'A' || answer > 'D') {
                    cin.clear();
                    cin.ignore(10000, '\n');
                    cout << "Invalid input. Try again.\n";
                } else {
                    cin.ignore(10000, '\n');
                    break;
                }
            }
 Input validation for answers A–D.
 int ansIndex = answer - 'A';
            if (ansIndex == q->correctIdx) {
                cout << "Correct!\n";
                score++;
            } else {
                cout << "Wrong! Correct answer: " << q->choices[q->correctIdx] << "\n";
            }
            cout << "\n";
        }
        cout << "Score: " << score << " out of " << n << "\n";
        return score;
    }
};

 Compares answer, updates score, and shows final result.
 QuizEngine Class

class QuizEngine {
    Question questions;
    int count, capacity;

	QuizUser users;
    int userCount, userCapacity;
 Holds dynamic arrays for `questions` and `users`.
count` and `capacity` track current and total number of questions/users.

public:
    QuizEngine() {
        questions = NULL;
        count = capacity = 0;
        users = NULL;
        userCount = userCapacity = 0;
    }

	Initializes everything to zero or null in the constructor.

    QuizEngine() {
        delete[] questions;
        for (int i = 0; i < userCount; i++) {
            delete users[i];
        }
        delete[] users;
    }
	Destructor cleans up dynamic memory (questions and users).
  void addQuestion(const Question& q) {
        if (count == capacity) {
            int newCap = (capacity == 0) ? 2 : capacity * 2;
            Question* newArr = new Question[newCap];
            for (int i = 0; i < count; i++) {
                newArr[i] = questions[i];
            }
            delete[] questions;
            questions = newArr;
            capacity = newCap;
        }
        questions[count++] = q;
    }
	Adds a question and resizes the array if needed.
void removeQuestion(int index) {
        if (index < 0 || index >= count) {
            cout << "Invalid index\n";
            return;
        }

        for (int i = index; i < count - 1; i++) {
            questions[i] = questions[i + 1];
        }

        count--;
    }

	Removes a question by shifting the array elements.
 void addUser(QuizUser user) {
        if (userCount == userCapacity) {
            int newCap = (userCapacity == 0) ? 2 : userCapacity  2;
            QuizUser newArr = new QuizUser [newCap];
            for (int i = 0; i < userCount; i++) {
                newArr[i] = users[i];
            }
            delete[] users;
            users = newArr;
            userCapacity = newCap;
        }
        users[userCount++] = user;
	Adds a user and resizes the user array dynamically.
    void runAllQuizzes() {
        for (int i = 0; i < userCount; i++) {
            cout << "\n--- Quiz for User " << i + 1 << " ---\n";
            users[i]->takeQuiz(questions, count);
            cout << "==========================\n";
        }
    }
};
 Runs the quiz for each user using polymorphism (`takeQuiz()` calls correct version).
	Main Function
int main() {
    QuizEngine engine;
	Creates the quiz engine object.
Question q1;
    strcpy(q1.prompt, "What is the capital of Rwanda?");
    strcpy(q1.choices[0], "Kigali");
    strcpy(q1.choices[1], "Nairobi");
    strcpy(q1.choices[2], "Kampala");
    strcpy(q1.choices[3], "Addis Ababa");
    q1.correctIdx = 0;
    engine.addQuestion(q1)
	Adds first question.
 Question q2;
    strcpy(q2.prompt, "What is the main language in Rwanda?");
    strcpy(q2.choices[0], "English");
    strcpy(q2.choices[1], "French");
    strcpy(q2.choices[2], "Kinyarwanda");
    strcpy(q2.choices[3], "Swahili");
    q2.correctIdx = 2;
    engine.addQuestion(q2);
	Adds second question.
engine.addUser(new RegisteredUser("Alice"));
    engine.addUser(new AnonymousUser());
 Adds a registered user and an anonymous user.
    engine.runAllQuizzes();
    return 0;
}

 Runs quizzes for all users and ends the program.

