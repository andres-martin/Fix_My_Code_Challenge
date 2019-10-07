#!/usr/bin/python3
""" Check response
"""

if __name__ == "__main__":
    try:
        from square import Square

        if Square.__init__.__doc__ is None or len(Square.__init__.__doc__) < 10:
            print("Missing documentation for __init__ method or not enough")
            exit(1)

        if Square.area_of_my_square.__doc__ is None or len(Square.area_of_my_square.__doc__) < 10:
            print("Missing documentation for area_of_my_square method or not enough")
            exit(1)

        if Square.permiter_of_my_square.__doc__ is None or len(Square.permiter_of_my_square.__doc__) < 10:
            print("Missing documentation for permiter_of_my_square method or not enough")
            exit(1)

        if Square.__str__.__doc__ is None or len(Square.__str__.__doc__) < 10:
            print("Missing documentation for __str__ method or not enough")
            exit(1)

        print("OK", end="")
    except:
        import sys
        print("Error: {}".format(sys.exc_info()))
