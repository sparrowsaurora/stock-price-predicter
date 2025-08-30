import os

def main() -> None:
    try:
        os.system("uvicorn display.api:app --reload")
    except KeyboardInterrupt:
        print("Exiting...")
        exit

if __name__ == "__main__":
    main()
