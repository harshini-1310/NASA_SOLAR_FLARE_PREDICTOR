# NASA Solar Flare Predictor ☀️

A Machine Learning-based web application that predicts solar flare classes using NASA Solar Flare data. The project uses feature engineering, data preprocessing, and a Random Forest Classifier to analyze solar flare characteristics and generate predictions through an interactive Gradio interface.

## 🚀 Live Demo

Hugging Face Deployment:

https://harshinixiii-nasa-predictor.hf.space

## 📌 Project Overview

Solar flares are intense bursts of radiation from the Sun that can impact satellites, communication systems, navigation networks, and power grids on Earth.

This project leverages historical NASA solar flare data and machine learning techniques to predict the likely class of a solar flare based on various observational parameters.

## 🎯 Objectives

* Analyze NASA Solar Flare data
* Perform feature engineering and preprocessing
* Train a Machine Learning model for flare prediction
* Develop an interactive web interface
* Deploy the model for public use

## 📊 Dataset

The dataset contains solar flare observations collected from NASA records, including:

* Flare ID
* Begin Time
* Peak Time
* End Time
* Class Type
* Source Location
* Active Region Number
* Linked Events

## ⚙️ Feature Engineering

The following features were created and used for model training:

| Feature           | Description                        |
| ----------------- | ---------------------------------- |
| activeRegionNum   | Active solar region number         |
| linkedEvents      | Encoded linked event information   |
| duration_minutes  | Flare duration in minutes          |
| rise_time_minutes | Time taken to reach peak intensity |
| month             | Month of occurrence                |
| hour              | Hour of occurrence                 |

## 🤖 Machine Learning Model

### Algorithm Used

Random Forest Classifier

### Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Label Encoding
5. Train-Test Split
6. Feature Scaling
7. Model Training
8. Model Evaluation
9. Model Deployment

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Gradio
* Hugging Face Spaces
* Git
* GitHub

## 📂 Project Structure

```text
NASA_SOLAR_FLARE_PREDICTOR/
│
├── app.py
├── requirements.txt
├── solar_flare_rf.pkl
├── solar_flare_scaler.pkl
├── solar_flare_encoder.pkl
├── README.md
└── flares.ipynb
```

## ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/harshini-1310/NASA_SOLAR_FLARE_PREDICTOR.git
cd NASA_SOLAR_FLARE_PREDICTOR
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

## 🖥️ Usage

Enter the following values:

* Active Region Number
* Linked Events
* Duration
* Rise Time
* Month
* Hour

Click **Submit** to obtain the predicted solar flare class.

## 🌐 Deployment

The application is deployed on Hugging Face Spaces using Gradio.

Live Application:

https://huggingface.co/spaces/Harshinixiii/NASA_PREDICTOR

## 📈 Future Improvements

* Neural Network-based prediction models
* Confidence score visualization
* Advanced feature engineering
* Real-time solar activity integration
* Performance comparison across multiple models
* Interactive analytics dashboard



Built using Machine Learning, Gradio, and NASA Solar Flare data to explore space weather prediction and deployment of AI-powered applications.
