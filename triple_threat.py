"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Carter Glaspey - November 2024
"""

import random


def main() -> None:
    # set variables for cost to play and base prize
    cost_to_play: int = 1
    base_prize: int = 10
    mega_number: int = 6
    mega_multiplier: int = 10
    # roll three dice
    roll_1: int = random.randint(1, 6)
    roll_2: int = random.randint(1, 6)
    roll_3: int = random.randint(1, 6)
    # check if they are equal
    payout: int = 0
    if roll_1 == roll_2 == roll_3:
        if roll_1 == mega_number:
            payout = base_prize * mega_multiplier
        else:
            payout = base_prize * roll_1
    # output results
    print(f"Casino collects: ${cost_to_play}")
    print(f"player rolls: {roll_1}-{roll_2}-{roll_3}")
if __name__ == "__main__":
    main()