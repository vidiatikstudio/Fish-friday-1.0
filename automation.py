import requests

# --- ESP32 Configuration ---
# Paste the exact IP address your ESP32 printed in the Serial Monitor here
ESP32_IP = "192.168.43.51"  # Replace with your actual ESP32 IP address
BASE_URL = f"http://{ESP32_IP}"

def control_device(device, state):
    """
    Sends an HTTP GET request to the ESP32 to control a device.
    device: 'light' or 'fan'
    state: 'ON' or 'OFF'
    """
    # Build the URL matching the ESP32 web server endpoints
    # Example target: http://192.168.X.X/light/ON
    url = f"{BASE_URL}/{device}/{state.upper()}"
    
    try:
        print(f"[FRIDAY] Sending command to hardware: {device.upper()} -> {state.upper()}...")
        response = requests.get(url, timeout=3)
        
        if response.status_code == 200:
            print(f"[FRIDAY] Success: {device.upper()} is now {state.upper()}.")
            return True
        else:
            print(f"[FRIDAY] Warning: Server responded with status code {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"[FRIDAY] Error: Could not reach ESP32 at {ESP32_IP}.")
        print("Please check if the ESP32 is powered on and connected to the same Wi-Fi.")
        return False