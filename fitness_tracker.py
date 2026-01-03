import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="darkgrid")

class FitnessTracker:

    def __init__(self, file_name):
        self.file_name = file_name

        if not os.path.exists(self.file_name):
            pd.DataFrame(
                columns=["Date", "Activity Type", "Duration", "Calories Burned"]
            ).to_csv(self.file_name, index=False)

        self.data = pd.read_csv(self.file_name)

        if not self.data.empty:
            self.data["Date"] = pd.to_datetime(self.data["Date"], errors="coerce")
            self.data["Duration"] = pd.to_numeric(self.data["Duration"], errors="coerce")
            self.data["Calories Burned"] = pd.to_numeric(self.data["Calories Burned"], errors="coerce")
            self.data.dropna(inplace=True)

    def add_activity(self):
        try:
            date = pd.to_datetime(input("Enter Date (YYYY-MM-DD): "))
            activity = input("Enter Activity Type: ")
            duration = int(input("Enter Duration (minutes): "))
            calories = int(input("Enter Calories Burned: "))

            if duration <= 0 or calories <= 0:
                print("\nDuration and Calories must be positive\n")
                return

            self.data = pd.concat([
                self.data,
                pd.DataFrame([{
                    "Date": date,
                    "Activity Type": activity,
                    "Duration": duration,
                    "Calories Burned": calories
                }])
            ], ignore_index=True)

            self.data.to_csv(self.file_name, index=False)
            print("\nActivity added successfully\n")

        except:
            print("\nInvalid input. Please try again.\n")

    def view_metrics(self):
        if self.data.empty:
            print("\nNo data available\n")
            return

        print("\n---- QUICK METRICS ----\n")
        print("Total Calories Burned :", self.data["Calories Burned"].sum())
        print("Average Duration      :", round(np.mean(self.data["Duration"]), 2), "minutes")
        print("Total Activities      :", len(self.data))
        print("\n-----------------------\n")

    def generate_report(self):
        if self.data.empty:
            print("\nNo data available\n")
            return

        daily_avg = (
            self.data
            .groupby("Date")["Calories Burned"]
            .mean()
            .reset_index()
            .sort_values("Date")
        )

        print("\n========== FITNESS REPORT ==========\n")

        print("Total Calories Burned :", self.data["Calories Burned"].sum())
        print("Average Duration      :", round(np.mean(self.data["Duration"]), 2), "minutes\n")

        print("Activity Frequency:")
        print(self.data["Activity Type"].value_counts(), "\n")

        print("Daily Average Calories:")
        print(daily_avg.tail(), "\n")

        if len(daily_avg) >= 2:
            improvement = (
                (daily_avg.iloc[-1]["Calories Burned"] -
                 daily_avg.iloc[0]["Calories Burned"]) /
                daily_avg.iloc[0]["Calories Burned"]
            ) * 100
            print("Percentage Improvement:", round(improvement, 2), "%")

        print("\n===================================\n")

    def filter_activities(self):
        if self.data.empty:
            print("\nNo data available\n")
            return

        print("\n1. Filter by Activity Type")
        print("2. Filter by Date Range\n")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                activity = input("Enter Activity Type: ")
                print("\nFiltered Data:\n")
                print(self.data[self.data["Activity Type"] == activity])

            elif choice == "2":
                start = pd.to_datetime(input("Enter Start Date (YYYY-MM-DD): "))
                end = pd.to_datetime(input("Enter End Date (YYYY-MM-DD): "))
                print("\nFiltered Data:\n")
                print(self.data[(self.data["Date"] >= start) & (self.data["Date"] <= end)])

            else:
                print("\nInvalid choice\n")
        except:
            print("\nInvalid input format\n")

    def visualize_data(self):
        if self.data.empty:
            print("\nNo data available for visualization\n")
            return

        daily = (
            self.data
            .groupby("Date")["Calories Burned"]
            .mean()
            .reset_index()
            .sort_values("Date")
        )

        fig, axes = plt.subplots(2, 2, figsize=(14, 10))

        sns.barplot(ax=axes[0, 0], data=self.data, x="Activity Type", y="Duration", estimator=sum,
                    palette="viridis")
        axes[0, 0].set_title("Total Time Spent per Activity")

        axes[0, 1].plot(daily["Date"], daily["Calories Burned"], marker="o")
        axes[0, 1].set_title("Daily Average Calories Burned")
        axes[0, 1].tick_params(axis="x", rotation=45)

        self.data["Activity Type"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=axes[1, 0], startangle=90
        )
        axes[1, 0].set_title("Activity Distribution")
        axes[1, 0].set_ylabel("")

        sns.heatmap(
            self.data[["Duration", "Calories Burned"]].corr(),
            annot=True,
            cmap="coolwarm",
            ax=axes[1, 1]
        )
        axes[1, 1].set_title("Correlation Heatmap")

        plt.suptitle("Personal Fitness Tracker Dashboard", fontsize=18)
        plt.tight_layout()
        plt.show()


tracker = FitnessTracker("fitness_activities.csv")

while True:
    print("---- PERSONAL FITNESS TRACKER ----")
    print("1. Add Activity")
    print("2. View Metrics")
    print("3. Filter Activities")
    print("4. Generate Report")
    print("5. Visualize Data")
    print("6. Exit\n")

    choice = input("Enter choice: ")

    if choice == "1":
        tracker.add_activity()
    elif choice == "2":
        tracker.view_metrics()
    elif choice == "3":
        tracker.filter_activities()
    elif choice == "4":
        tracker.generate_report()
    elif choice == "5":
        tracker.visualize_data()
    elif choice == "6":
        print("\nProgram exited safely\n")
        break
    else:
        print("\nPlease enter a valid option\n")
