#include <iostream>  // Standard input/output stream library
#include <cstring>   // C-style string manipulation functions

using namespace std; // Standard namespace to avoid std:: prefixes

// Structure to hold a single quiz question
struct Question {
    char prompt[100];     // The question text (max 99 chars + null terminator)
    char choices[4][40];  // Array of 4 possible answers (each max 39 chars + null)
    int correctIdx;       // Index (0-3) of the correct answer
};

// Abstract base class for quiz users
class QuizUser {
public:
    // Pure virtual function - must be implemented by derived classes
    virtual int takeQuiz(Question* questions, int n) = 0;
    
    // Virtual destructor for proper cleanup of derived classes
    virtual ~QuizUser() {}
};

// Concrete class for registered users
class RegisteredUser : public QuizUser {
    char username[50];  // Stores the registered user's name
    
public:
    // Constructor that initializes the username
    RegisteredUser(const char* name) {
        // Copy at most 49 characters to prevent buffer overflow
        strncpy(username, name, 49);
        username[49] = '\0'; // Ensure null-termination
    }

    // Implementation of takeQuiz for registered users
    int takeQuiz(Question* questions, int n) {
        // Display user information
        cout << "Registered User: " << username << " taking quiz.\n";
        int score = 0;  // Initialize score counter
        
        // Loop through all questions
        for (int i = 0; i < n; ++i) {
            // Get current question using pointer arithmetic
            Question* q = questions + i;
            
            // Display question prompt
            cout << q->prompt << "\n";
            
            // Display all choices (numbered 1-4)
            for (int j = 0; j < 4; ++j) {
                cout << j + 1 << ". " << q->choices[j] << "\n";
            }

            int answer;  // Variable to store user's answer
            
            // Input validation loop
            while (true) {
                cout << "Your answer (1-4): ";
                cin >> answer;  // Get user input

                // Check for invalid input
                if (cin.fail() || answer < 1 || answer > 4) {
                    cin.clear();  // Clear error flags
                    cin.ignore(10000, '\n');  // Discard bad input
                    cout << "Invalid input. Try again.\n";
                } else {
                    cin.ignore(10000, '\n');  // Clean up input buffer
                    break;  // Exit validation loop
                }
            }

            // Check if answer is correct
            if (answer - 1 == q->correctIdx) {
                cout << "Correct!\n";
                score++;  // Increment score
            } else {
                // Show correct answer if wrong
                cout << "Wrong! Correct answer: " << q->choices[q->correctIdx] << "\n";
            }
            cout << "\n";  // Add spacing between questions
        }
        
        // Display final score
        cout << "Score: " << score << " out of " << n << "\n";
        return score;  // Return the final score
    }
};

// Concrete class for anonymous users
class AnonymousUser : public QuizUser {
public:
    // Implementation of takeQuiz for anonymous users
    int takeQuiz(Question* questions, int n) {
        cout << "Anonymous User taking quiz.\n";
        int score = 0;  // Initialize score counter
        
        // Loop through all questions
        for (int i = 0; i < n; ++i) {
            // Get current question using pointer arithmetic
            Question* q = questions + i;
            
            // Display question prompt
            cout << q->prompt << "\n";
            
            // Display all choices (lettered A-D)
            for (int j = 0; j < 4; ++j) {
                cout << (char)('A' + j) << ". " << q->choices[j] << "\n";
            }

            char answer;  // Variable to store user's answer
            
            // Input validation loop
            while (true) {
                cout << "Your answer (A-D): ";
                cin >> answer;  // Get user input
                answer = toupper(answer);  // Convert to uppercase

                // Check for invalid input
                if (answer < 'A' || answer > 'D') {
                    cin.clear();  // Clear error flags
                    cin.ignore(10000, '\n');  // Discard bad input
                    cout << "Invalid input. Try again.\n";
                } else {
                    cin.ignore(10000, '\n');  // Clean up input buffer
                    break;  // Exit validation loop
                }
            }

            // Convert letter answer to index (0-3)
            int ansIndex = answer - 'A';
            
            // Check if answer is correct
            if (ansIndex == q->correctIdx) {
                cout << "Correct!\n";
                score++;  // Increment score
            } else {
                // Show correct answer if wrong
                cout << "Wrong! Correct answer: " << q->choices[q->correctIdx] << "\n";
            }
            cout << "\n";  // Add spacing between questions
        }
        
        // Display final score
        cout << "Score: " << score << " out of " << n << "\n";
        return score;  // Return the final score
    }
};

// Main quiz engine class
class QuizEngine {
    Question* questions;  // Dynamic array of questions
    int count;           // Current number of questions
    int capacity;        // Current capacity of questions array

    QuizUser** users;     // Dynamic array of user pointers
    int userCount;       // Current number of users
    int userCapacity;    // Current capacity of users array

public:
    // Constructor - initialize all pointers to NULL and counts to 0
    QuizEngine() {
        questions = NULL;
        count = capacity = 0;
        users = NULL;
        userCount = userCapacity = 0;
    }

    // Destructor - clean up all dynamically allocated memory
    ~QuizEngine() {
        delete[] questions;  // Free questions array
        
        // Free each user object and then the users array
        for (int i = 0; i < userCount; i++) {
            delete users[i];
        }
        delete[] users;
    }

    // Add a new question to the quiz engine
    void addQuestion(const Question& q) {
        // Check if we need to resize the array
        if (count == capacity) {
            // Calculate new capacity (double current or start with 2)
            int newCap = (capacity == 0) ? 2 : capacity * 2;
            
            // Allocate new array
            Question* newArr = new Question[newCap];
            
            // Copy existing questions
            for (int i = 0; i < count; i++) {
                newArr[i] = questions[i];
            }
            
            // Free old array and update pointers
            delete[] questions;
            questions = newArr;
            capacity = newCap;
        }
        
        // Add new question and increment count
        questions[count++] = q;
    }

    // Remove a question by index
    void removeQuestion(int index) {
        // Validate index
        if (index < 0 || index >= count) {
            cout << "Invalid index\n";
            return;
        }
        
        // Shift all questions after the index down by one
        for (int i = index; i < count - 1; i++) {
            questions[i] = questions[i + 1];
        }
        
        count--;  // Decrement count
    }

    // Add a new user to the quiz engine
    void addUser(QuizUser* user) {
        // Check if we need to resize the array
        if (userCount == userCapacity) {
            // Calculate new capacity (double current or start with 2)
            int newCap = (userCapacity == 0) ? 2 : userCapacity * 2;
            
            // Allocate new array
            QuizUser** newArr = new QuizUser*[newCap];
            
            // Copy existing users
            for (int i = 0; i < userCount; i++) {
                newArr[i] = users[i];
            }
            
            // Free old array and update pointers
            delete[] users;
            users = newArr;
            userCapacity = newCap;
        }
        
        // Add new user and increment count
        users[userCount++] = user;
    }

    // Run all quizzes for all registered users
    void runAllQuizzes() {
        // Loop through all users
        for (int i = 0; i < userCount; i++) {
            // Display user header
            cout << "\n--- Quiz for User " << i + 1 << " ---\n";
            
            // Polymorphic call to takeQuiz (behavior depends on actual user type)
            users[i]->takeQuiz(questions, count);
            
            // Display separator
            cout << "==========================\n";
        }
    }
};

// Main function - entry point of the program
int main() {
    // Create quiz engine instance
    QuizEngine engine;

    // Add question 1
    Question q1;
    strcpy(q1.prompt, "What is the capital of Rwanda?");
    strcpy(q1.choices[0], "Kigali");
    strcpy(q1.choices[1], "Nairobi");
    strcpy(q1.choices[2], "Kampala");
    strcpy(q1.choices[3], "Addis Ababa");
    q1.correctIdx = 0;
    engine.addQuestion(q1);

    // Add question 2
    Question q2;
    strcpy(q2.prompt, "What is the main language in Rwanda?");
    strcpy(q2.choices[0], "English");
    strcpy(q2.choices[1], "French");
    strcpy(q2.choices[2], "Kinyarwanda");
    strcpy(q2.choices[3], "Swahili");
    q2.correctIdx = 2;
    engine.addQuestion(q2);

    // Add users
    engine.addUser(new RegisteredUser("Alice"));  // Registered user
    engine.addUser(new AnonymousUser());         // Anonymous user

    // Run all quizzes
    engine.runAllQuizzes();

    return 0;  // Exit program
}
