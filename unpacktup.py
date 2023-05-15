albums = [("clb", "Drake", 2021,
           [
                   (1, "No friends"),
                   (2, "TSU"),
                   (3, "Knife Talk"),
           ],
           ),
          ("Dawn FM","The weeknd",2022,
           [
               (1,"Moth to a Flame"),
               (2,"Here we go again"),
               (3,"Out of time"),
           ]
           ),
]


for name, artist, year, songs in albums:
        print("name: {}, artist: {}, year: {}, songs: {}"
              .format(name, artist, year, songs))

KnifeTalk= albums[1][3][1][1]
print(KnifeTalk)

print(albums[1][3])

