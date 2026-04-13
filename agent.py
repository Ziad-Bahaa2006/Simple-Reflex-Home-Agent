
#  Alexandria National University - Faculty of Computers and Data Science
#  Smart Systems - Assignment 1: Simple-Reflex-Home-Agent 
#  Team Members: [Ziad Bahaa Elsayed-2405720], [Mohamed Ahmed Elmesarea-2405727], [Mohamed Islam Ibrahim-2405736]
# ==========================================

# ------------------------------------------
# PART 1: PERCEPTS (INPUTS)
# ------------------------------------------
print("--- 🏠 Smart Home Sensor Initialization ---")

# Lighting Percepts
motion=input("Is there a motion? (yes/no)")
time_of_day=input("Is it day or night? (day/night)")
light_level=input("What is light level (low/high)")

# Climate Percepts

temperature = float(input("Enter temperature (°C): "))


# SECURITY & EMERGENCY PERCEPTS

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
# ----------------------------------------------------
# PART 2: THE INTELLIGENT AGENT LOGIC (IF-THEN RULES)
# ----------------------------------------------------

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
    
# --- climate_agent ---
def climate_agent(temperature, smoke_level):

    # --- Smoke Logic ---
    if smoke_level >= 0.7:
        smoke_status = " Ventilation ON (MAX)"
    elif smoke_level >= 0.4:
        smoke_status = " Ventilation ON (Normal)"
    elif smoke_level >= 0.2:
        smoke_status = " Air Monitoring (Low Ventilation)"
    else:
        smoke_status = " Ventilation OFF"


    # --- Temperature Logic ---
    if temperature >= 30:
        temp_status = "❄️ AC ON (High Cooling)"
    elif temperature >= 25:
        temp_status = "❄️ AC ON (Normal Cooling)"
    elif temperature >= 20:
        temp_status = "✅ Climate Stable (No Action)"
    elif temperature >= 15:
        temp_status = "🔥 Heater ON (Normal)"
    else:
        temp_status = "🔥 Heater ON (High)"


    # --- Final Output ---
    return f"{temp_status} | {smoke_status}"


# -- Security & Emergency (Ziad's Module) ---

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

# -----------------------------------------------------------------------------------------------
# PART 3: ACTIONS (OUTPUTS)
# -----------------------------------------------------------------------------------------------

print("\n" + "=" * 40)
print("🤖 AGENT FINAL DECISIONS:")
print("=" * 40)

# 1. Lighting Output
print("\n",lighting_agent(motion,time_of_day,light_level))

# 2. Climate Output
print("-" * 40)
print("--- 🌡️ Climate System Status ---")
print(climate_agent(temperature, smoke_level))
print("-" * 40)

# 3. Security Output
print(f"[{'!] SYSTEM ALERT' if '🚨' in security_action else 'i] SYSTEM STATUS'}")
print(f"Final Security Decision: {security_action}")
print("-" * 40)

print("--- End of Smart Home Agent Execution ---")