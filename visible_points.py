import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import pandas as pd

from src.points import PlayingField, Point


def main():
    # read data
    data = pd.read_csv("points.csv")

    # create playing field
    playing_field = PlayingField()

    # populate playing field with players
    for i, row in data.iterrows():
        playing_field.add_point(
            Point(
                playing_field=playing_field,
                position=(int(row["X"]), int(row["Y"])),
                direction=row["Direction"],
                id=row["Number"],
            )
        )

    # # print it out
    # for point in playing_field.points:
    #     print(f"{point.id}: Position {point.position}, Direction {point.direction}")
    # print("\n\n")

    # # find visible points and print to stdout
    # angle = 45
    # distance = 20
    # visible_points = []
    # for point in playing_field.points:
    #     visible_points.append(playing_field.visible_points(point.id, angle, distance))

    # If you want an interactive tool, use the code below
    id = int(input("enter a point id: "))
    angle = int(input("enter an angle: "))
    distance = int(input("enter a distance: "))
    print("-------")
    playing_field.visible_points(id, angle, distance)

if __name__ == "__main__":
    main()