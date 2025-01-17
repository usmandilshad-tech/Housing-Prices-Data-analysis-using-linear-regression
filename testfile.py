
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Create sample data about hours studied and exam scores
hours_studied = np.array([[2], [4], [6], [8], [10]])  # Input (hours studied)
exam_scores = np.array([50, 60, 70, 80, 90])  # Output (exam scores)

# Create a model to predict exam scores based on hours studied
model = LinearRegression()
model.fit(hours_studied, exam_scores)

# Predict the score for a student who studied 7.5 hours
new_hours = np.array([[7.5]])
predicted_score = model.predict(new_hours)
print("Predicted score for 7.5 hours of study:", predicted_score[0])

# Create a clear and informative plot
plt.figure(figsize=(8, 6))
plt.scatter(hours_studied, exam_scores, color='blue', label='Original data')
plt.plot(hours_studied, model.predict(hours_studied), color='red', label='Regression line')
plt.scatter(new_hours, predicted_score, color='green', label='Predicted point')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.title('Predicting Exam Scores from Hours Studied')
plt.legend()
plt.show()


