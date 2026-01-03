# Personal Fitness Tracker Dashboard

## Project Overview
The Personal Fitness Tracker Dashboard is a Python-based, menu-driven application that allows users to log fitness activities, analyze health metrics, and visualize fitness progress.  
The project is designed as a final practical submission and follows Object-Oriented Programming (OOP) principles along with NumPy, Pandas, Matplotlib, and Seaborn.

---

## Objectives
- Allow users to dynamically enter fitness activity data
- Validate user input using control structures
- Perform numerical analysis using NumPy
- Handle and analyze data using Pandas
- Generate summary reports
- Visualize fitness progress using professional charts
- Ensure the program runs continuously until the user exits

---

## Features and Functionalities

### 1. Add Activity
- Users can enter:
  - Date (YYYY-MM-DD)
  - Activity Type
  - Duration (in minutes)
  - Calories Burned
- Invalid inputs are handled safely without stopping the program

---

### 2. View Metrics
Displays quick numerical insights:
- Total calories burned
- Average workout duration
- Total number of activities logged

---

### 3. Filter Activities
- Filter activities by activity type
- Filter activities by date range
- Helps in focused data analysis

---

### 4. Generate Report
Generates a detailed fitness report including:
- Activity frequency
- Daily average calories burned
- Percentage improvement over time
- Overall fitness summary

---

### 5. Visualize Data
Displays professional data visualizations:
- Bar Chart: Total time spent per activity
- Line Graph: Daily average calories burned
- Pie Chart: Activity distribution
- Heatmap: Correlation between duration and calories burned

---

### 6. Exit
- Safely exits the program
- The application runs continuously until the user chooses to exit

---

## Technologies Used

| Technology | Description |
|----------|------------|
| Python | Core programming language |
| Pandas | Data loading, cleaning, filtering, and grouping |
| NumPy | Numerical calculations such as averages and percentage improvement |
| Matplotlib | Data visualization |
| Seaborn | Advanced and professional visualizations |
| OOP | Structured and reusable code design |

---

## Project Structure

Personal_Fitness_Tracker/
│
├── fitness_tracker.py
├── fitness_activities.csv
└── README.md

---

## How to Run the Project

1. Install Python on your system
2. Install required libraries:
   pip install pandas numpy matplotlib seaborn
3. Run the project file:
   python fitness_tracker.py
4. Follow the menu options displayed on the screen

---

## Dataset Details
The dataset file (fitness_activities.csv) contains the following columns:
- Date
- Activity Type
- Duration (Minutes)
- Calories Burned

The dataset is dynamic and automatically updates as users add new activities.

---

## Error Handling
- Handles incorrect date formats
- Prevents text input in numeric fields
- Avoids program crashes due to invalid input
- Displays error messages and returns to the menu

---

## Academic Relevance
This project demonstrates:
- Control Structures (loops and conditional statements)
- Object-Oriented Programming concepts
- NumPy-based numerical analysis
- Pandas-based data handling
- Data visualization using Matplotlib and Seaborn

The project fully meets the requirements of a 50-mark final practical examination.

---

## Conclusion
The Personal Fitness Tracker Dashboard is a robust, user-friendly, and professional Python application that simulates real-world data analysis.  
It is suitable for academic submission, viva examination, and portfolio presentation.

