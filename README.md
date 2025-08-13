# Doctor AI Chatbot – Your Personal Health Assistant

## Overview

Doctor AI is an intelligent, conversational health assistant built using **Python** and **Flask**. It recognizes common symptoms, provides medical advice and dosage suggestions, and uses **real-time geolocation** with **Google Maps API** to recommend the best nearby doctors. Whether you're feeling unwell or just curious, Doctor AI is ready to assist—right from your terminal or browser.

## Features

- **Symptom Recognition**: Detects common symptoms like fever, headache, and cold.
- **Health Advice**: Suggests relevant treatments, medicines, and proper dosages.
- **Doctor Finder**: Locates the best doctors near you using real-time GPS and Google Maps.
- **Nearby City Search**: Suggests doctors from nearby cities if none are available locally.
- **Input Handling**: Supports misspelled or capitalized symptom and city names.
- **Interactive Chat UI**: Clean, responsive web interface for easy interaction.
- **Result Caching**: Reduces API calls and improves performance.
- **Error Handling**: Ensures smooth user experience even with incomplete data.

## Installation

```bash
# Clone the repository
git clone https://github.com/irfanshakeel1094/Doctor-AI.git
cd Doctor-AI

# Create a virtual environment
python -m venv venv

# Activate the environment
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Setup

1. Create a `.env` file in the project root.
2. Copy contents from `.env.example`.
3. Add your **Google Maps API key**.

## Usage

```bash
# Run the Flask app
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

## Tech Stack

- Python 3.13
- Flask
- Geopy
- Google Maps Places API
- JavaScript (for geolocation)
- HTML + CSS

## License

© 2025 YourName. This project is protected by a strict license.  
You **may not** copy, sell, or replicate this idea without permission.

## Contributing

We welcome suggestions and improvements! Fork the repository, enhance symptom coverage, improve UI, or optimize performance—and submit a pull request.

## Contact

📧 Email: **irfanshakeel1094@gmail.com**  
🌐 GitHub: [Doctor AI Repository](https://github.com/irfanshakeel1094/Doctor-AI)
