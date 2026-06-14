import sys
from datetime import datetime

def main():
    # Get current Python version
    python_version = sys.version
    
    # Get current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("=" * 50)
    print(f"Container Execution Report")
    print("=" * 50)
    print(f"Current Date & Time: {current_time}")
    print(f"Python Version:      {python_version.split('[')[0].strip()}")
    print("=" * 50)

if __name__ == "__main__":
    main()