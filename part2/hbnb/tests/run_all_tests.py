import os

def run_tests():
    test_files = ["test_user.py", "test_place.py", "test_review.py", "test_amenity.py"]
    for test in test_files:
        print(f"🔹 Running {test}...")
        os.system(f"python3 tests/{test}")

if __name__ == "__main__":
    run_tests()
