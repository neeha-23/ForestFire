# ForestFire
This project focuses on detecting and analyzing forest fires in the Amazon Rainforest using data from the MODIS satellite. Spanning a decade (2013–2023), the dataset includes vital parameters such as brightness, confidence, and fire radiative power (FRP). The goal is to develop an efficient data analytic solution to classify fire occurrences, evaluate fire intensity, and identify contributing factors. Data preprocessing and manipulation were performed extensively for Logistic Regression and reused across other techniques to maintain consistency. Leveraging machine learning models like Random Forest, Neural Networks, and XGBoost, we determined Random Forest as the most effective technique for this problem. Challenges included handling missing data, integrating multiple datasets, and ensuring model interpretability. Key findings reveal that Random Forest’s robustness and feature importance analysis make it an ideal choice for large-scale fire monitoring. The results have significant implications for environmental policy and resource management.
##Introduction:
Problem Description: Forest fires pose a significant threat to biodiversity, climate stability, and human livelihoods. The Amazon Rainforest, often referred to as the "lungs of the Earth," is particularly vulnerable to fires. Detecting and analyzing fire events is vital for preventing extensive damage and guiding mitigation efforts.
Motivation: Addressing this problem is crucial to understanding the factors contributing to fire events, improving response strategies, and safeguarding the ecosystem. By leveraging advanced data analytics and machine learning, this project aims to provide actionable insights for stakeholders.
Approach: We adopted a data-driven approach, utilizing MODIS satellite data for fire detection and classification. Our solution involves:
1.	Preprocessing raw data to extract meaningful features.
2.	Employing multiple machine learning models to classify fire events.
3.	Comparing model performance to identify the best-fit algorithm.
Research Outcomes:
•	Improved detection of fire intensity and frequency.
•	Identification of key contributing factors.
•	Enhanced data-driven decision-making for policymakers.
Significance: The project contributes to the existing body of knowledge by integrating diverse machine learning techniques for forest fire analysis. The outcomes provide tools for environmental monitoring and resource allocation.
Original Data Description:
Data Source:
The dataset was collected from the MODIS satellite, spanning 2013–2023. This dataset includes vital parameters for analyzing forest fire events:
•	Latitude and longitude.
•	Brightness and confidence levels.
•	Fire radiative power (FRP).
•	Acquisition date and time.
•	Satellite and instrument information.
File Format:
The dataset is provided in Excel format (modis_Brazil.xlsx) and contains approximately [number of rows] rows and [number of columns] columns, detailing geographic and fire event data.
Data Types:
•	Numeric: Brightness, confidence, FRP.
•	Categorical: Satellite name, instrument type.
•	Temporal: Acquisition date and time.
Processing Requirements:
The original dataset was filtered and merged to focus on the Amazon Rainforest, resulting in a comprehensive dataset for analysis. Missing values were addressed through imputation, and columns unrelated to fire event classification were excluded.
Steps in the Code
1.	Import Libraries:
•	pandas for data manipulation.
•	matplotlib and seaborn for visualization.
•	sklearn for machine learning models, preprocessing, and evaluation metrics.
2.	Data Loading:
•	The dataset is loaded from an Excel file.
3.	Data Preprocessing:
•	Unnecessary columns are dropped.
•	Categorical variables are encoded.
•	Missing values are handled by dropping rows with missing data.
•	Features are scaled using StandardScaler.
4.	Train-Test Split:
•	The data is split into training and testing sets (80% training, 20% testing).
5.	Model Building:
•	A Logistic Regression model is initialized and trained using the training data.
6.	Model Evaluation:
•	Predictions are made on the test set.
•	The model's accuracy, classification report, and confusion matrix are calculated.
•	ROC curves and precision-recall curves are plotted.
•	Feature importances are extracted and displayed.
7.	Visualization:
•	Confusion matrix heatmap.
•	ROC curves.
•	Precision-recall curves.
8.	Output:
•	The accuracy, classification report, confusion matrix, ROC curves, precision-recall curves, and feature importances are printed.
###Conclusion:
Summary: This project demonstrates the utility of machine learning for forest fire detection. Random Forest emerged as the best-fit model, providing high accuracy and actionable insights.
Challenges:
•	Handling missing values.
•	Balancing computational efficiency with model performance.
Future Directions:
•	Integrating real-time satellite data for continuous monitoring.
•	Expanding analysis to other geographic regions.
•	Enhancing model performance with deep learning techniques
