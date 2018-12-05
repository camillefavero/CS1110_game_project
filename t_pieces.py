
import gamebox

# Piece conditions
s = 20
h = (s/2)*(3**0.5)
piece_x = 150
piece_y = -60

# Makes the tetrominoes:
tet1 = gamebox.from_polygon(piece_x, piece_y, "red",
                            (0, 0),
                            (-s, 0),
                            (-s, -s),
                            (s, -s),
                            (s, 2*s),
                            (0, 2*s)
                            )
tet2 = gamebox.from_polygon(piece_x, piece_y, "orange",
                            (0, 0),
                            (s, 0),
                            (s, -s),
                            (-s, -s),
                            (-s, 2*s),
                            (0, 2*s)
                            )
tet3 = gamebox.from_polygon(piece_x, piece_y, "yellow",
                            (0, 0),
                            (0, -s),
                            (-s, -s),
                            (-s, s),
                            (0, s),
                            (0, 2*s),
                            (s, 2*s),
                            (s, 0)
                            )
tet4 = gamebox.from_polygon(piece_x, piece_y, "green",
                            (0, 0),
                            (0, -s),
                            (s, -s),
                            (s, s),
                            (0, s),
                            (0, 2*s),
                            (-s, 2*s),
                            (-s, 0)
                            )
tet5 = gamebox.from_polygon(piece_x, piece_y, "blue",
                            (0, 0),
                            (s, 0),
                            (s, s),
                            (0, s),
                            (0, 2*s),
                            (-s, 2*s),
                            (-s, -s),
                            (0, -s)
                            )
tet6 = gamebox.from_polygon(piece_x, piece_y, "purple",
                            (0, -2*s),
                            (s, -2*s),
                            (s, 2*s),
                            (0, 2*s)
                            )
tet7 = gamebox.from_polygon(piece_x, piece_y, "pink",
                            (-s, -s),
                            (s, -s),
                            (s, s),
                            (-s, s)
                            )
tetrominoes = [tet1, tet2, tet3, tet4, tet5, tet6, tet7]

# Makes the tritrominoes:
tri1 = gamebox.from_polygon(piece_x, piece_y, "red",
                            (0, 0),
                            (-s/2, -h),
                            (s/2, -h),
                            (s, 0),
                            (s/2, h),
                            (-s/2, h),
                            (-s, 0)
                            )

tri2 = gamebox.from_polygon(piece_x, piece_y, "yellow",
                            (0, 0),
                            (-s/2, -h),
                            (s/2, -h),
                            (s, 0),
                            (0, 2*h),
                            (-s/2, h)
                            )

tri3 = gamebox.from_polygon(piece_x, piece_y, "green",
                            (0, 0),
                            (-s/2, -h),
                            (s/2, -h),
                            (1.5*s, h),
                            (-s/2, h)
                            )

tri4 = gamebox.from_polygon(piece_x, piece_y, "blue",
                            (0, 0),
                            (-s/2, -h),
                            (1.5*s, -h),
                            (s/2, h),
                            (-s/2, h)
                            )

tri5 = gamebox.from_polygon(piece_x, piece_y, "purple",
                            (0, 0),
                            (-s/2, -h),
                            (0, -2*h),
                            (s, 0),
                            (s/2, h),
                            (-s/2, h)
                            )

tri6 = gamebox.from_polygon(piece_x - 40, piece_y, "orange",
                            (-s/2, h),
                            (s, -2*h),
                            (1.5*s, -h),
                            (s/2, h)
                            )

tritrominoes = [tri1, tri2, tri3, tri4, tri5, tri6]
