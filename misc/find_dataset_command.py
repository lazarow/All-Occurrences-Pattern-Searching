import sys
import subprocess
import time

dataset = sys.argv[1]
sizeOfPattern = int(sys.argv[2])
sizeOfAlphabet = int(sys.argv[3])
sizeOfText = int(sys.argv[4])
seed = int(sys.argv[5])

def run_command(command, timeout):
    try:
        start_time = time.time()
        subprocess.run(command, shell=True, check=True, timeout=timeout, stdout = subprocess.DEVNULL)
        execution_time = time.time() - start_time
        return execution_time
    except subprocess.TimeoutExpired:
        print(f"Command timed out after {timeout} seconds.")
        return None
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        return None

while True:
    generation_command = f"python generate.py {sizeOfPattern} {sizeOfAlphabet} {sizeOfText} {seed} > datasets/dataset{dataset}.txt"
    print(f"Running generation command: {generation_command}")
    run_command(generation_command, 30)
    algorithm_command = f"algorithms\\automaton-on-suffix-tree\\STzad11\\bin\\Release\\net8.0\\STzad11.exe datasets\\dataset{dataset}.txt"
    execution_time = run_command(algorithm_command, 65)
    if execution_time is None:
        print("Execution failed or timed out. Adjusting the command.")
        seed += 1
        continue
    if execution_time < 5:
        print(f"Command executed too quickly ({execution_time} s). Adjusting the command.")
        seed += 1
    elif execution_time > 60:
        print(f"Command took too long ({execution_time} s). Adjusting the command.")
        seed += 1
    else:
        print(f"Command executed within the desired time range ({execution_time} s).")
        break
