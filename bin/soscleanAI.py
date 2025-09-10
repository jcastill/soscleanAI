import sys
import argparse
from soscleanai import SosCleanAI


def main():
    parser = argparse.ArgumentParser(description="Run SoSCleanAI.")
    parser.add_argument("files", nargs="*", help="Files to process")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Enable verbose mode")
    args = parser.parse_args()

    # Create and run CleanAI with parsed args
    cai = SosCleanAI(args)
    try:
        cai.execute()
    except KeyboardInterrupt:
        print("\nInterrupted by user.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
