import math

MAX_REQUESTS = 1000
MAX_CYLINDER = 5000

def read_requests(filename):
    requests = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                requests.append(int(line.strip()))
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        exit(1)
    except ValueError:
        print("Error: Invalid data in the input file.")
        exit(1)
    return requests

def fcfs(requests, start_pos):
    total_movement = abs(start_pos - requests[0])
    for i in range(1, len(requests)):
        total_movement += abs(requests[i] - requests[i - 1])
    return total_movement

def scan(requests, start_pos):
    requests.sort()
    total_movement = 0
    i = 0

    # Move towards the end
    while i < len(requests) and requests[i] < start_pos:
        i += 1
    for j in range(i, len(requests)):
        total_movement += abs(start_pos - requests[j])
        start_pos = requests[j]

    # Move towards the start
    for j in range(i - 1, -1, -1):
        total_movement += abs(start_pos - requests[j])
        start_pos = requests[j]

    return total_movement

def c_scan(requests, start_pos):
    requests.sort()
    total_movement = 0
    i = 0

    # Move towards the end
    while i < len(requests) and requests[i] < start_pos:
        i += 1
    for j in range(i, len(requests)):
        total_movement += abs(start_pos - requests[j])
        start_pos = requests[j]

    # Jump to the start and continue
    if i > 0:
        total_movement += abs(start_pos - MAX_CYLINDER - 1)
        start_pos = 0
        for j in range(0, i):
            total_movement += abs(start_pos - requests[j])
            start_pos = requests[j]

    return total_movement

if __name__ == "__main__":
    requests = read_requests("input.txt")
    start_pos = 1000  # Example start position

    print(f"FCFS Total Head Movements: {fcfs(requests, start_pos)}")
    print(f"SCAN Total Head Movements: {scan(requests, start_pos)}")
    print(f"C-SCAN Total Head Movements: {c_scan(requests, start_pos)}")

