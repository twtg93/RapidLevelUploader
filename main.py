from urllib.request import urlopen,Request
import webbrowser
gjver = "20"
print('Geometry Dash Rapid Level Uploader Hack')
print('Hack made by : BunnyGamerGD and HackedHard ')
print(' ')
Server = input('Enter Server URL: ')
AccID = input('Enter Your User ID: ')
b = input('Enter Level Name: ')
c = input('Enter Level Version: ')
d = input('Enter Level Song ID: ')
e = input('Enter Level Coins Amount: ')
f = input('Enter Level Requested Stars: ')
 
 
 
a = 0
while a > -1:
    a = a + 1
 
    url = ""+str(Server)+""
    p = "gameVersion=20&binaryVersion=29&USID="+str(AccID)+"&userName=Hack&levelID=0&levelName="+str(b)+" "+str(a)+"&levelDesc=&levelVersion="+str(c)+"&levelLength=4&audioTrack=0&auto=1&password=0&original=0&twoPlayer=0&songID="+str(d)+"&objects=30000&coins="+str(e)+"&requestedStars="+str(f)+"&extraString=29_29_29_40_29_29_29_29_29_29_29_29_29_29_29_29&seed=K6cfLiGvDV&seed2=BVQFUgBSVwQBBVECC1UBBAIKAQRQVwAEUQAABAYHUQhTVFYNAgZUBA==&levelString=H4sIAAAAAAAAC6WP0Q2DMAxEFzKSz44DiC9mYIAbgBU6fEnc_tBKpeLnXuzLnZJ980nAojTCgk6LIJCwRC4LB7ASqsqRIA6HE_EAe1rtWhq30vM53ey8eylvbNFTR_v5u0N_NcS3Bv3nDfWzQfYVLtoQiZoocmiex9y8MDVsPvfJumZBN9bSNV1oAqILBGICD3EZEMsTGgXGGAECAAA=&levelInfo=H4sIAAAAAAAACzPUszC2NrAGAHBkYpsHAAAA&secret=Wmfd2893gb7"
    p = p.encode()
    data = urlopen(url,p).read().decode()
 
    Level_Name = 'Level Name : ' + str(b) + ' ' + repr(a)
    Level_ID = 'Level ID : ' + str(data)
    Border = ' '
    print (Border)
    print (Level_Name)
    print (Level_ID)
