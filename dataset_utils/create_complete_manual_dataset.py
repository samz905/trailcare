import json
import random

def create_complete_emergency_dataset():
    """Create a comprehensive manual dataset with all 44 emergency types"""
    
    # Complete emergency dataset with manually written instructions
    emergency_responses = {
        "Cuts": {
            "patterns": ["What to do if Cuts?", "How to cure Cuts?", "Which medicine to apply for Cuts?", "what to apply on cuts?", "Cuts", "I cut myself", "bleeding cut"],
            "steps": [
                {"step": 1, "title": "Apply Direct Pressure", "description": "Use a clean cloth or sterile gauze to apply firm, direct pressure to the wound for 10-15 minutes to stop bleeding. Do not lift the cloth to check - maintain constant pressure."},
                {"step": 2, "title": "Clean the Wound", "description": "Once bleeding stops, rinse the cut gently with clean water. Remove any visible dirt or debris with clean tweezers sterilized with rubbing alcohol."},
                {"step": 3, "title": "Apply Antiseptic", "description": "Apply a thin layer of antibiotic ointment (like Neosporin) to prevent infection. If allergic to antibiotics, use petroleum jelly instead."},
                {"step": 4, "title": "Cover and Protect", "description": "Cover the wound with a sterile adhesive bandage or gauze. Change the dressing daily or when it becomes wet or dirty."},
                {"step": 5, "title": "Monitor for Infection", "description": "Watch for signs of infection: increased redness, swelling, warmth, pus, or red streaks. Seek medical attention if any of these occur."}
            ]
        },
        
        "Choking": {
            "patterns": ["How do you treat Choking?", "someone is choking", "can't breathe", "choking emergency", "blocked airway"],
            "steps": [
                {"step": 1, "title": "Assess the Situation", "description": "Check if the person can speak or cough. If they can make sounds, encourage them to keep coughing to try to dislodge the object. If they cannot speak or cough, proceed immediately to back blows."},
                {"step": 2, "title": "Perform Back Blows", "description": "Stand behind the person and lean them forward. Using the heel of your hand, give 5 sharp blows between the shoulder blades. Check if the object is dislodged after each blow."},
                {"step": 3, "title": "Give Abdominal Thrusts", "description": "If back blows don't work, stand behind the person and wrap your arms around their waist. Make a fist and place it just above the navel. Grasp the fist with your other hand and give 5 quick upward thrusts."},
                {"step": 4, "title": "Alternate Techniques", "description": "Continue alternating between 5 back blows and 5 abdominal thrusts until the object is expelled or the person becomes unconscious."},
                {"step": 5, "title": "Call for Help", "description": "If the person becomes unconscious, call 911 immediately and begin CPR. If alone with a conscious person, call 911 after trying the above techniques for 1 minute."}
            ]
        },
        
        "CPR": {
            "patterns": ["How to give CPR?", "cardiac arrest", "no pulse", "not breathing", "CPR emergency", "heart stopped"],
            "steps": [
                {"step": 1, "title": "Check Responsiveness", "description": "Tap the person's shoulders firmly and shout 'Are you okay?' If no response, call 911 immediately or have someone else call while you begin CPR."},
                {"step": 2, "title": "Position the Person", "description": "Place the person on their back on a firm, flat surface. Tilt their head back slightly by lifting the chin and tilting the forehead."},
                {"step": 3, "title": "Hand Placement", "description": "Place the heel of one hand on the center of the chest between the nipples. Place your other hand on top, interlacing your fingers. Keep your arms straight and shoulders directly over your hands."},
                {"step": 4, "title": "Perform Chest Compressions", "description": "Push hard and fast, compressing the chest at least 2 inches deep. Allow complete chest recoil between compressions. Compress at a rate of 100-120 compressions per minute."},
                {"step": 5, "title": "Continue Until Help Arrives", "description": "Perform continuous chest compressions without stopping until emergency medical services arrive or the person regains consciousness. Switch with another person every 2 minutes if possible to avoid fatigue."}
            ]
        },
        
        "Fracture": {
            "patterns": ["How do you treat a Fracture?", "broken bone", "fractured arm", "fractured leg", "bone sticking out"],
            "steps": [
                {"step": 1, "title": "Don't Move the Person", "description": "Keep the person still and calm. Do not try to move them unless they are in immediate danger. Movement can worsen the injury."},
                {"step": 2, "title": "Control Bleeding", "description": "If there is bleeding, apply gentle pressure around the wound with a clean cloth. Do not apply pressure directly over the fracture site or protruding bone."},
                {"step": 3, "title": "Immobilize the Area", "description": "Support the fractured area above and below the injury. Use a splint (rigid board, magazine, or cardboard) padded with cloth. Secure with bandages or tape, but not too tightly."},
                {"step": 4, "title": "Apply Ice Carefully", "description": "Apply ice wrapped in a cloth for 15-20 minutes to reduce swelling and pain. Never apply ice directly to skin or over an open fracture."},
                {"step": 5, "title": "Monitor and Seek Help", "description": "Watch for signs of shock (pale, clammy skin, rapid breathing). Keep the person warm and call 911 immediately for transportation to hospital."}
            ]
        },
        
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
        
        "Drowning": {
            "patterns": ["What to do if someone is Drowning?", "person drowning", "water rescue", "underwater too long", "not breathing after water"],
            "steps": [
                {"step": 1, "title": "Ensure Safety", "description": "Do not enter the water unless you are a trained lifeguard. Instead, throw a flotation device or extend a pole/rope to the person. Call 911 immediately."},
                {"step": 2, "title": "Remove from Water", "description": "Once the person is safely out of water, place them on their back on a firm surface. Be careful with head and neck - suspect spinal injury if they dove or fell."},
                {"step": 3, "title": "Check Breathing", "description": "Check for breathing by watching the chest rise and fall for 10 seconds. If not breathing normally, begin rescue breathing immediately."},
                {"step": 4, "title": "Begin CPR if Needed", "description": "If no pulse and not breathing, begin CPR immediately. For drowning victims, start with 2 rescue breaths before chest compressions."},
                {"step": 5, "title": "Monitor and Treat", "description": "Even if the person recovers, they need medical evaluation. Watch for secondary drowning symptoms like coughing, chest pain, or difficulty breathing hours later."}
            ]
        },
        
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
        
        "Nose Bleed": {
            "patterns": ["How do you treat a bleeding nose?", "nosebleed", "blood from nose", "nasal bleeding", "nose bleeding"],
            "steps": [
                {"step": 1, "title": "Sit and Lean Forward", "description": "Have the person sit upright and lean slightly forward. This prevents blood from flowing back into the throat, which can cause nausea or vomiting."},
                {"step": 2, "title": "Pinch the Nostrils", "description": "Using thumb and index finger, pinch the soft part of the nostrils together firmly. Hold for 10-15 minutes without releasing to check."},
                {"step": 3, "title": "Apply Ice", "description": "Apply ice wrapped in a thin cloth to the bridge of the nose and cheeks. This helps constrict blood vessels and reduce bleeding."},
                {"step": 4, "title": "Breathe Through Mouth", "description": "Have the person breathe through their mouth while maintaining pressure on the nose. Avoid talking, swallowing, or spitting during this time."},
                {"step": 5, "title": "Check and Seek Help", "description": "After 15 minutes, gently release pressure. If bleeding continues, repeat for another 15 minutes. If bleeding doesn't stop after 30 minutes, seek medical attention."}
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
        },
        
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
        
        "Seizure": {
            "patterns": ["How do you treat a seizure?", "convulsions", "epileptic fit", "person shaking", "seizure emergency"],
            "steps": [
                {"step": 1, "title": "Keep the Person Safe", "description": "Clear the area of any dangerous objects. Do not restrain the person or put anything in their mouth. Stay calm and time the seizure."},
                {"step": 2, "title": "Cushion the Head", "description": "Place something soft under their head if possible, like a folded jacket or pillow. Turn them on their side to help keep the airway clear."},
                {"step": 3, "title": "Do Not Interfere", "description": "Do not try to stop the seizure or hold the person down. Do not put anything in their mouth - they cannot swallow their tongue."},
                {"step": 4, "title": "Monitor Duration", "description": "Time the seizure. Most seizures last 1-3 minutes. If it lasts longer than 5 minutes, call 911 immediately."},
                {"step": 5, "title": "Care After Seizure", "description": "After the seizure stops, help the person sit up slowly. They may be confused or tired. Stay with them until they are fully alert or emergency help arrives."}
            ]
        },
        
        "Head Injury": {
            "patterns": ["How do you treat a head injury?", "head trauma", "concussion", "head wound", "skull injury"],
            "steps": [
                {"step": 1, "title": "Keep Person Still", "description": "Keep the person lying down with head and shoulders slightly elevated. Do not move them unless absolutely necessary due to possible neck injury."},
                {"step": 2, "title": "Control Bleeding", "description": "If there's bleeding, apply gentle pressure with a clean cloth around the wound, not directly on it if you suspect a skull fracture."},
                {"step": 3, "title": "Monitor Consciousness", "description": "Check the person's level of consciousness every few minutes. Ask simple questions like their name, date, and what happened."},
                {"step": 4, "title": "Watch for Symptoms", "description": "Monitor for signs of serious injury: vomiting, confusion, seizures, unequal pupil size, or loss of consciousness."},
                {"step": 5, "title": "Seek Emergency Care", "description": "Call 911 immediately for any head injury. Even minor head injuries can be serious and require medical evaluation."}
            ]
        },
        
        "Fainting": {
            "patterns": ["How do you treat Fainting?", "passed out", "unconscious", "fainted", "lost consciousness"],
            "steps": [
                {"step": 1, "title": "Check Responsiveness", "description": "Check if the person is responsive by gently tapping their shoulders and calling their name. Look for normal breathing."},
                {"step": 2, "title": "Position Properly", "description": "If breathing normally, place the person on their back and elevate their legs 8-12 inches above the heart to improve blood flow to the brain."},
                {"step": 3, "title": "Loosen Clothing", "description": "Loosen any tight clothing around the neck, chest, and waist. Ensure good air circulation around the person."},
                {"step": 4, "title": "Check for Injuries", "description": "Look for any injuries that may have occurred during the fall. If you suspect head, neck, or back injury, do not move the person."},
                {"step": 5, "title": "Monitor and Seek Help", "description": "If the person doesn't regain consciousness within 1-2 minutes, call 911. When they wake up, have them sit up slowly and rest before standing."}
            ]
        },
        
        "Eye Injury": {
            "patterns": ["How do you treat an eye injury?", "something in eye", "eye pain", "eye trauma", "damaged eye"],
            "steps": [
                {"step": 1, "title": "Do Not Rub", "description": "Tell the person not to rub or press on the injured eye. This can cause further damage, especially if there's a foreign object."},
                {"step": 2, "title": "Assess the Injury", "description": "Determine the type of injury: foreign object, chemical exposure, or trauma. Different injuries require different treatments."},
                {"step": 3, "title": "Flush if Chemical", "description": "If chemical exposure, immediately flush the eye with clean water for at least 15 minutes. Hold the eyelid open and rinse from inner to outer corner."},
                {"step": 4, "title": "Cover if Trauma", "description": "For trauma or embedded objects, cover both eyes with sterile gauze (this prevents the injured eye from moving). Do not remove embedded objects."},
                {"step": 5, "title": "Seek Medical Care", "description": "Get immediate medical attention for any eye injury. Eye injuries can cause permanent vision loss if not treated promptly and properly."}
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
        },
        
        "Pulled Muscle": {
            "patterns": ["How do you treat a Pulled Muscle?", "muscle strain", "torn muscle", "muscle injury", "muscle pain"],
            "steps": [
                {"step": 1, "title": "Rest the Muscle", "description": "Stop the activity that caused the injury immediately. Avoid using the affected muscle for 24-48 hours or until pain subsides."},
                {"step": 2, "title": "Apply Ice", "description": "Apply ice wrapped in a towel for 15-20 minutes every 2-3 hours for the first 24-48 hours to reduce swelling and pain."},
                {"step": 3, "title": "Compress the Area", "description": "Use an elastic bandage to wrap the injured area, but not too tightly. This helps reduce swelling and provides support."},
                {"step": 4, "title": "Elevate if Possible", "description": "If the injured muscle is in a limb, elevate it above heart level when resting to help reduce swelling."},
                {"step": 5, "title": "Gradual Return", "description": "After 48 hours, gradually return to activity. Switch to heat therapy and gentle stretching. Seek medical care if pain persists or worsens."}
            ]
        },
        
        "Vertigo": {
            "patterns": ["How do you treat Vertigo?", "dizziness", "spinning sensation", "balance problems", "dizzy spells"],
            "steps": [
                {"step": 1, "title": "Sit Down Immediately", "description": "Have the person sit down immediately to prevent falling. If lying down, keep the head slightly elevated with pillows."},
                {"step": 2, "title": "Stay Still", "description": "Avoid sudden movements. Keep the head as still as possible until the spinning sensation passes."},
                {"step": 3, "title": "Fix Your Gaze", "description": "Focus on a stationary object to help reduce the spinning sensation. Close eyes if this helps reduce symptoms."},
                {"step": 4, "title": "Hydrate", "description": "Sip water slowly if able. Dehydration can worsen vertigo symptoms."},
                {"step": 5, "title": "Seek Medical Care", "description": "If vertigo is severe, persistent, or accompanied by hearing loss, headache, or neurological symptoms, seek medical attention immediately."}
            ]
        },
        
        "Broken Teeth": {
            "patterns": ["How do you treat broken teeth?", "tooth knocked out", "dental trauma", "chipped tooth", "dental emergency"],
            "steps": [
                {"step": 1, "title": "Find the Tooth", "description": "If a tooth is knocked out, find it immediately. Handle it by the crown (white part) only, never touch the root."},
                {"step": 2, "title": "Rinse Gently", "description": "Rinse the tooth gently with milk or clean water. Do not scrub or remove any tissue fragments attached to the root."},
                {"step": 3, "title": "Keep Moist", "description": "Try to place the tooth back in its socket if possible. If not, keep it moist in milk, saline solution, or the person's saliva."},
                {"step": 4, "title": "Control Bleeding", "description": "Control bleeding by having the person bite down on a clean cloth or gauze. Apply cold compress to reduce swelling."},
                {"step": 5, "title": "Seek Dental Care", "description": "Get to a dentist immediately, ideally within 30 minutes. Time is critical for successfully reimplanting a knocked-out tooth."}
            ]
        }
    }
    
    # Create training examples
    training_examples = []
    
    for emergency_type, data in emergency_responses.items():
        for pattern in data["patterns"]:
            example = {
                "input": pattern,
                "output": {
                    "steps": data["steps"]
                }
            }
            training_examples.append(example)
    
    # Shuffle the examples
    random.seed(42)
    random.shuffle(training_examples)
    
    # Save to JSONL file
    with open('processed_data/complete_manual_dataset.jsonl', 'w') as f:
        for example in training_examples:
            f.write(json.dumps(example) + '\n')
    
    print(f"Created {len(training_examples)} training examples for {len(emergency_responses)} emergency types")
    
    # Generate summary
    print("\nEmergency Types Covered:")
    for i, emergency_type in enumerate(emergency_responses.keys(), 1):
        step_count = len(emergency_responses[emergency_type]["steps"])
        pattern_count = len(emergency_responses[emergency_type]["patterns"])
        print(f"{i:2d}. {emergency_type}: {step_count} steps, {pattern_count} patterns")

if __name__ == "__main__":
    create_complete_emergency_dataset() 