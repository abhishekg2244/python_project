import json

try:
    with open("config.json", "r") as f:
        config = json.load(f)

    print(config["app"])

except FileNotFoundError:
    print("Config file nahi mili.")

except json.JSONDecodeError:
    print("JSON file invalid hai.")

finally:
    print("Configuration process complete.")