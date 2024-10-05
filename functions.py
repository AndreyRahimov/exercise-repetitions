import pygame

# Initialize pygame mixer
pygame.mixer.init()


def play_sound(sound_file: str) -> None:
    """Plays a .wav sound file and waits until the sound finishes.

    Args:
        sound_file (str): The path to the .wav file to be played.

    Behavior:
        - Loads the specified sound file using pygame.
        - Plays the sound.
        - Waits in a loop until the sound finishes playing before returning."""

    # Load the sound file (must be a .wav file)
    pygame.mixer.music.load(sound_file)

    # Play the sound
    pygame.mixer.music.play()

    # Wait until the sound finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
