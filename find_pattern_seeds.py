import json
from sys import platform
import subprocess
import time

def run_command(command, timeout):
    try:
        start_time = time.time()
        result = subprocess.run(command, shell=True, check=True, timeout=timeout, capture_output=True, text=True)
        execution_time = time.time() - start_time
        output = result.stdout.strip()
        return [execution_time, len(output)]
    except subprocess.TimeoutExpired:
        print(f"Command timed out after {timeout} seconds.")
        return [None, None]
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        return [None, None]

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

        while True:
            generationCommand = f"{pythonCommand} generate_pattern.py {sizeOfPattern} {sizeOfAlphabet} {seedOfPattern} > datasets/pattern{datasetNumber}.txt"
            subprocess.run(generationCommand, shell=True)
            print(f"Running generation command: {generationCommand}")
            subprocess.run(f"cat datasets/text{datasetNumber}.txt datasets/pattern{datasetNumber}.txt > datasets/dataset{datasetNumber}.txt", shell=True)
            algorithmCommand = f"algorithms/automaton-on-suffix-tree/STzad11/bin/Release/net8.0/STzad11 datasets/dataset{datasetNumber}.txt"
            [executionTime, sizeOfOutput] = run_command(algorithmCommand, 120)
            if executionTime is None:
                print("Execution failed or timed out. Adjusting the command.")
                seedOfPattern += 1
                continue
            if executionTime < 5:
                print(f"Command executed too quickly ({executionTime} s). Adjusting the command.")
                seedOfPattern += 1
            elif executionTime > 120:
                print(f"Command took too long ({executionTime} s). Adjusting the command.")
                seedOfPattern += 1
            elif sizeOfOutput == 0:
                print(f"Command executed with no output ({executionTime} s). Adjusting the command.")
                seedOfPattern += 1
            else:
                print(f"Command executed within the desired time range ({executionTime} s).")
                break
