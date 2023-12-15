#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with answer key
# Usage : Update the value of n with the required number of quizzes. Run the script.

import random
import data

# The quiz data. {state: capital}
states = list(data.states.keys())
capitals = list(data.states.values())

# Generate n quiz files
def generateQuiz(n):
    for quizNum in range(1, n+1):
        # Create quiz and answer key files
        quizFile = open(".\capitalQuiz{}.txt".format(quizNum), "w")
        ansKeyFile = open(".\capitalQuizKey{}.txt".format(quizNum), "w")

        # Create header fields 
        quizFile.write("Name:\nDate:\n\n")
        quizFile.write("{} State Capitals Quiz Form {}\n\n".format(" " * 20, quizNum))

        # Shuffle order of states
        random.shuffle(states)

        for ind, question in enumerate(states):
            # Creating a set of 4 options with 1 correct answer
            answer = data.states[question]
            capitals.remove(answer)
            options = random.sample(capitals, 3) + [answer]
            random.shuffle(options)

            # Re-insert the removed capital into the answers
            capitals.append(answer)

            # Writing questions and answers in the files
            quizFile.write("{}. What is the capital of {}\n".format(ind+1, question))
            for _ in range(4):
                quizFile.write("{}. {}\n".format("ABCD"[_], options[_]))
            quizFile.write("\n")
            ansKeyFile.write("{}. {}\n".format(ind+1, "ABCD"[options.index(answer)]))
        
        # Closing both files
        quizFile.close()
        ansKeyFile.close()

if __name__ == "__main__":
    n = 3
    generateQuiz(n)