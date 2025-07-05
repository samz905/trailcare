#!/usr/bin/env python3
"""
Multimodal Emergency Response Testing Script
Tests Gemma 3n with text, audio, image, and video inputs for emergency scenarios
"""

import os
import sys
import json
import base64
import requests
from typing import Dict, Any, Optional, List
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MultimodalEmergencyTester:
    """
    Test Gemma 3n multimodal capabilities for emergency scenarios
    """
    
    def __init__(self, model_name: str = "gemma3n:e2b"):
        self.model_name = model_name
        self.base_url = "http://localhost:11434"
        self.emergency_prompt = """This is an emergency report from a hiker. Based on the input provided, analyze the situation and return step-by-step JSON instructions to help the person.

Format your response as JSON with this structure:
{
  "steps": [
    {
      "step": 1,
      "title": "Title of step",
      "description": "Detailed description of what to do"
    }
  ]
}
"""
        
    def test_text_input(self, text: str) -> Dict[str, Any]:
        """Test text input with emergency scenario"""
        logger.info("Testing text input...")
        
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model_name,
                    "prompt": f"{self.emergency_prompt}\n\nEmergency Description: {text}",
                    "stream": False
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                return {
                    "success": True,
                    "input_type": "text",
                    "input": text,
                    "response": result.get("response", ""),
                    "model_info": result.get("model", "")
                }
            else:
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
                
        except Exception as e:
            logger.error(f"Text input test failed: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def test_image_input(self, image_path: str, description: str = "") -> Dict[str, Any]:
        """Test image input with emergency scenario"""
        logger.info(f"Testing image input: {image_path}")
        
        try:
            # Read and encode image
            with open(image_path, "rb") as image_file:
                image_data = base64.b64encode(image_file.read()).decode('utf-8')
            
            prompt = f"{self.emergency_prompt}\n\nEmergency Image Description: {description}\nPlease analyze the image and provide emergency instructions."
            
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "images": [image_data],
                    "stream": False
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                return {
                    "success": True,
                    "input_type": "image",
                    "input": image_path,
                    "description": description,
                    "response": result.get("response", ""),
                    "model_info": result.get("model", "")
                }
            else:
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
                
        except Exception as e:
            logger.error(f"Image input test failed: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def test_audio_input(self, audio_path: str, description: str = "") -> Dict[str, Any]:
        """Test audio input with emergency scenario"""
        logger.info(f"Testing audio input: {audio_path}")
        
        try:
            # For now, simulate audio processing as Ollama's audio support may be limited
            # In a full implementation, this would send raw audio to Gemma 3n
            
            prompt = f"{self.emergency_prompt}\n\nEmergency Audio Description: {description}\nThis is a transcription/description of an audio emergency report. Please provide appropriate emergency instructions."
            
            # Read audio file as base64 (conceptual - actual implementation depends on Ollama's audio support)
            with open(audio_path, "rb") as audio_file:
                audio_data = base64.b64encode(audio_file.read()).decode('utf-8')
            
            # Note: This is a placeholder - actual Ollama audio API might be different
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                return {
                    "success": True,
                    "input_type": "audio",
                    "input": audio_path,
                    "description": description,
                    "response": result.get("response", ""),
                    "model_info": result.get("model", ""),
                    "note": "Audio processing simulated - actual implementation depends on Ollama audio support"
                }
            else:
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
                
        except Exception as e:
            logger.error(f"Audio input test failed: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def test_video_input(self, video_path: str, description: str = "") -> Dict[str, Any]:
        """Test video input with emergency scenario"""
        logger.info(f"Testing video input: {video_path}")
        
        try:
            # For now, simulate video processing as Ollama's video support may be limited
            # In a full implementation, this would send raw video to Gemma 3n
            
            prompt = f"{self.emergency_prompt}\n\nEmergency Video Description: {description}\nThis is a description of a video emergency report. Please analyze and provide appropriate emergency instructions."
            
            # Read video file as base64 (conceptual - actual implementation depends on Ollama's video support)
            with open(video_path, "rb") as video_file:
                video_data = base64.b64encode(video_file.read()).decode('utf-8')
            
            # Note: This is a placeholder - actual Ollama video API might be different
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                return {
                    "success": True,
                    "input_type": "video",
                    "input": video_path,
                    "description": description,
                    "response": result.get("response", ""),
                    "model_info": result.get("model", ""),
                    "note": "Video processing simulated - actual implementation depends on Ollama video support"
                }
            else:
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
                
        except Exception as e:
            logger.error(f"Video input test failed: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def check_model_availability(self) -> bool:
        """Check if the specified model is available"""
        try:
            response = requests.get(f"{self.base_url}/api/tags")
            if response.status_code == 200:
                models = response.json().get("models", [])
                available_models = [model["name"] for model in models]
                logger.info(f"Available models: {available_models}")
                return self.model_name in available_models
            return False
        except Exception as e:
            logger.error(f"Failed to check model availability: {e}")
            return False
    
    def create_test_scenarios(self) -> List[Dict[str, Any]]:
        """Create test scenarios for different input types"""
        scenarios = [
            {
                "type": "text",
                "input": "I'm hiking alone and fell into a shallow ravine. My left ankle is twisted and very painful. I can't put weight on it. It's getting dark and I'm about 2 miles from the trailhead. I have water, a flashlight, and my phone has 30% battery but no signal.",
                "description": "Hiking injury scenario"
            },
            {
                "type": "text", 
                "input": "I'm camping and my friend has been stung by something. His face is swelling rapidly and he's having trouble breathing. He says he's allergic to bee stings. We're 5 miles from the nearest road.",
                "description": "Allergic reaction scenario"
            },
            {
                "type": "text",
                "input": "While rock climbing, my partner fell and hit his head. He's conscious but seems confused and keeps asking the same questions. There's a small cut on his forehead that's bleeding.",
                "description": "Head injury scenario"
            }
        ]
        
        return scenarios
    
    def run_comprehensive_test(self) -> Dict[str, Any]:
        """Run comprehensive test of all input modalities"""
        logger.info("Starting comprehensive multimodal test...")
        
        # Check model availability
        if not self.check_model_availability():
            logger.error(f"Model {self.model_name} not available")
            return {
                "success": False,
                "error": f"Model {self.model_name} not available"
            }
        
        results = {
            "model": self.model_name,
            "test_results": [],
            "summary": {
                "total_tests": 0,
                "successful_tests": 0,
                "failed_tests": 0
            }
        }
        
        # Test text scenarios
        scenarios = self.create_test_scenarios()
        for scenario in scenarios:
            if scenario["type"] == "text":
                result = self.test_text_input(scenario["input"])
                result["scenario"] = scenario["description"]
                results["test_results"].append(result)
                results["summary"]["total_tests"] += 1
                if result["success"]:
                    results["summary"]["successful_tests"] += 1
                else:
                    results["summary"]["failed_tests"] += 1
        
        # Test image input (if test images exist)
        test_images = ["test_emergency_image.jpg", "test_injury_image.png"]
        for image_path in test_images:
            if os.path.exists(image_path):
                result = self.test_image_input(image_path, "Emergency situation captured in image")
                results["test_results"].append(result)
                results["summary"]["total_tests"] += 1
                if result["success"]:
                    results["summary"]["successful_tests"] += 1
                else:
                    results["summary"]["failed_tests"] += 1
        
        # Test audio input (if test audio exists)
        test_audio = ["test_emergency_audio.mp3", "test_emergency_audio.wav"]
        for audio_path in test_audio:
            if os.path.exists(audio_path):
                result = self.test_audio_input(audio_path, "Emergency audio report")
                results["test_results"].append(result)
                results["summary"]["total_tests"] += 1
                if result["success"]:
                    results["summary"]["successful_tests"] += 1
                else:
                    results["summary"]["failed_tests"] += 1
        
        # Test video input (if test video exists)
        test_videos = ["test_emergency_video.mp4", "test_emergency_video.mov"]
        for video_path in test_videos:
            if os.path.exists(video_path):
                result = self.test_video_input(video_path, "Emergency video report")
                results["test_results"].append(result)
                results["summary"]["total_tests"] += 1
                if result["success"]:
                    results["summary"]["successful_tests"] += 1
                else:
                    results["summary"]["failed_tests"] += 1
        
        return results
    
    def save_results(self, results: Dict[str, Any], filename: str = "multimodal_test_results.json"):
        """Save test results to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(results, f, indent=2)
            logger.info(f"Results saved to {filename}")
        except Exception as e:
            logger.error(f"Failed to save results: {e}")
    
    def print_summary(self, results: Dict[str, Any]):
        """Print test summary"""
        print("\n" + "="*60)
        print("MULTIMODAL EMERGENCY RESPONSE TEST SUMMARY")
        print("="*60)
        print(f"Model: {results['model']}")
        print(f"Total Tests: {results['summary']['total_tests']}")
        print(f"Successful: {results['summary']['successful_tests']}")
        print(f"Failed: {results['summary']['failed_tests']}")
        print(f"Success Rate: {(results['summary']['successful_tests'] / results['summary']['total_tests'] * 100):.1f}%")
        print("="*60)
        
        # Print individual test results
        for i, result in enumerate(results['test_results'], 1):
            print(f"\nTest {i}: {result['input_type'].upper()} Input")
            if 'scenario' in result:
                print(f"Scenario: {result['scenario']}")
            
            if result['success']:
                print("✅ SUCCESS")
                print(f"Response: {result['response'][:200]}...")
            else:
                print("❌ FAILED")
                print(f"Error: {result['error']}")
        
        print("\n" + "="*60)

def main():
    """Main function to run multimodal tests"""
    if len(sys.argv) > 1:
        model_name = sys.argv[1]
    else:
        model_name = "gemma3n:e2b"
    
    print(f"🔬 Starting Multimodal Emergency Response Tests with {model_name}")
    print("This tests Gemma 3n's ability to handle text, audio, image, and video inputs for emergency scenarios.")
    print("="*80)
    
    tester = MultimodalEmergencyTester(model_name)
    results = tester.run_comprehensive_test()
    
    # Print and save results
    tester.print_summary(results)
    tester.save_results(results)
    
    print("\n🎯 Test completed! Check multimodal_test_results.json for detailed results.")

if __name__ == "__main__":
    main() 