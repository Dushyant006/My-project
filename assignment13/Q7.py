#Using "Customizing Matplotlib Visualizations" discussed in Numpy session4 notes plot graph to compare your at least 2 semester result
import numpy as np
import matplotlib.pyplot as plt
# Sample data for two semesters
semesters = ['Semester 1', 'Semester 2']
results_sem1 = [85, 90, 79, 95, 80]  # Sample results for Semester 1
results_sem2 = [80, 90, 80, 82, 90]  # Sample results for Semester 2
# Calculate average results for each semester
avg_sem1 = np.mean(results_sem1)
avg_sem2 = np.mean(results_sem2)
# Plotting the results
plt.figure(figsize=(10, 5))
plt.bar(semesters, [avg_sem1, avg_sem2], color=['blue', 'orange'])
plt.title('Average Results Comparison Between Two Semesters')
plt.xlabel('Semesters')
plt.ylabel('Average Result')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()