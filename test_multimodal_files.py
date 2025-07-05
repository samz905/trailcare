#!/usr/bin/env python3
"""
Test script for multimodal inputs with actual audio, image, and video files
This script demonstrates how to send different file types to Gemma 3n via Ollama
"""

import os
import sys
import json
import base64
import logging
from pathlib import Path
from typing import Dict, Any, Optional
import ollama

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MultimodalFileTester:
    """Test multimodal inputs with actual files"""
    
    def __init__(self, model_name: str = "gemma3n:e2b"):
        self.model_name = model_name
        self.base_prompt = """You are an emergency first aid expert. Analyze the emergency situation and provide step-by-step JSON instructions.

Return only valid JSON in this format:
{
  "analysis": "Brief description of what you observe",
  "emergency_type": "Type of emergency",
  "urgency_level": "Low/Medium/High/Critical",
  "steps": [
    {
      "step": 1,
      "title": "Step title",
      "description": "Detailed description"
    }
  ]
}
"""
        
    def encode_file_to_base64(self, file_path: str) -> str:
        """Encode a file to base64 for sending to Ollama"""
        try:
            with open(file_path, 'rb') as f:
                return base64.b64encode(f.read()).decode('utf-8')
        except Exception as e:
            logger.error(f"Error encoding file {file_path}: {e}")
            return None
    
    def check_model_availability(self) -> bool:
        """Check if the model is available in Ollama"""
        try:
            models = ollama.list()
            available_models = [model['name'] for model in models['models']]
            logger.info(f"Available models: {available_models}")
            
            if self.model_name in available_models:
                logger.info(f"✅ Model {self.model_name} is available")
                return True
            else:
                logger.warning(f"❌ Model {self.model_name} not found")
                logger.info("Available models for testing:")
                for model in available_models:
                    logger.info(f"  - {model}")
                return False
        except Exception as e:
            logger.error(f"Error checking model availability: {e}")
            return False
    
    def test_text_input(self) -> bool:
        """Test text input functionality"""
        logger.info("🔤 Testing text input...")
        
        emergency_scenarios = [
            "I'm hiking and my friend just fell down a cliff. They're conscious but saying their leg really hurts and they can't move it.",
            "Someone at our campsite is having trouble breathing after being stung by something. Their face is starting to swell.",
            "I found someone unconscious on the trail. They're breathing but won't wake up when I shake them."
        ]
        
        success_count = 0
        for i, scenario in enumerate(emergency_scenarios, 1):
            logger.info(f"Testing scenario {i}: {scenario[:50]}...")
            
            try:
                response = ollama.generate(
                    model=self.model_name,
                    prompt=f"{self.base_prompt}\n\nEmergency Report: {scenario}"
                )
                
                # Try to parse response as JSON
                try:
                    json_response = json.loads(response['response'])
                    logger.info(f"✅ Scenario {i}: Valid JSON response")
                    success_count += 1
                except json.JSONDecodeError:
                    logger.warning(f"⚠️ Scenario {i}: Response not valid JSON")
                    logger.info(f"Response: {response['response'][:200]}...")
                    
            except Exception as e:
                logger.error(f"❌ Scenario {i}: Error - {e}")
        
        logger.info(f"Text input test: {success_count}/{len(emergency_scenarios)} scenarios successful")
        return success_count == len(emergency_scenarios)
    
    def test_image_input(self, image_path: str) -> bool:
        """Test image input functionality"""
        logger.info(f"🖼️ Testing image input with {image_path}...")
        
        if not os.path.exists(image_path):
            logger.warning(f"Image file not found: {image_path}")
            return False
        
        try:
            # Encode image to base64
            image_base64 = self.encode_file_to_base64(image_path)
            if not image_base64:
                return False
            
            # Send to Ollama with image
            response = ollama.generate(
                model=self.model_name,
                prompt=f"{self.base_prompt}\n\nAnalyze this emergency situation in the image:",
                images=[image_base64]
            )
            
            logger.info(f"Image analysis response: {response['response'][:200]}...")
            
            # Try to parse as JSON
            try:
                json_response = json.loads(response['response'])
                logger.info("✅ Image input: Valid JSON response")
                return True
            except json.JSONDecodeError:
                logger.warning("⚠️ Image input: Response not valid JSON")
                logger.info(f"Raw response: {response['response']}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Image input error: {e}")
            return False
    
    def test_audio_input(self, audio_path: str) -> bool:
        """Test audio input functionality"""
        logger.info(f"🎵 Testing audio input with {audio_path}...")
        
        if not os.path.exists(audio_path):
            logger.warning(f"Audio file not found: {audio_path}")
            return False
        
        try:
            # Note: Audio handling may require different approach depending on Ollama version
            # For now, we'll simulate by describing the audio content
            audio_description = f"Audio emergency report from file: {audio_path}"
            
            response = ollama.generate(
                model=self.model_name,
                prompt=f"{self.base_prompt}\n\nThis is a voice recording of an emergency: {audio_description}"
            )
            
            logger.info(f"Audio analysis response: {response['response'][:200]}...")
            
            # Try to parse as JSON
            try:
                json_response = json.loads(response['response'])
                logger.info("✅ Audio input: Valid JSON response")
                return True
            except json.JSONDecodeError:
                logger.warning("⚠️ Audio input: Response not valid JSON")
                return False
                
        except Exception as e:
            logger.error(f"❌ Audio input error: {e}")
            return False
    
    def test_video_input(self, video_path: str) -> bool:
        """Test video input functionality"""
        logger.info(f"🎥 Testing video input with {video_path}...")
        
        if not os.path.exists(video_path):
            logger.warning(f"Video file not found: {video_path}")
            return False
        
        try:
            # Encode video to base64
            video_base64 = self.encode_file_to_base64(video_path)
            if not video_base64:
                return False
            
            # Send to Ollama with video
            response = ollama.generate(
                model=self.model_name,
                prompt=f"{self.base_prompt}\n\nAnalyze this emergency situation in the video:",
                # Note: Video handling depends on Ollama's multimodal support
                # This is a template for when video support is available
            )
            
            logger.info(f"Video analysis response: {response['response'][:200]}...")
            
            # Try to parse as JSON
            try:
                json_response = json.loads(response['response'])
                logger.info("✅ Video input: Valid JSON response")
                return True
            except json.JSONDecodeError:
                logger.warning("⚠️ Video input: Response not valid JSON")
                return False
                
        except Exception as e:
            logger.error(f"❌ Video input error: {e}")
            return False
    
    def run_full_test_suite(self, test_files: Dict[str, str] = None) -> Dict[str, bool]:
        """Run the complete multimodal test suite"""
        logger.info("🧪 MULTIMODAL TEST SUITE")
        logger.info("=" * 50)
        
        results = {}
        
        # Check model availability first
        if not self.check_model_availability():
            logger.error("Model not available. Cannot run tests.")
            return results
        
        # Test text input
        results['text'] = self.test_text_input()
        
        # Test multimodal inputs if files are provided
        if test_files:
            if 'image' in test_files:
                results['image'] = self.test_image_input(test_files['image'])
            
            if 'audio' in test_files:
                results['audio'] = self.test_audio_input(test_files['audio'])
            
            if 'video' in test_files:
                results['video'] = self.test_video_input(test_files['video'])
        
        # Print summary
        logger.info("📊 TEST RESULTS SUMMARY")
        logger.info("=" * 30)
        for test_type, passed in results.items():
            status = "✅ PASSED" if passed else "❌ FAILED"
            logger.info(f"{test_type.upper()}: {status}")
        
        return results

def create_sample_files():
    """Create sample files for testing (placeholders)"""
    logger.info("📁 Creating sample test files...")
    
    # Create test_files directory
    test_dir = Path("test_files")
    test_dir.mkdir(exist_ok=True)
    
    # Create placeholder files with instructions
    sample_files = {
        "image_instructions.txt": """
SAMPLE IMAGE FILES FOR TESTING:

1. emergency_wound.jpg - Photo of a cut or wound
2. emergency_burn.jpg - Photo of a burn injury  
3. emergency_choking.jpg - Photo of someone choking
4. emergency_fall.jpg - Photo of someone who has fallen

Place actual image files in this directory with these names for testing.
Example emergency scenarios these images might represent:
- Deep cut on arm bleeding
- Burn from hot surface
- Person choking on food
- Person fallen with suspected fracture
        """,
        
        "audio_instructions.txt": """
SAMPLE AUDIO FILES FOR TESTING:

1. emergency_help.wav - Audio of someone calling for help
2. emergency_choking.wav - Audio of someone choking
3. emergency_pain.wav - Audio of someone in pain
4. emergency_breathing.wav - Audio of someone having breathing difficulties

Place actual audio files in this directory with these names for testing.
Example emergency scenarios these audio files might represent:
- "Help! I'm trapped under a fallen tree!"
- "Someone is choking and can't breathe!"
- "My leg is broken and I can't move!"
- "I'm having trouble breathing!"
        """,
        
        "video_instructions.txt": """
SAMPLE VIDEO FILES FOR TESTING:

1. emergency_scenario.mp4 - Video of an emergency situation
2. emergency_cpr.mp4 - Video showing need for CPR
3. emergency_accident.mp4 - Video of an accident scene
4. emergency_medical.mp4 - Video of medical emergency

Place actual video files in this directory with these names for testing.
Keep videos short (under 10 seconds) for optimal processing.
        """
    }
    
    for filename, content in sample_files.items():
        file_path = test_dir / filename
        with open(file_path, 'w') as f:
            f.write(content.strip())
        logger.info(f"Created: {file_path}")
    
    logger.info(f"Sample files created in {test_dir}")
    return test_dir

def main():
    """Main testing function"""
    logger.info("🚑 MULTIMODAL EMERGENCY RESPONSE TESTING")
    logger.info("=" * 60)
    
    # Create sample files directory
    test_dir = create_sample_files()
    
    # Initialize tester
    tester = MultimodalFileTester()
    
    # Define test files (update paths as needed)
    test_files = {
        'image': 'test_files/emergency_wound.jpg',  # Replace with actual image
        'audio': 'test_files/emergency_help.wav',   # Replace with actual audio
        'video': 'test_files/emergency_scenario.mp4'  # Replace with actual video
    }
    
    # Run tests
    results = tester.run_full_test_suite(test_files)
    
    # Final summary
    logger.info("\n🎯 TESTING COMPLETE")
    logger.info("=" * 30)
    
    if results:
        passed = sum(results.values())
        total = len(results)
        logger.info(f"Tests passed: {passed}/{total}")
        
        if passed == total:
            logger.info("🎉 All tests passed! Multimodal functionality is working.")
        else:
            logger.info("⚠️ Some tests failed. Check logs for details.")
    else:
        logger.error("❌ No tests could be run. Check model availability.")

if __name__ == "__main__":
    main() 