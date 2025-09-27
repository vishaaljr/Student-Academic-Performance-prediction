# 🎓 Student Academic Performance Predictor

This is a **Streamlit web app** that predicts a student’s academic performance based on various features such as study hours, attendance, past scores, internet access, extracurricular activities, and educational background. The app uses a **trained machine learning model** to provide predictions in real time.

---

## **Features**

* Interactive web interface built with Streamlit
* Inputs include:

  * Gender
  * Study Hours per Week
  * Attendance Rate (%)
  * Past Exam Scores
  * Internet Access at Home
  * Extracurricular Activities
  * Educational Background (Bachelors, Masters, PhD)
* Predicts **academic performance** (numerical score)
* Real-time predictions with a single button click

---

## **Installation**

1. **Clone the repository**

```bash
git clone https://github.com/your-username/student-performance-predictor.git
cd student-performance-predictor
```

2. **Create and activate a virtual environment**

```bash
python -m venv myenv
myenv\Scripts\activate   # Windows
# OR
source myenv/bin/activate # macOS/Linux
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Make sure your trained model file is present**

* The trained model should be named: `Student_academic_performance.joblib`

---

## **Usage**

Run the Streamlit app:

```bash
streamlit run app.py
```

* Open the link in your browser (usually `http://localhost:8501`)
* Enter student details and click **Predict Performance** to see the prediction.

---

## **Project Structure**

```
student-performance-predictor/
│
├─ app.py                         # Main Streamlit app
├─ Student_academic_performance.joblib  # Trained ML model
├─ requirements.txt               # Python dependencies
└─ README.md                      # Project documentation
```

---

## **Dependencies**

* Python 3.8+
* Streamlit
* numpy
* pandas
* matplotlib
* seaborn
* scikit-learn
* joblib

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## **How to Train Your Own Model (Optional)**

If you want to retrain the model with your own data:

```python
from sklearn.linear_model import LinearRegression
import joblib
import pandas as pd

# Load your dataset
data = pd.read_csv("your_dataset.csv")
X = data[['Gender','Study_Hours_per_Week','Attendance_Rate','Past_Exam_Scores',
          'Internet_Access_at_Home','Extracurricular_Activities','Bachelors','Masters','PhD']]
y = data['Academic_Performance']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, "Student_academic_performance.joblib")
```

---



