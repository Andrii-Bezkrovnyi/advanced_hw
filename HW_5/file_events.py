import os
import threading
import time

# Shared event between threads
wow_event = threading.Event()


# Function 1: checks for the file and searches for "Wow!"
def file_checker(filename):
    while True:
        if not os.path.exists(filename):
            print(f"[Checker] File '{filename}' not found. Sleeping 5 seconds...")
            time.sleep(5)
            continue

        print(f"[Checker] File '{filename}' found. Reading...")
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()

        if "Wow!" in content:
            print("[Checker] 'Wow!' found! Triggering event...")
            wow_event.set()  # Generate event
            break
        else:
            print("[Checker] 'Wow!' not found. Sleeping 5 seconds...")
            time.sleep(5)


# Function 2: waits for the event and deletes the file
def file_remover(filename):
    print("[Remover] Waiting for 'Wow!' event...")
    wow_event.wait()  # Wait until event is set
    if os.path.exists(filename):
        os.remove(filename)
        print(f"[Remover] File '{filename}' has been deleted.")
    else:
        print("[Remover] File was already removed.")


# Function 3: runs both threads
def main():
    filename = "test_wow.txt"

    t1 = threading.Thread(target=file_checker, args=(filename,))
    t2 = threading.Thread(target=file_remover, args=(filename,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("[Main] Program finished.")


if __name__ == "__main__":
    main()
