# Alarm Clock Script

The **Alarm Clock Script** is a simple Python program designed to allow users to set alarms based on specific times. Upon reaching the set alarm time, the script triggers an alarm sound to notify the user.

## Purpose

The purpose behind creating this script is to further my understanding with Python. The `alarm_original.py` script was created during my Data Science education at EC Utbildning (2022-2024), and the other was created afterwards to try and improve it with the help of TKinter GUI.

## Flowchart

Below is a flowchart depicting the basic structure, logic and the flow of the alarm clock script that was used:

<img src="docs/alarm_clock.svg" alt="Flowchart alarm_clock" width="800" height="600">

## How to Use

1. **Setup**:
   - Ensure Python is installed on your system.
   - Clone or download the script to your local machine.

2. **Run the Script**:
   - Open your terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using Python:
     ```
     python alarm_original.py
     ```
     or
     
     ```
     python alarm.py
     ```

3. **Set an Alarm**:
   - Follow the prompts to enter the desired alarm time.
   - Once the alarm time is reached, an alarm sound will play.

4. **Exit the Script**:
   - To stop the script, press `Ctrl+C` in the terminal or command prompt.

## Requirements

- Python 3.x
- `winsound` library (for playing sound on Windows)