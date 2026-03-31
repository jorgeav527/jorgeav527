+++
title = "How to Start with AI and Gemini on Linux"
date = 2024-05-15
+++

Starting your journey with AI on Linux is straightforward and powerful. Here's a simple, step-by-step guide to getting up and running with Google's Gemini.

## Prerequisites
Ensure your system is updated and you have Python installed:
```bash
sudo apt update && sudo apt upgrade
sudo apt install python3 python3-pip python3-venv
```

## Step 1: Get Your Gemini API Key
Head over to [Google AI Studio](https://aistudio.google.com/) and create a free API key for your project.

## Step 2: Set Up Your Project Environment
It's best practice to use a virtual environment:
```bash
mkdir my-ai-project && cd my-ai-project
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Install the Gemini Library
Install the official Google Generative AI package:
```bash
pip install -q -U google-generativeai
```

## Step 4: Your First AI Script
Create a file named `hello_gemini.py`:
```python
import google.generativeai as genai
import os

genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Give me a cool Linux tip!")
print(response.text)
```
Replace `"YOUR_API_KEY_HERE"` with your actual key and run it:
```bash
python3 hello_gemini.py
```

## Video Tutorial
For a deeper dive and a visual walkthrough, check out this excellent tutorial:
[YouTube: Master Gemini AI on Linux](https://www.youtube.com/watch?v=MsQACpcuTkU)
