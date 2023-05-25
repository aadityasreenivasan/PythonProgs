#List albums containing tuples of lists of tuples
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
           ("Meet The Woo","Pop Smoke",2020,
           [
               (1,"Invincible"),
               (2,"Shake The Room"),
               (3,"Christopher Walking"),
           ]
           ),
           ("Birds In The Trap Sing McKnight","Travis Scott",2016,
           [
               (1,"sdp interlude"),
               (2,"outside"),
               (3,"Goosebumps"),
               (4,"pick up thr phone"),
               (5,"beibs in the trap"),
           ]
           ),
]

#for loop to display items in the List Albums
for name, artist, year, songs in albums:
        print("name: {}, artist: {}, year: {}, songs: {}"
              .format(name, artist, year, songs))

KnifeTalk= albums[1][3][1][1]
print(KnifeTalk)

print(albums[1][3])

