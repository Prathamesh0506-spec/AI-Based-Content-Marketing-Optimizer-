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

LLM-driven content generation (LLaMA + Gemini APIs)

Emotion + sentiment analysis engine

Trend optimization layer

A/B variant coach

Slack alerts

Google Sheets sync

Auto-retrainer

Streamlit dashboard

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

Create multi-variant content

Generate dynamic prompts

Inject keywords & platform context

Apply trend-aware optimization

2. Sentiment & Emotion Engine

File:

sentiment_analyzer.py

Capabilities:

Multi-label sentiment + emotion recognition

Polarity & toxicity scoring

Trend-aware fusion

Sheets logging

Multi-language support

3. A/B Testing Coach

File:

ab_coach.py

Capabilities:

Variant scoring

Probability-based winner prediction

Automated selection

Optional Slack summary

4. Metrics Hub & Tracker

Files:

metrics_hub.py

metrics_tracker.py

tracker.py

Responsibilities:

Store KPIs

Track impressions, CTR, sentiment, conversions

Merge trend + sentiment + performance

Feed ML pipeline

5. ML Engine (Training + Auto-Retrainer)

Files:

train_model.py

auto_retrainer.py

Features:

RandomForest classifier

SMOTE balancing

Auto model versioning

Scheduled retraining

Slack notifications

6. Integrations Layer

Files:

sheets_connector.py

slack_notifier.py

trend_fetcher.py

Used For:

Sheets API

Slack alerts

Trend fetcher

7. Streamlit Dashboard

File:

streamlit_app.py

Tabs Include:

Content generator

Sentiment engine

Trend analysis

A/B testing

Metrics

ML training

Slack notifications

8. Pipeline Orchestration

File:

run.py

Workflow:

Generate content

Trend optimization

Sentiment scoring

A/B evaluation

Sheets push

Auto-retrain

Slack summary



📁 Project Folder Structure
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



🌟 Features in Detail
🚀 AI Content Generator

Produces multiple variants

Injects keywords, tone & persona

Handles platform formats

Optional trend-based rewriting

Adaptive prompt logic
Source: content_generator.py

📈 Trend-Aware Optimization

Aligns generated content with trending keywords, hashtags, and live context.

💬 Deep Sentiment + Emotion Analysis

Sentiment tags

Polarity score

Emotion labels

Toxicity estimation

Trend–sentiment fusion

Multi-language

🆚 A/B Variant Coach

Weighted scoring

Performance prediction

Auto-winner

Slack notifications

📊 Metrics Engine & Sheets Integration

Tracks:

Impressions

Clicks

CTR

Trend score

Sentiment

Conversions

Feeds ML model.

🤖 ML Model Training & Auto-Retraining

RandomForest

GridSearchCV

SMOTE

Versioning

Auto retrain

Slack updates

🔔 Slack Notification System

A/B summaries

Retrain updates

Custom alerts

Performance digests

🖥️ Streamlit Dashboard

Interact with:

Content generation

Sentiment

A/B tests

Metrics

ML training

Slack settings

🔧 Installation
1. Clone the repo
git clone https://github.com/Prathamesh0506-spec/AI-Based-Content-Marketing-Optimizer-.git
cd AI-Based-Content-Marketing-Optimizer-

2. Create & activate virtual environment
python -m venv venv


Mac/Linux:

source venv/bin/activate


Windows:

venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Configure environment

Place your credentials inside:

/credentials
.env

5. Environment Variables

(unchanged — your exact block kept intact)

6. Run Streamlit
streamlit run streamlit_app.py

7. Run Full Pipeline
python run.py

🔄 How the Full Pipeline Works

1️⃣ Generate content
2️⃣ Apply trends
3️⃣ Sentiment scoring
4️⃣ A/B evaluation
5️⃣ Sheets logging
6️⃣ Auto retrain
7️⃣ Slack summary

🤖 ML Model Output

models/predictor.joblib

models/predictor_TIMESTAMP.joblib

models/model_TIMESTAMP.pkl

👥 Contributors
🧑‍💼 Project Lead

Charan Teja Mangali — Lead Developer, System Architect & Mentor

🎓 Student Contributors

Prathamesh Ohol

🤝 Contributing

Pull requests & issues are welcome.

📜 License

MIT License.

⭐ Support

If you found this useful, consider giving it a ⭐ on GitHub — it motivates further improvements!
