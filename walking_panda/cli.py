from . import panda

import argparse

def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate",help="Suppress Rotation",
                        action="store_true")
    parser.add_argument("--scale",help="Change Panda Size",
                        action="store", type=float, default=1.0)
    parser.add_argument("--pose", help="Make Panda Stationary",
                        action="store_true")
    parser.add_argument("--friends", help="Make More Pandas",
                        action="store", type=int, default=1)
    parser.add_argument("--color", help="Randomise Panda Colors",
                        action="store_true")
    parser.add_argument("--music", help="Turn Music On",
                        action="store_true")
    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()