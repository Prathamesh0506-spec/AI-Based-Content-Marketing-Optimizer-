🚀 AI-Based Content Marketing Optimizer

Repo for AI-Powered Marketing Automation Project

A next-generation, fully automated intelligence layer for digital marketing — engineered to generate, refine, evaluate, and continuously improve content using LLMs, sentiment engines, ML pipelines, and seamless integrations.

🌟 Overview

The AI-Based Automated Content Marketing Optimizer is an end-to-end system designed to elevate the entire digital content lifecycle.

Instead of manually crafting, testing, and adjusting content, this platform automates the full journey:

AI-generated content using LLaMA / Gemini models

Sentiment & emotion understanding

Trend-aware content enhancement

A/B performance comparison

Real-time analytics & metric logging

ML-powered performance predictions

Automated retraining for continuous model improvement

Multiple intelligence components work together to create a smart, self-learning content engine that becomes better with every execution cycle.

🎛️ What the System Brings Together

LLM-Driven Content Generation (LLaMA + Gemini APIs)

Emotion + Sentiment Analysis Engine for tone & audience perception

Trend Optimization Layer to adapt content to real-time topics

A/B Variant Coach for probability-based winner prediction

Slack Alerts for instant performance updates

Google Sheets Sync for logging, analytics & traceability

Auto-Retrainer to refresh ML models using new campaign data

Interactive Streamlit Dashboard for insights, monitoring & manual control

🎯 Key Objectives
✔️ Fully Automated Content Pipeline

Generate, score, and optimize content using LLMs + sentiment analysis + trend signals — entirely hands-free.

✔️ Predictive Content Intelligence

Leverages historical metrics & A/B results to forecast which content will deliver superior performance.

✔️ Continuous ML Model Retraining

The system adapts by learning from engagement metrics, sentiment outputs, and A/B results — ensuring long-term accuracy.

✔️ Centralized Dashboard & Insights

A clean Streamlit interface that unifies content creation, evaluation, metrics tracking, A/B analysis, and ML training controls.

🧠 System Architecture (High-Level)
1. Content Engine

Files:

content_generator.py

dynamic_prompt.py

trend_based_optimizer.py

Responsibilities:

Create multi-variant content using LLMs

Generate dynamic prompts

Inject keyword + platform context

Apply trend-aware scoring & optimization

2. Sentiment & Emotion Engine

File:

sentiment_analyzer.py

Capabilities:

Multi-label sentiment + emotion recognition

Polarity, mood & toxicity scores

Trend-aware fusion scoring

Google Sheets logging

Multi-language compatibility

3. A/B Testing Coach

File:

ab_coach.py

Capabilities:

Variant scoring logic

Probability-based winner prediction

Automated result selection

Optional Slack summary

4. Metrics Hub & Tracker

Files:

metrics_hub.py

metrics_tracker.py

tracker.py

Responsibilities:

Store daily marketing KPIs

Track impressions, CTR, sentiment, conversions

Combine trend + sentiment + performance

Feed ML training pipeline

5. ML Engine (Training + Auto-Retrainer)

Files:

train_model.py

auto_retrainer.py

Features:

RandomForest classifier with tuning

SMOTE balancing

Automatic model versioning

Scheduled retraining

Slack notifications after retrain

6. Integrations Layer

Files:

sheets_connector.py

slack_notifier.py

trend_fetcher.py

Used For:

Google Sheets API access

Slack-based alerts & summaries

Fetching and interpreting real-time trends

7. Streamlit Dashboard

File:

streamlit_app.py

Tabs Include:

Content generator

Sentiment engine

Trend analysis

A/B testing

Metrics overview

Manual/Auto ML training

Slack notifications

8. Pipeline Orchestration

File:

run.py — orchestrates the entire workflow:

Generate content

Apply trend optimization

Sentiment & emotion scoring

A/B evaluation

Push metrics to Sheets

Auto-retrain ML model

Slack summary report



## 📁 Project Folder Structure

```none
AI-Based-Content-Marketing-Optimizer/
│
├── app/
│   ├── content_engine/
│   │   ├── content_generator.py
│   │   ├── dynamic_prompt.py
│   │   └── trend_based_optimizer.py
│   │
│   ├── sentiment_engine/
│   │   └── sentiment_analyzer.py
│   │
│   ├── integrations/
│   │   ├── sheets_connector.py
│   │   ├── slack_notifier.py
│   │   └── trend_fetcher.py
│   │
│   ├── metrics_engine/
│   │   ├── metrics_hub.py
│   │   ├── metrics_tracker.py
│   │   └── tracker.py
│   │
│   ├── ab_testing/
│   │   └── ab_coach.py
│   │
│   ├── ml_engine/
│       ├── train_model.py
│       └── auto_retrainer.py
│
├── streamlit_app.py
├── run.py
├── requirements.txt
├── LICENSE
└── README.md
```



🌟 Features in Detail
🚀 AI Content Generator

Produces multiple platform-ready content variations

Injects keywords, tone, persona & audience context

Handles platform formatting styles

Optional trend-based rewriting for relevancy

Adaptive prompt-building logic

Source: content_generator.py

📈 Trend-Aware Optimization

The trend engine enhances generated content by matching current keywords, hashtags, and emerging digital patterns — keeping content fresh and aligned with what’s trending.

💬 Deep Sentiment + Emotion Analysis

Sentiment labels (Positive / Neutral / Negative)

Polarity scoring

Emotion tagging (Joy, Anger, Fear, Surprise, etc.)

Toxicity estimation

Trend–sentiment fusion score

Multi-language detection

🆚 A/B Variant Coach

Uses a weighted scoring approach to estimate which content version (A or B) will perform better.

Variant scoring

Probabilistic performance prediction

Automated winner suggestion

Slack notification support

📊 Metrics Engine & Sheets Integration

Stores marketing KPIs such as:

Impressions

Clicks

CTR

Trend score

Sentiment outputs

Conversions

These values feed into the ML model for continuous improvement.

🤖 ML Model Training & Auto-Retraining

RandomForestClassifier

GridSearchCV hyperparameter tuning

SMOTE balancing

Automatic versioning of trained models

Scheduled retraining via AutoRetrainer

Slack notifications after retraining

🔔 Slack Notification System

A/B test winner summaries

Model retraining updates

Custom alerts

Periodic content performance summaries

🖥️ Streamlit Dashboard

A complete UI that allows you to interact with all engines:

Generate content

Analyze sentiment

Compare A/B versions

Monitor metrics

Run auto or manual model training

Configure Slack notifications

View system summaries

🔧 Installation
1. Clone the repo
git clone https://github.com/Prathamesh0506-spec/AI-Based-Content-Marketing-Optimizer-.git
cd AI-Based-Content-Marketing-Optimizer-

2. Create & Activate Virtual Environment
python -m venv venv


Mac/Linux

source venv/bin/activate


Windows

venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Configure environment

Place your credentials inside:

/credentials
.env

5. Environment Variables

Create your .env file:

# Groq
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.3-70b-versatile
GROQ_TEMPERATURE=0.7

# Google Gemini
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-1.5-flash

# Twitter/X API
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_secret_key
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_SECRET=your_access_secret
TWITTER_BEARER_TOKEN=your_bearer_token

# Google Sheets
GOOGLE_SHEET_ID=your_google_sheet_id

# Service account JSON
GOOGLE_APPLICATION_CREDENTIALS=credentials/service_account.json

# Slack
SLACK_WEBHOOK_URL=your_slack_webhook_url

# Internals
MODEL_DIR=models
METRICS_RETRY_LIMIT=3
STREAMLIT_DEBUG=false

ENABLE_TRENDING=true
ENABLE_SENTIMENT=true
ENABLE_SHEETS_LOGGING=true
ENABLE_SLACK_NOTIFICATIONS=true


(Ignored automatically via .gitignore)

6. Run the Streamlit app
streamlit run streamlit_app.py

7. Run the full pipeline
python run.py

🔄 How the Full Pipeline Works

(Managed by run.py)

1️⃣ Generate content variations
2️⃣ Apply trend optimization
3️⃣ Sentiment & emotion scoring
4️⃣ A/B evaluation
5️⃣ Push metrics to Google Sheets
6️⃣ Auto-retrain ML model
7️⃣ Slack summary notification

🤖 ML Model Output

Training pipeline outputs:

models/predictor.joblib — latest active model

models/predictor_TIMESTAMP.joblib — archived versions

AutoRetrainer outputs:

models/model_TIMESTAMP.pkl

👥 Contributors
🧑‍💼 Project Lead

Charan Teja Mangali — Lead Developer, System Architect & Mentor

🎓 Student Contributors

Prathamesh Ohol

🤝 Contributing

Pull requests are welcome.
Feel free to open issues for suggestions, improvements, or bug reports.

📜 License

This project is licensed under the MIT License.

⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub —
it helps support future improvements!
