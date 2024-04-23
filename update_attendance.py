import json
import pandas as pd
from datetime import datetime


def update_attendance(Users_file, Recognized_faces):
    # Load registered faces from Users.json
    with open(Users_file, 'r') as f:
        registered_faces = json.load(f)

    # Get current date
    current_date = datetime.now().strftime('%d-%m-%Y')

    # Check if the Excel file exists
    try:
        attendance_df = pd.read_excel('Attendance.xlsx')
    except FileNotFoundError:
        # Create an empty DataFrame if the file doesn't exist
        attendance_data = {'Students': list(registered_faces.values())}
        attendance_df = pd.DataFrame(attendance_data)

    # Add a new column for the current date if it doesn't exist
    if current_date not in attendance_df.columns:
        attendance_df[current_date] = 'Absent'

    # Update attendance for recognized faces
    for face in Recognized_faces:
        for user_id, user_name in registered_faces.items():
            if face == user_name:
                attendance_df.loc[attendance_df['Students'] == user_name,
                                  current_date] = datetime.now().strftime('%H:%M:%S')
                break

    # Save to Excel file
    attendance_df.to_excel('Attendance.xlsx', index=False)
