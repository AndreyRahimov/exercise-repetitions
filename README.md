# Exercise Repetitions

## Overview

The **Exercise Repetitions** program is a simple Python application designed to help users manage and track their exercise routines. It plays sound cues for different intervals, indicating when to switch exercises or when a session has ended.

## Features

- **Customizable Repetitions**: Specify how many repetitions you want to perform.
- **Sound Cues**: Plays different sound files to indicate the start of the session, switch intervals, and the end of the session.
- **Easy to Use**: The application is straightforward to run and customize.

## Requirements

- Python 3.12 or higher
- Pygame library for sound playback

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AndreyRahimov/exercise-repetitions.git
   cd exercise-repetitions

2. Install the required libraries:

   ```bash
   pip install pygame

3. (Optional) Create a virtual environment for better package management:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate

## Usage

To run the program, use the following command:

   ```bash
   python main.py <repetitions_amount> [<repetition_duration>]
   ```

* repetitions_amount: The total number of repetitions to perform.
* repetition_duration: The duration (in seconds) for each repetition. This is optional and defaults to 5 seconds.

### Example

   ```bash
   python main.py 10 3
   ```

This command starts the exercise session with 10 repetitions, each lasting 3 seconds.

## Sound Files

Ensure that you have the following sound files in the same directory as the script:

*  start.wav: Sound to indicate the start of the session.
*  switch.wav: Sound to indicate switching between repetitions.
*  finish.wav: Sound to indicate the end of the session.
