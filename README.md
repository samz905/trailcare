# Gemma 3N First-Aid Assistant

A fine-tuned Gemma 3N (4B) model specialized in providing first-aid medical advice and emergency care guidance. This project leverages advanced multimodal capabilities to understand text, images, and audio inputs for comprehensive healthcare assistance.

## Key Features

- **Multimodal Support**: Handles text, images, and audio inputs
- **Specialized Medical Knowledge**: Fine-tuned on first-aid procedures and emergency care
- **Efficient Training**: Uses Unsloth for fine-tuning with reduced memory usage
- **Mobile-Ready**: Designed for deployment with AI Edge for mobile applications
- **Local Testing**: Integrated with Ollama for local model testing and development

## Tech Stack

- **Fine-tuning**: Unsloth + LoRA (Low-Rank Adaptation)
- **Base Model**: Gemma 3N (4B)
- **Local Testing**: Ollama
- **Mobile Deployment**: AI Edge
- **Data Processing**: Custom ShareGPT format conversion
- **Training Framework**: HuggingFace Transformers, PEFT, TRL

## Prerequisites

- Python 3.8+
- CUDA-compatible GPU (recommended: 8GB+ VRAM)
- Ollama installed for local testing

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/samz905/trailcare
cd gemma-hackathon
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Install Ollama** (for local testing):
```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh
```

4. **Pull the Gemma 3N model in Ollama**:
```bash
ollama pull gemma3n:e4b
```

## Dataset

The project uses a comprehensive first-aid dataset covering:

- **Cuts & Abrasions**: Wound care and cleaning procedures
- **Sprains & Strains**: Muscle and joint injury treatment
- **Burns & Stings**: Emergency response for burns and insect stings
- **Fever & Infections**: Temperature management and basic care
- **Respiratory Issues**: Cough, congestion, and breathing problems
- **Digestive Problems**: Nausea, diarrhea, and stomach issues
- **Emergency Situations**: Choking, bleeding, and trauma response

### Data Format

The dataset is stored in two formats:
- **Raw Format**: `raw_data/intents.json` - Intent-based classification format
- **ShareGPT Format**: `processed_data/complete_manual_dataset_sharegpt.jsonl` - Conversational format for training

## Usage

### Local Testing with Ollama

Test the base model locally:
```bash
ollama run gemma3n:e4b
```

### Fine-tuning the Model

1. **Open the Jupyter notebook**:
```bash
jupyter notebook Finetune_Gemma3N_\(4B\).ipynb
```

2. **Follow the notebook sections**:
   - **Installation**: Install required packages
   - **Model Loading**: Load Gemma 3N with Unsloth optimizations
   - **Multimodal Testing**: Test image, text, and audio capabilities
   - **Fine-tuning**: Apply LoRA adapters and train on first-aid data

### Data Processing

Convert your data to ShareGPT format:
```bash
python convert_to_sharegpt.py
```

This script transforms the intent-based dataset into a conversational format suitable for fine-tuning.

## Model Capabilities

### Text-Based Queries
```python
messages = [{
    "role": "user",
    "content": [{"type": "text", "text": "What should I do for a minor cut?"}]
}]
```

### Image Analysis
```python
messages = [{
    "role": "user",
    "content": [
        {"type": "image", "image": "path/to/injury_image.jpg"},
        {"type": "text", "text": "What type of injury is this?"}
    ]
}]
```

### Audio Processing
```python
messages = [{
    "role": "user",
    "content": [
        {"type": "audio", "audio": "path/to/audio.mp3"},
        {"type": "text", "text": "What emergency situation is described?"}
    ]
}]
```

## Fine-tuning Configuration

The model uses the following LoRA configuration:
- **Rank (r)**: 8 - Balance between accuracy and efficiency
- **Target Modules**: Attention and MLP layers
- **Quantization**: 4-bit for reduced memory usage
- **Max Sequence Length**: 1024 tokens
- **Vision Layers**: Frozen (language-only fine-tuning)

## Mobile Deployment

The model is optimized for mobile deployment using AI Edge:

1. **Export the fine-tuned model**
2. **Convert to AI Edge format**
3. **Deploy to mobile applications**

*(Detailed mobile deployment instructions coming soon)*

## Testing

### Sample Queries

Try these example queries with the model:

- "How do I treat a bee sting?"
- "What should I do for someone who is choking?"
- "How can I stop bleeding from a deep cut?"
- "What are the signs of a sprained ankle?"

## Project Structure

```
gemma-hackathon/
├── Finetune_Gemma3N_(4B).ipynb    # Main fine-tuning notebook
├── convert_to_sharegpt.py          # Data format conversion
├── requirements.txt                # Python dependencies
├── raw_data/
│   └── intents.json               # Original intent-based dataset
├── processed_data/
│   ├── complete_manual_dataset.jsonl
│   └── complete_manual_dataset_sharegpt.jsonl
└── README.md                      
```

## Important Notes

- **Medical Disclaimer**: This model provides general first-aid guidance only. Always consult healthcare professionals for serious medical conditions.
- **GPU Requirements**: Fine-tuning requires a CUDA-compatible GPU with sufficient VRAM
- **Training Time**: Full fine-tuning may take several hours depending on hardware

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- **Unsloth**: For providing efficient fine-tuning capabilities
- **Google**: For the Gemma 3N base model
- **Ollama**: For local model testing infrastructure
- **HuggingFace**: For the transformers ecosystem

## Support

For questions or issues:
- Open an issue on GitHub
- Check the Unsloth documentation
- Review the Gemma model guidelines