import time

from functions import play_sound


def main(repetitions_amount: int, repetition_duration: int = 5) -> None:
    """Plays sounds to indicate the start, switch, and end of exercise repetitions.

    Args:
        repetitions_amount (int): The number of exercise repetitions to perform.
        repetition_duration (int, optional): Duration (in seconds) between each repetition. Defaults to 5 seconds.

    Behavior:
        - Plays the "start.wav" sound at the beginning.
        - Plays the "switch.wav" sound between repetitions.
        - Plays the "finish.wav" sound after the final repetition."""

    print("Repetition: 1")
    play_sound("start.wav")
    time.sleep(repetition_duration)

    for i in range(repetitions_amount - 1):
        print(f"Repetition: {i + 2}")
        play_sound("switch.wav")
        time.sleep(repetition_duration)

    play_sound("finish.wav")


if __name__ == '__main__':
    repetitions_amount = int(input("How many times do you want to repeat an exercise? "))
    main(repetitions_amount)
