import time

def typing_speed_test():
    test_text = "If you believe in yourself anything is possible."
    print("Typing Speed Tester")
    print("--------------------")
    print("Type the following sentence as fast as you can:\n")
    print(f'"{test_text}"\n')

    input("Press Enter to start...")
    start_time = time.time()

    user_input = input("\nStart typing: ")
    end_time = time.time()

    time_taken = end_time - start_time
    word_count = len(test_text.split())
    speed_wpm = (word_count / time_taken) * 60

    print("\n--- Results ---")
    if user_input.strip() == test_text:
        print(f"Typing Speed: {speed_wpm:.2f} WPM")
        print("Accuracy: 100%")
    else:
        correct_chars = sum(1 for i, c in enumerate(user_input) if i < len(test_text) and c == test_text[i])
        accuracy = (correct_chars / len(test_text)) * 100
        print(f"Typing Speed: {speed_wpm:.2f} WPM")
        print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_speed_test()


