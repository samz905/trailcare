import json
import random

def add_environmental_emergencies():
    """Add environmental and exposure-related emergencies"""
    return {
        "Heat Stroke": {
            "patterns": ["How do you treat Heat Stroke?", "overheating", "heat emergency", "hot weather illness", "body temperature high"],
            "steps": [
                {"step": 1, "title": "Move to Cool Area", "description": "Immediately move the person to a cool, shaded area or air-conditioned environment. Remove excess clothing and any tight garments."},
                {"step": 2, "title": "Cool the Body Rapidly", "description": "Apply cool water to the skin and fan the person. Focus on neck, armpits, and groin areas. Use ice packs wrapped in cloth on these areas if available."},
                {"step": 3, "title": "Monitor Temperature", "description": "Check body temperature frequently. Continue cooling until body temperature drops to 102°F (39°C) or below, then stop to prevent overcooling."},
                {"step": 4, "title": "Give Fluids if Conscious", "description": "If the person is conscious and able to swallow, give small sips of cool water. Do not give fluids if they are vomiting or unconscious."},
                {"step": 5, "title": "Seek Emergency Care", "description": "Call 911 immediately. Heat stroke is life-threatening and requires immediate medical attention even if the person appears to recover."}
            ]
        },
        
        "Heat Exhaustion": {
            "patterns": ["How do you treat Heat Exhaustion?", "heat fatigue", "overheated", "heat cramps", "dehydration from heat"],
            "steps": [
                {"step": 1, "title": "Move to Cool Environment", "description": "Move the person to a cool, shaded area immediately. Have them lie down and elevate their feet slightly."},
                {"step": 2, "title": "Remove Excess Clothing", "description": "Loosen or remove tight clothing. Apply cool, wet cloths to the skin or fan the person while misting with water."},
                {"step": 3, "title": "Provide Cool Fluids", "description": "Give small sips of cool water or sports drinks if the person is conscious and not nauseous. Avoid alcohol or caffeine."},
                {"step": 4, "title": "Monitor Symptoms", "description": "Watch for improvement in 15-20 minutes. If symptoms worsen or include confusion, hot dry skin, or high fever, treat as heat stroke."},
                {"step": 5, "title": "Seek Medical Care", "description": "If symptoms don't improve within 30 minutes, vomiting occurs, or the person becomes unconscious, call 911 immediately."}
            ]
        },
        
        "Frost Bite": {
            "patterns": ["How do you treat Frost bite?", "frozen skin", "cold injury", "frostbitten fingers", "ice burn"],
            "steps": [
                {"step": 1, "title": "Move to Warmth", "description": "Get the person to a warm, dry environment immediately. Remove any wet clothing and jewelry from the affected area before swelling occurs."},
                {"step": 2, "title": "Warm Gently", "description": "Soak the affected area in warm (not hot) water, 104-108°F for 15-30 minutes. The water should feel warm to unaffected skin."},
                {"step": 3, "title": "Protect the Area", "description": "After rewarming, gently dry the area and wrap with sterile gauze. Separate affected fingers and toes with gauze."},
                {"step": 4, "title": "Avoid Further Damage", "description": "Do not rub or massage the area. Avoid direct heat like heating pads or fires. Take over-the-counter pain medication as rewarming can be painful."},
                {"step": 5, "title": "Seek Medical Care", "description": "Get medical attention immediately, especially for deep frostbite. Watch for signs of infection and never refreeze thawed tissue."}
            ]
        },
        
        "Sun Burn": {
            "patterns": ["How do you treat Sun Burn?", "sunburned skin", "too much sun", "burned by sun", "skin burning"],
            "steps": [
                {"step": 1, "title": "Cool the Skin", "description": "Apply cool, wet compresses to the burned area for 15-20 minutes several times a day. Take cool baths or showers to help reduce heat."},
                {"step": 2, "title": "Hydrate Inside and Out", "description": "Drink plenty of water to prevent dehydration. While skin is damp, apply moisturizer with aloe vera or hydrocortisone cream."},
                {"step": 3, "title": "Avoid Further Sun", "description": "Stay out of the sun until the burn heals. If you must go outside, wear protective clothing and use broad-spectrum sunscreen."},
                {"step": 4, "title": "Treat Pain", "description": "Take ibuprofen or acetaminophen for pain and inflammation. Apply cold milk compresses - the proteins help soothe burned skin."},
                {"step": 5, "title": "Don't Pop Blisters", "description": "If blisters form, don't pop them. They protect the healing skin underneath. Seek medical care for severe burns with extensive blistering."}
            ]
        }
    }

def add_poisoning_emergencies():
    """Add poisoning and toxic emergencies"""
    return {
        "Poison": {
            "patterns": ["How do you treat Poison?", "poisoning", "toxic ingestion", "swallowed chemicals", "poisonous substance"],
            "steps": [
                {"step": 1, "title": "Call Poison Control", "description": "Immediately call Poison Control at 1-800-222-1222 or 911. Have the poison container available for identification."},
                {"step": 2, "title": "Assess the Person", "description": "Check if the person is conscious and breathing. If unconscious or not breathing, call 911 immediately and begin CPR if trained."},
                {"step": 3, "title": "Follow Expert Instructions", "description": "Follow the specific instructions given by Poison Control. Do not induce vomiting unless specifically told to do so."},
                {"step": 4, "title": "Provide Information", "description": "Give Poison Control details: what was ingested, how much, when it happened, and the person's age, weight, and current symptoms."},
                {"step": 5, "title": "Stay with the Person", "description": "Stay with the person and monitor their condition. Be prepared to provide updates to emergency services and follow additional instructions."}
            ]
        },
        
        "Chemical Burn": {
            "patterns": ["How do you treat a chemical burn?", "acid burn", "chemical on skin", "caustic burn", "chemical spill"],
            "steps": [
                {"step": 1, "title": "Remove from Chemical", "description": "Remove the person from the chemical source immediately. Remove contaminated clothing and jewelry carefully, cutting them off if necessary."},
                {"step": 2, "title": "Flush with Water", "description": "Rinse the affected area with large amounts of clean water for at least 20 minutes. Use a gentle stream to avoid further tissue damage."},
                {"step": 3, "title": "Remove Particles", "description": "While rinsing, gently remove any visible chemical particles with a soft cloth. Do not scrub or rub the area."},
                {"step": 4, "title": "Cover the Burn", "description": "After thorough rinsing, cover the area with a sterile gauze bandage or clean cloth. Do not apply any ointments or creams."},
                {"step": 5, "title": "Seek Emergency Care", "description": "Call 911 immediately. Chemical burns require professional medical treatment. If possible, bring the chemical container for identification."}
            ]
        }
    }

def add_bite_sting_emergencies():
    """Add bite and sting emergencies"""
    return {
        "Snake Bite": {
            "patterns": ["How do you treat a snake bite?", "venomous snake", "snake bit me", "snake attack", "poisonous snake"],
            "steps": [
                {"step": 1, "title": "Move to Safety", "description": "Move the person away from the snake immediately. Do not try to catch or kill the snake, but try to remember its appearance for medical personnel."},
                {"step": 2, "title": "Keep Calm and Still", "description": "Keep the person calm and as still as possible. Physical activity can increase the spread of venom through the bloodstream."},
                {"step": 3, "title": "Position and Remove Items", "description": "Position the bite below the level of the heart if possible. Remove jewelry and tight clothing near the bite site before swelling begins."},
                {"step": 4, "title": "Clean and Cover", "description": "Gently clean the bite area with soap and water. Cover with a clean, loose bandage. Do not use a tourniquet or apply ice."},
                {"step": 5, "title": "Get Emergency Help", "description": "Call 911 immediately and transport to the nearest hospital. Note the time of the bite and monitor for symptoms like nausea, difficulty breathing, or severe swelling."}
            ]
        },
        
        "Animal Bite": {
            "patterns": ["How do you treat an animal bite?", "dog bite", "cat bite", "monkey bite", "rabies risk"],
            "steps": [
                {"step": 1, "title": "Control Bleeding", "description": "Apply direct pressure with a clean cloth to control bleeding. Do not try to clean deep puncture wounds initially."},
                {"step": 2, "title": "Clean the Wound", "description": "For shallow wounds, wash gently with soap and warm water for 5 minutes. Rinse thoroughly and pat dry."},
                {"step": 3, "title": "Apply Antiseptic", "description": "Apply antibiotic ointment and cover with a sterile bandage. Change the dressing daily and keep the wound clean."},
                {"step": 4, "title": "Document the Incident", "description": "Note the time, animal type, and circumstances. Try to determine if the animal is vaccinated against rabies."},
                {"step": 5, "title": "Seek Medical Care", "description": "See a doctor within 24 hours, especially for deep bites, face/hand bites, or if rabies vaccination status is unknown. Tetanus shot may be needed."}
            ]
        },
        
        "Insect Bites": {
            "patterns": ["How do you treat Insect Bites?", "bee sting", "mosquito bite", "ant bite", "wasp sting", "bug bite"],
            "steps": [
                {"step": 1, "title": "Remove Stinger if Present", "description": "If a stinger is visible, remove it immediately by scraping it out with a credit card or fingernail. Do not use tweezers as this can squeeze more venom into the wound."},
                {"step": 2, "title": "Clean the Area", "description": "Wash the bite area with soap and water to prevent infection. Pat dry with a clean towel."},
                {"step": 3, "title": "Apply Cold Treatment", "description": "Apply ice wrapped in a cloth for 15-20 minutes to reduce swelling and pain. This also helps slow the spread of venom."},
                {"step": 4, "title": "Treat Symptoms", "description": "Apply calamine lotion or hydrocortisone cream to reduce itching. Take an antihistamine like Benadryl if there's significant swelling or itching."},
                {"step": 5, "title": "Monitor for Allergic Reaction", "description": "Watch for signs of severe allergic reaction: difficulty breathing, swelling of face or throat, rapid pulse, or dizziness. Call 911 if these occur."}
            ]
        }
    }

# Load existing data and add more emergency types
def extend_complete_dataset():
    """Extend the dataset with more emergency types"""
    
    # Load existing data
    existing_responses = {}
    
    # Add new emergency types
    all_responses = {}
    all_responses.update(add_environmental_emergencies())
    all_responses.update(add_poisoning_emergencies())
    all_responses.update(add_bite_sting_emergencies())
    
    # Create new training examples
    new_examples = []
    
    for emergency_type, data in all_responses.items():
        for pattern in data["patterns"]:
            example = {
                "input": pattern,
                "output": {
                    "steps": data["steps"]
                }
            }
            new_examples.append(example)
    
    # Load existing examples
    existing_examples = []
    with open('processed_data/complete_manual_dataset.jsonl', 'r') as f:
        for line in f:
            existing_examples.append(json.loads(line.strip()))
    
    # Combine all examples
    all_examples = existing_examples + new_examples
    
    # Shuffle and save
    random.seed(42)
    random.shuffle(all_examples)
    
    with open('processed_data/complete_manual_dataset.jsonl', 'w') as f:
        for example in all_examples:
            f.write(json.dumps(example) + '\n')
    
    print(f"✅ Added {len(new_examples)} new training examples")
    print(f"✅ Total examples: {len(all_examples)}")
    print(f"✅ New emergency types added: {len(all_responses)}")
    print("\nNew Emergency Types:")
    for i, emergency_type in enumerate(all_responses.keys(), 1):
        step_count = len(all_responses[emergency_type]["steps"])
        print(f"{i}. {emergency_type}: {step_count} steps")

if __name__ == "__main__":
    extend_complete_dataset() 