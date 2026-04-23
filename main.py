from greet import greeter


def main():
    """Regression test for the greeter() function with Latin-based names."""
    print("Running greet module regression tests...\n")
    
    # Test cases with 5 Latin-based names
    test_names = [
        "Marcus",      # Roman praenomen
        "Julius",      # Roman family name (as in Julius Caesar)
        "Lucius",      # Roman praenomen
        "Augustus",    # Roman praenomen/title (as in Augustus Caesar)
        "Aeneas",      # Trojan hero from Roman mythology
    ]
    
    all_passed = True
    
    for name in test_names:
        result = greeter(name)
        expected = f"Hi {name}"
        passed = result == expected
        all_passed = all_passed and passed
        
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: greeter('{name}') = '{result}'")
        
        if not passed:
            print(f"       Expected: '{expected}'")
    
    print()
    if all_passed:
        print("All regression tests passed!")
        return 0
    else:
        print("Some regression tests failed!")
        return 1


if __name__ == "__main__":
    exit(main())
