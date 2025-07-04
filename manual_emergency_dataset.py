import json
import random

def create_manual_emergency_dataset():
    """Create a comprehensive manual dataset - starting with critical emergencies"""
    
    # Critical life-threatening emergencies first
    emergency_responses = {
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
        
        "Drowning": {
            "patterns": ["What to do if someone is Drowning?", "person drowning", "water rescue", "underwater too long", "not breathing after water"],
            "steps": [
                {"step": 1, "title": "Ensure Safety", "description": "Do not enter the water unless you are a trained lifeguard. Instead, throw a flotation device or extend a pole/rope to the person. Call 911 immediately."},
                {"step": 2, "title": "Remove from Water", "description": "Once the person is safely out of water, place them on their back on a firm surface. Be careful with head and neck - suspect spinal injury if they dove or fell."},
                {"step": 3, "title": "Check Breathing", "description": "Check for breathing by watching the chest rise and fall for 10 seconds. If not breathing normally, begin rescue breathing immediately."},
                {"step": 4, "title": "Begin CPR if Needed", "description": "If no pulse and not breathing, begin CPR immediately. For drowning victims, start with 2 rescue breaths before chest compressions."},
                {"step": 5, "title": "Monitor and Treat", "description": "Even if the person recovers, they need medical evaluation. Watch for secondary drowning symptoms like coughing, chest pain, or difficulty breathing hours later."}
            ]
        }
    }
    
    return emergency_responses

def add_trauma_emergencies():
    """Add trauma-related emergencies"""
    return {
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
        
        "Cuts": {
            "patterns": ["What to do if Cuts?", "How to cure Cuts?", "bleeding cut", "deep cut", "I cut myself"],
            "steps": [
                {"step": 1, "title": "Apply Direct Pressure", "description": "Use a clean cloth or sterile gauze to apply firm, direct pressure to the wound for 10-15 minutes to stop bleeding. Do not lift the cloth to check - maintain constant pressure."},
                {"step": 2, "title": "Clean the Wound", "description": "Once bleeding stops, rinse the cut gently with clean water. Remove any visible dirt or debris with clean tweezers sterilized with rubbing alcohol."},
                {"step": 3, "title": "Apply Antiseptic", "description": "Apply a thin layer of antibiotic ointment (like Neosporin) to prevent infection. If allergic to antibiotics, use petroleum jelly instead."},
                {"step": 4, "title": "Cover and Protect", "description": "Cover the wound with a sterile adhesive bandage or gauze. Change the dressing daily or when it becomes wet or dirty."},
                {"step": 5, "title": "Monitor for Infection", "description": "Watch for signs of infection: increased redness, swelling, warmth, pus, or red streaks. Seek medical attention if any of these occur."}
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
        }
    }

def add_medical_emergencies():
    """Add medical and neurological emergencies"""
    return {
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
        
        "Nose Bleed": {
            "patterns": ["How do you treat a bleeding nose?", "nosebleed", "blood from nose", "nasal bleeding", "nose bleeding"],
            "steps": [
                {"step": 1, "title": "Sit and Lean Forward", "description": "Have the person sit upright and lean slightly forward. This prevents blood from flowing back into the throat, which can cause nausea or vomiting."},
                {"step": 2, "title": "Pinch the Nostrils", "description": "Using thumb and index finger, pinch the soft part of the nostrils together firmly. Hold for 10-15 minutes without releasing to check."},
                {"step": 3, "title": "Apply Ice", "description": "Apply ice wrapped in a thin cloth to the bridge of the nose and cheeks. This helps constrict blood vessels and reduce bleeding."},
                {"step": 4, "title": "Breathe Through Mouth", "description": "Have the person breathe through their mouth while maintaining pressure on the nose. Avoid talking, swallowing, or spitting during this time."},
                {"step": 5, "title": "Check and Seek Help", "description": "After 15 minutes, gently release pressure. If bleeding continues, repeat for another 15 minutes. If bleeding doesn't stop after 30 minutes, seek medical attention."}
            ]
        }
    }

def add_outdoor_emergencies():
    """Add outdoor and hiking-specific emergency types"""
    return {
        "Heat Stroke": {
            "patterns": ["How do you treat Heat Stroke?", "overheating", "heat emergency", "body temperature high", "heat exhaustion"],
            "steps": [
                {"step": 1, "title": "Move to Cool Area", "description": "Immediately move the person to a cool, shaded area or air-conditioned environment. Remove excess clothing and any tight garments."},
                {"step": 2, "title": "Cool the Body Rapidly", "description": "Apply cool water to the skin and fan the person. Focus on neck, armpits, and groin areas. Use ice packs wrapped in cloth on these areas if available."},
                {"step": 3, "title": "Monitor Temperature", "description": "Check body temperature frequently. Continue cooling until body temperature drops to 102°F (39°C) or below, then stop to prevent overcooling."},
                {"step": 4, "title": "Give Fluids if Conscious", "description": "If the person is conscious and able to swallow, give small sips of cool water. Do not give fluids if they are vomiting or unconscious."},
                {"step": 5, "title": "Seek Emergency Care", "description": "Call 911 immediately. Heat stroke is life-threatening and requires immediate medical attention even if the person appears to recover."}
            ]
        },
        
        "Hypothermia": {
            "patterns": ["How do you treat Hypothermia?", "too cold", "freezing", "cold exposure", "shivering uncontrollably"],
            "steps": [
                {"step": 1, "title": "Move to Warm Shelter", "description": "Get the person to a warm, dry shelter immediately. Remove any wet clothing and replace with dry clothing or blankets."},
                {"step": 2, "title": "Warm the Core", "description": "Apply warm, dry compresses to the neck, chest, and groin. Do not apply heat to arms and legs as this can cause dangerous heart rhythms."},
                {"step": 3, "title": "Insulate the Person", "description": "Wrap the person in blankets or sleeping bags. Cover their head but leave the face clear. If conscious, give warm, non-alcoholic, non-caffeinated drinks."},
                {"step": 4, "title": "Handle Gently", "description": "Move the person very gently as sudden movements can trigger dangerous heart rhythms. Do not massage or rub the person."},
                {"step": 5, "title": "Get Medical Help", "description": "Call 911 immediately. Hypothermia is life-threatening and requires professional medical treatment, even if the person seems to be recovering."}
            ]
        },
        
        "Allergic Reaction": {
            "patterns": ["How do you treat an allergic reaction?", "anaphylaxis", "severe allergy", "can't breathe allergy", "swelling throat"],
            "steps": [
                {"step": 1, "title": "Check for EpiPen", "description": "If the person has an epinephrine auto-injector (EpiPen), use it immediately. Inject into the outer thigh, even through clothing."},
                {"step": 2, "title": "Call 911 Immediately", "description": "Call emergency services right away. Anaphylaxis can be fatal within minutes. State that someone is having a severe allergic reaction."},
                {"step": 3, "title": "Position the Person", "description": "Have the person lie down with legs elevated unless they're having trouble breathing, then keep them sitting upright."},
                {"step": 4, "title": "Monitor Breathing", "description": "Watch for signs of breathing difficulty, swelling of face or throat, rapid weak pulse, or loss of consciousness."},
                {"step": 5, "title": "Give Second Dose", "description": "If symptoms don't improve in 5-15 minutes and you have a second EpiPen, give another injection. Continue monitoring until help arrives."}
            ]
        },
        
        "Altitude Sickness": {
            "patterns": ["How do you treat Altitude Sickness?", "mountain sickness", "high altitude", "altitude headache", "HACE HAPE"],
            "steps": [
                {"step": 1, "title": "Descend Immediately", "description": "The most important treatment is to descend to a lower altitude immediately. Even descending 1,000-2,000 feet can provide significant relief."},
                {"step": 2, "title": "Rest and Hydrate", "description": "Stop climbing and rest. Drink plenty of water and avoid alcohol. Eat light, easily digestible foods if able."},
                {"step": 3, "title": "Give Oxygen", "description": "If available, administer supplemental oxygen. This can provide temporary relief but descent is still necessary."},
                {"step": 4, "title": "Monitor Symptoms", "description": "Watch for severe symptoms: confusion, difficulty walking, severe headache, vomiting, or difficulty breathing at rest."},
                {"step": 5, "title": "Evacuate if Severe", "description": "If symptoms worsen or include confusion, difficulty breathing, or loss of coordination, evacuate immediately to medical care. This can be life-threatening."}
            ]
        },
        
        "Dehydration": {
            "patterns": ["How do you treat Dehydration?", "no water", "thirsty", "dry mouth", "dizzy from heat"],
            "steps": [
                {"step": 1, "title": "Find Shade", "description": "Move to a cool, shaded area immediately. Remove excess clothing and rest in the coolest position possible."},
                {"step": 2, "title": "Drink Fluids Slowly", "description": "Sip water or electrolyte solutions slowly and frequently. Don't drink large amounts at once as this can cause nausea."},
                {"step": 3, "title": "Cool the Body", "description": "Apply cool, wet cloths to the neck, armpits, and groin. Fan the person or use evaporative cooling if water is available."},
                {"step": 4, "title": "Monitor Symptoms", "description": "Watch for signs of severe dehydration: confusion, rapid heartbeat, little to no urination, or fainting."},
                {"step": 5, "title": "Seek Help if Severe", "description": "If the person can't keep fluids down, shows signs of heat exhaustion, or becomes confused, seek emergency medical attention."}
            ]
        },
        
        "Bee Sting": {
            "patterns": ["How do you treat a bee sting?", "wasp sting", "stung by bee", "insect sting", "multiple stings"],
            "steps": [
                {"step": 1, "title": "Remove Stinger", "description": "If the stinger is visible, remove it immediately by scraping it out with a credit card or fingernail. Don't use tweezers as this can squeeze more venom."},
                {"step": 2, "title": "Clean the Area", "description": "Wash the sting site with soap and water to prevent infection. Pat dry with a clean towel."},
                {"step": 3, "title": "Apply Cold", "description": "Apply ice wrapped in a cloth for 15-20 minutes to reduce swelling and pain. Remove ice for 10 minutes then reapply."},
                {"step": 4, "title": "Take Antihistamine", "description": "Give an antihistamine like Benadryl to reduce swelling and itching. Follow package directions for dosage."},
                {"step": 5, "title": "Watch for Allergic Reaction", "description": "Monitor for severe allergic reaction: difficulty breathing, swelling of face or throat, rapid pulse, or dizziness. Call 911 if these occur."}
            ]
        },
        
        "Tick Bite": {
            "patterns": ["How do you treat a tick bite?", "tick removal", "found tick", "Lyme disease", "tick embedded"],
            "steps": [
                {"step": 1, "title": "Remove Tick Properly", "description": "Use fine-tipped tweezers to grasp the tick as close to skin as possible. Pull upward with steady pressure. Don't twist or jerk as this can break off parts."},
                {"step": 2, "title": "Clean the Area", "description": "After removal, clean the bite area and your hands with rubbing alcohol or soap and water. Dispose of the tick in alcohol or flush down toilet."},
                {"step": 3, "title": "Monitor the Site", "description": "Watch the bite site for several weeks for signs of a rash, especially a bulls-eye pattern which may indicate Lyme disease."},
                {"step": 4, "title": "Note the Date", "description": "Record the date of the tick bite and take a photo if possible. This information may be helpful if symptoms develop later."},
                {"step": 5, "title": "Seek Medical Care", "description": "See a doctor if you develop fever, rash, or flu-like symptoms within 3-30 days of the bite. Early treatment of tick-borne diseases is most effective."}
            ]
        },
        
        "Severe Sunburn": {
            "patterns": ["How do you treat severe sunburn?", "burned by sun", "blistering sunburn", "sun poisoning", "second degree sunburn"],
            "steps": [
                {"step": 1, "title": "Get Out of Sun", "description": "Move to shade or indoors immediately. Remove any clothing that might be irritating the burned skin."},
                {"step": 2, "title": "Cool the Skin", "description": "Take cool (not cold) baths or showers. Apply cool, wet towels to the burned areas for 15-20 minutes several times a day."},
                {"step": 3, "title": "Hydrate Inside and Out", "description": "Drink lots of water to prevent dehydration. Apply moisturizer with aloe vera while skin is still damp. Avoid products with alcohol."},
                {"step": 4, "title": "Protect Blisters", "description": "Don't pop blisters - they protect healing skin underneath. If blisters break, clean gently and apply antibiotic ointment."},
                {"step": 5, "title": "Seek Medical Care", "description": "Get immediate medical attention for severe burns with extensive blistering, fever, chills, or signs of infection like pus or red streaking."}
            ]
        }
    }

def add_more_emergencies():
    """Add additional emergency types"""
    return {
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
        
        "Sprains": {
            "patterns": ["How do you treat a sprain?", "sprained ankle", "twisted joint", "sports injury", "joint pain"],
            "steps": [
                {"step": 1, "title": "Rest the Injury", "description": "Stop activity immediately and rest the injured area. Avoid putting weight on a sprained ankle or using a sprained wrist."},
                {"step": 2, "title": "Apply Ice", "description": "Apply ice wrapped in a towel for 15-20 minutes every 2-3 hours for the first 48 hours to reduce swelling and pain."},
                {"step": 3, "title": "Compress the Area", "description": "Wrap the injured area with an elastic bandage to provide support and reduce swelling. Don't wrap too tightly as this can cut off circulation."},
                {"step": 4, "title": "Elevate the Injury", "description": "Raise the injured area above heart level when possible, especially when resting. This helps reduce swelling."},
                {"step": 5, "title": "Monitor and Seek Care", "description": "If pain is severe, you can't bear weight, or there's numbness, seek medical attention. Most sprains heal with proper rest and care."}
            ]
        },
        
        "Fever": {
            "patterns": ["How do you treat a fever?", "high temperature", "burning up", "hot with fever", "temperature over 100"],
            "steps": [
                {"step": 1, "title": "Stay Hydrated", "description": "Drink plenty of fluids like water, clear broths, or electrolyte solutions. Avoid alcohol and caffeine which can lead to dehydration."},
                {"step": 2, "title": "Rest and Cool Down", "description": "Rest in a cool, comfortable environment. Remove excess clothing and use lightweight blankets. Take cool (not cold) baths or showers."},
                {"step": 3, "title": "Take Fever Reducers", "description": "Take acetaminophen (Tylenol) or ibuprofen (Advil) as directed on the package. Do not give aspirin to children under 18."},
                {"step": 4, "title": "Monitor Temperature", "description": "Check temperature regularly. For adults, seek medical care if fever exceeds 103°F (39.4°C) or lasts more than 3 days."},
                {"step": 5, "title": "Seek Medical Care", "description": "Call 911 if fever is accompanied by difficulty breathing, chest pain, severe headache, stiff neck, confusion, or persistent vomiting."}
            ]
        },
        
        "Bruises": {
            "patterns": ["How do you treat bruises?", "black and blue", "contusion", "bruised area", "blood under skin"],
            "steps": [
                {"step": 1, "title": "Apply Ice Immediately", "description": "Apply ice wrapped in a towel for 15-20 minutes as soon as possible after the injury. This helps reduce swelling and pain."},
                {"step": 2, "title": "Elevate if Possible", "description": "If the bruise is on an arm or leg, elevate it above heart level when resting to help reduce swelling."},
                {"step": 3, "title": "Avoid Heat Initially", "description": "For the first 24-48 hours, avoid heat, hot baths, or heating pads as these can increase swelling and make bruising worse."},
                {"step": 4, "title": "Take Pain Relievers", "description": "Take acetaminophen for pain. Avoid aspirin or ibuprofen initially as they can increase bleeding and make bruising worse."},
                {"step": 5, "title": "Monitor for Complications", "description": "Seek medical care if the bruise is very large, extremely painful, or if you develop signs of infection like increased warmth or red streaks."}
            ]
        }
    }

# Create the complete dataset
def create_complete_dataset():
    all_responses = {}
    all_responses.update(create_manual_emergency_dataset())
    all_responses.update(add_trauma_emergencies())
    all_responses.update(add_medical_emergencies())
    all_responses.update(add_more_emergencies())
    all_responses.update(add_outdoor_emergencies())
    
    # Create training examples
    training_examples = []
    
    for emergency_type, data in all_responses.items():
        for pattern in data["patterns"]:
            example = {
                "input": pattern,
                "output": {
                    "steps": data["steps"]
                }
            }
            training_examples.append(example)
    
    # Shuffle and save
    random.seed(42)
    random.shuffle(training_examples)
    
    with open('processed_data/complete_manual_dataset.jsonl', 'w') as f:
        for example in training_examples:
            f.write(json.dumps(example) + '\n')
    
    print(f"✅ Created {len(training_examples)} training examples")
    print(f"✅ Covers {len(all_responses)} emergency types")
    print("\nAll Emergency Types Covered:")
    for i, emergency_type in enumerate(all_responses.keys(), 1):
        step_count = len(all_responses[emergency_type]["steps"])
        print(f"{i:2d}. {emergency_type}: {step_count} steps")

if __name__ == "__main__":
    create_complete_dataset() 