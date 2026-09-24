def street_light_agent(environment_light):
    if environment_light == "Dark":
        return "Light ON"
    else:
        return "Light OFF"

perceptions = ["Dark", "Dark", "Bright", "Dark", "Bright", "Bright"]
print("Smart Street Light Agent - Simple Reflex Agent")
print("=" * 45)
for i, perception in enumerate(perceptions):
    action = street_light_agent(perception)
    print(f"Step {i+1}: Perception = {perception} -> Action = {action}")

print()
print("Agent Details:")
print("Sensor     : Light Sensor / LDR (detects ambient light)")
print("Actuator   : Street Light Switch (ON/OFF)")
print("Agent Type : Simple Reflex Agent")
print("Environment: Fully Observable, Single-agent, Static")
