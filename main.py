from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Categorizing 'confidence' into Low, Medium, High
def categorize_confidence(conf):
    if conf < 50:
        return "Low"
    elif 50 <= conf <= 80:
        return "Medium"
    else:
        return "High"

# Apply categorization
data['confidence_category'] = data['confidence'].apply(categorize_confidence)

# Selecting relevant features and target
features = ['brightness', 'latitude', 'longitude', 'frp', 'bright_t31']
target = 'confidence_category'

# Encode categorical target
label_encoder = LabelEncoder()
data['confidence_encoded'] = label_encoder.fit_transform(data[target])

# Splitting data into train and test sets
X = data[features]
y = data['confidence_encoded']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predictions and Evaluation
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred, target_names=label_encoder.classes_)

accuracy, classification_rep
