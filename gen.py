import csv
import random

# Set a seed for reproducibility
random.seed(42)

# Create a list to store the data
dataset = []

# Manually generate data where more study hours result in higher exam scores
for study_hours in range(1, 21):
    # Allow for some random error in exam scores
    error = random.uniform(-2, 2)
    exam_score = min(study_hours + error, 20)  # Ensure the exam score doesn't exceed 20
    dataset.append([study_hours, exam_score])

# Define the CSV file path
csv_file_path = 'StudyExam.csv'

# Write the data to a CSV file
with open(csv_file_path, 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    
    # Write data
    csv_writer.writerows(dataset)

print(f"Manually generated CSV dataset has been created and saved to {csv_file_path}.")
