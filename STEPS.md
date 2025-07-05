🏕️ AI Emergency Relief App for Hikers
Offline. Multimodal. Life-saving.
Built with Gemma 3n for the Gemma Hackathon

🛠️ Build Plan 

✅ Step 1: Dataset Preparation
Goal: Build a solid base for fine-tuning: Emergency input → structured JSON output (steps)

Datasets:

Kaggle – First Aid Intents: https://www.kaggle.com/datasets/therealsampat/intents-for-first-aid-recommendations/data

HuggingFace – First Aid Dataset: https://huggingface.co/datasets/badri55/First_aid__dataset 

Tasks:

Clean and normalize inputs

Convert all outputs into structured JSON format:

{
  "input": "I have a deep cut on my leg and it's bleeding a lot.",
  "output": {
    "steps": [
      {
        "step": 1,
        "title": "Ensure Safety",
        "description": "Move away from potential hazards. Make sure the scene is safe.",
      },
      {
        "step": 2,
        "title": "Apply Pressure",
        "description": "Use a clean cloth or bandage to apply firm pressure on the wound.",
      },
      {
        "step": 3,
        "title": "Elevate the Limb",
        "description": "Raise the injured leg above heart level if possible."
      },
      {
        "step": 4,
        "title": "Seek Help",
        "description": "If bleeding doesn’t stop, contact emergency services or seek medical help."
      }
    ]
  }
}

Save as JSONL for fine-tuning

80/10/10 train/val/test split

✅ Step 2: Fine-Tune Gemma 3n (Text-to-JSON Steps)
Goal: Train Gemma 3n to respond with structured step-by-step guidance

Tools:

Gemma 3n 2B

Unsloth for efficient LoRA fine-tuning

Prompt template:

You're a first aid expert. Based on the emergency described, generate step-by-step JSON instructions with fields: step, title, and description.

Tasks:

Fine-tune using the structured dataset

Validate outputs for:

Correct JSON format

Relevance of steps

Clear and safe instructions

✅ Step 3: Multimodal Input with Gemma 3n
Goal: Let users send audio, image, video, or text — and send directly to Gemma 3n

Modes & Flow:

Mode	Input	Handling
Text	Typed in-app	Send to model as-is
Audio	User records voice	Send raw audio directly to Gemma 3n
Image	Take a photo	Send image file to Gemma 3n
Video	Short clip (≤10s)	Send directly; Gemma handles parsing

Note:
Gemma 3n handles all formats natively — no need for OCR or speech-to-text.

Prompt wrapper (if needed):

“This is an emergency report from a hiker. Return step-by-step JSON instructions to help the person.”

✅ Step 4: Flutter App (Offline, Multimodal, JSON UI)
Goal: Build a clean mobile UI to show numbered emergency steps from Gemma’s output

Screens:

Home: Select input type (text, voice, image, video)

Input Screen: Capture or enter input

Instructions Screen: Display numbered steps (from JSON)

UI Example:

Use ListView.builder on the steps array

Show:

step: as leading number

title: bold

description: smaller text

Tech Stack:

Flutter

Local Gemma 3n model (Ollama for offline, Unsloth for fine-tuning)

camera, file_picker (image and video only), video_player, etc.

Optional offline caching of recent results