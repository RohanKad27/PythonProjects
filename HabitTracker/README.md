# Personal Habit Tracker

A console-based Habit Tracker built with Python using Object-Oriented Programming, modular architecture, JSON persistence, and Python's standard library.

## Features
- Create habits
- View all habits
- Complete habits for the current day
- Prevent duplicate completion on the same day
- Remove habits
- Track habit age
- Track current streak
- Track longest streak
- Track total completions
- Calculate completion percentage
- View a monthly calendar for each habit
- View previous, current, and next month
- Generate habit statistics and reports
- Automatically save and load habit data using JSON
- Unique internal IDs using UUID

## Project Structure
```
HabitTracker/
│
├── main.py
│
├── models/
│   └── habit.py
│
├── managers/
│   └── habit_tracker.py
│
├── storage/
│   └── json_storage.py
│
├── reports/
│   └── stats.py
│
├── utils/
│   ├── validators.py
│   └── display.py
│
└── data/
    └── habits.json
```

## Technologies Used
- Python
- Object-Oriented Programming
- JSON
- datetime
- calendar
- statistics
- uuid

The project uses only Python's standard library, so no external packages are required.

## How It Works

Each habit is represented by a Habit object containing its name, creation date, unique ID, and completed dates.

HabitTracker manages the collection of habits and handles operations such as creating, completing, displaying, and removing habits.

Habit data is converted into a JSON-compatible format and stored in data/habits.json, allowing the application to preserve data between runs.

The application also calculates statistics such as completion percentage, average completions, current streak, longest streak, and the most completed habit.

## Example
```
==================================================
                  HABIT TRACKER
==================================================

1. Create Habit
2. Show Habit
3. Complete Habit
4. Remove Habit
5. Monthly Calendar
6. Habit Report
7. Exit
```