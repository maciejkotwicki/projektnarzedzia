import sys
import json
import yaml
arguments = sys.argv[1:]
print("Passed arguments:", arguments)
json_file = "file.json"
try:
    with open(json_file, "r") as file:
        data = json.load(file)
    print("Loaded JSON data:", data)
except Exception as e:
    print("Failed to load JSON data from file:", e)
output_file = "output.json"
try:
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)
    print("JSON data saved to", output_file)
except Exception as e:
    print("Failed to save JSON data:", e)
yml_file = "file.yml"
try:
    with open(yml_file, "r") as file:
        data = yaml.safe_load(file)
    print("Loaded YAML data:", data)
except Exception as e:
    print("Failed to load YAML data from file:", e)
output_file = "output.yml"
try:
    with open(output_file, "w") as file:
        yaml.dump(data, file)
    print("YAML data saved to", output_file)
except Exception as e:
    print("Failed to save YAML data:", e)
xml_file = "file.xml"
try:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    print("Loaded XML data:")
    for child in root:
        print(child.tag, child.text)
except Exception as e:
    print("Failed to load XML data from file:", e)