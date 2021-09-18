import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("python app.py --lr_d 0.001 --lr_g 0.001")

    # Arguments with defaults
    # ------------------------------------------
    parser.add_argument("--lr_d",
                        type=float,
                        default=0.001,
                        help="Learning rate of the discriminator")
    parser.add_argument("--lr_g",
                        type=float,
                        default=0.001,
                        help="Learning rate of the generator")
    parser.add_argument("--disc_path",
                        type=str,
                        default=None,)

    parser.add_argument("--train", dest="train", action="store_true",
                        help="Specify flag to train model")
    parser.set_defaults(train=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()


