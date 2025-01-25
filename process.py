import time

def main():
    print("Process started. Press Ctrl+C to stop.")
    while True:
        time.sleep(1)  # Sleep for a second to avoid high CPU usage
        print("Process is still running...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Process stopped by user.")
