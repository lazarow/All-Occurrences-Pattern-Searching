import json
import subprocess
from sys import platform

if platform == "linux" or platform == "linux2":
    pythonCommand = "python3"
else:
    pythonCommand = "python"

i = 1
with open('configurations.json', 'r') as file:
    configurations = json.load(file)
    for configuration in configurations:
        sizeOfPattern = int(configuration[0])
        sizeOfAlphabet = int(configuration[1])
        sizeOfText = int(configuration[2])
        seedOfText = int(configuration[3])
        seedOfPattern = int(configuration[4])
        datasetNumber = str(i).rjust(2, "0")
        i += 1
        subprocess.run(f"{pythonCommand} generate_text.py {sizeOfAlphabet} {sizeOfText} {seedOfText} > datasets/text{datasetNumber}.txt", shell=True)
        subprocess.run(f"{pythonCommand} generate_pattern.py {sizeOfPattern} {sizeOfAlphabet} {seedOfPattern} > datasets/pattern{datasetNumber}.txt", shell=True)
        subprocess.run(f"cat datasets/text{datasetNumber}.txt datasets/pattern{datasetNumber}.txt > datasets/dataset{datasetNumber}.txt", shell=True)
        print(f"Dataset {datasetNumber} has been generated")
