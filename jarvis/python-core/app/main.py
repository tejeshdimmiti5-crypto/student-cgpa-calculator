from app.core.orchestrator import JarvisOrchestrator

def main() -> None:
    jarvis = JarvisOrchestrator()
    print("JARVIS online.")
    while True:
        try:
            command = input("You > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nJARVIS offline.")
            break

        if not command:
            continue
        if command.lower() in {"exit", "quit", "shutdown"}:
            print("JARVIS offline.")
            break

        print(f"JARVIS > {jarvis.handle(command)}")

if __name__ == "__main__":
    main()
