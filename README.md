# Python Multi-Tool Utility Program (plp-python-week8)

## What the Toolkit Does
This project is an interactive command-line application featuring a centralized menu system that allows users to seamlessly switch between three different utility tools:
1. **Number Guessing Game**: Tests your luck and intuition by having you guess a randomly generated number with dynamic feedback loops.
2. **Quick To-Do List Manager**: Lets you dynamically build, view, and clear tasks during runtime using lists.
3. **Tip Calculator**: Computes accurate tip totals and overall bill summaries using conditional logic and formatted outputs.

## How to Run It
1. Ensure you have Python installed on your system.
2. Open your terminal or command prompt in the project directory.
3. Run the application using the following command:
   ```bash
   python toolkit.py
   ```

## Reflection

Building this multi-tool application brought together everything learned in previous weeks, combining loops, conditionals, data structures, and functions. The hardest part was designing robust error handling for user inputs so that unexpected keystrokes or letters wouldn't crash the program mid-execution. The bug that took the longest to fix involved managing infinite loops when unexpected `ValueError` exceptions occurred in nested loops. With one more week of learning, I would add persistent file storage so that the To-Do List manager can save tasks to a local text file between sessions.
