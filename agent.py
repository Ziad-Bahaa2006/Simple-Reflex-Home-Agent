
# Alexandria National University - Faculty of Computers and Data Science
#  Smart Systems - Assignment 1: Simple-Reflex-Home-Agent 
#  Team Members: [Ziad Bahaa Elsayed-2405720], [Mohamed Ahmed Elmesarea-2405727], [Mohamed Islam Ibrahim-2405736]
# ==========================================

# ------------------------------------------
# PART 1: PERCEPTS (INPUTS)
#  كل واحد يحدد الانبوتس اللي محتاجها هنا
# [Input 1] Temperature (Example: float)
# [Input 2] Light Status (Example: yes/no)
# [Input 3] Motion Sensor (Example: yes/no)
# [Input 4] Smoke/Gas Sensor (Example: yes/no)
# [Input 5] Door Status (Example: open/closed)
# ------------------------------------------

motion=input("Is there a motion? (yes/no)")
time_of_day=input("Is it day or night? (day/night)")
light_level=input("What is light level (low/high)")

# -----------------------------------------------------------------
# SECURITY & EMERGENCY PERCEPTS
# -----------------------------------------------------------------
print("-" * 40)
print("--- 🛡️ Security System Initialization ---")

# 1. High Priority: Emergency Sensors (Safety First)
smoke_level = float(input("[Sensor] Enter Smoke Level (0.0 to 1.0): "))
emergency_button = input("[User] Is the Emergency Button pressed? (yes/no): ").lower()

# 2. Medium Priority: Intrusion & System State
system_armed = input("[System] Is the security system ARMED? (yes/no): ").lower()
door_status = input("[Sensor] Is the door open? (yes/no): ").lower()
motion_detected = input("[Sensor] Is there motion detected? (yes/no): ").lower()

print("-" * 40)

# ------------------------------------------------------------------------------------------------------------------------------
# PART 2: THE INTELLIGENT AGENT LOGIC (IF-THEN RULES)
#  هنا كل واحد يحط الـ Logic بتاعه

# --- Smart Lighting Logic ---

def lighting_agent(motion,time_of_day,light_level):
        # Rule 1: Night + Motion → ON
    if motion == "yes" and time_of_day == "night" and light_level == "low":
        return "Light ON (High Brightness)"
    
    # Rule 2: Night + Motion (normal)
    elif motion == "yes" and time_of_day == "night":
        return "Light ON"
    
    # Rule 3: Night + No Motion → OFF
    elif motion == "no" and time_of_day == "night":
        return "Light OFF"
    
    # Rule 4: Day + Motion → OFF (save energy)
    elif motion == "yes" and time_of_day == "day":
        return "Light OFF"
    
    # Rule 5: Day + No Motion → OFF
    elif motion == "no" and time_of_day == "day":
        return "Light OFF"
    
    # Default
    else:
        return "No Action"
# ------------------------------------------



# --- MEMBER 2 BLOCK: Climate & Air Quality Logic ---
# Rule 3: ...
# Rule 4: ...



# ------------------------------------------
# -- Advanced Security & Emergency (Ziad's Module) ---

# 1. Emergency Protocol (Highest Priority)
if emergency_button == "yes" or smoke_level > 0.5:
    security_action = "🚨 EMERGENCY: Calling Fire Dept/Ambulance & Unlocking all exits!"

# 2. Intrusion Detection (Armed State)
elif system_armed == "yes":
    if door_status == "open":
        security_action = "🛡️ INTRUSION: Door breach detected! Sounding Siren!"
    elif motion_detected == "yes":
        security_action = "🛡️ INTRUSION: Motion detected inside! Activating Cameras!"
    else:
        security_action = "🔒 System Armed & Secure."

# 3. Smart Welcome (Disarmed State)
elif system_armed == "no":
    if door_status == "open":
        security_action = "🔓 Welcome Home. Disarming security sensors."
    else:
        security_action = "🏠 Home Mode: Monitoring only for emergencies."

# 4. Final Fallback
else:
    security_action = "⚠️ System Status Unknown. Please check sensors."

# ------------------------------------------
# PART 3: ACTIONS (OUTPUTS)
# هنا بيتم طباعة القرارات النهائية بشكل واضح ومنظم

print("\n",lighting_agent(motion,time_of_day,light_level))
# [Output 2] Climate System Status
# -----------------------------------------------------------------

# This section displays the final decision of the Security Agent
print("-" * 40)
print(f"[{'!] SYSTEM STATUS' if '🚨' in security_action else 'i] SYSTEM STATUS'}")
print(f"Final Security Decision: {security_action}")
print("-" * 40)
# ------------------------------------------
print("\n--- End of Agent Decisions ---")
