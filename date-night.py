from time import sleep

print "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
sleep(1)
print "loading Choose Your Own Date Night!"
sleep(.5)
print "loading"
sleep(.5)
print "loading."
sleep(.5)
print "loading.."
sleep(.5)
print "loading..."
sleep(.5)
print "Done!"
sleep(1)
print""

# Welcome the user
print "Welcome to Choose Your Own Date Night"
sleep(2)
print""
print "I am just a basic app designed to help you have spontaneous fun with your spouse"
sleep(3)
print "I'm going to ask you some simple questions"
sleep(3)
print "and then I'll use your answers to give you a Date Night recommendation"
sleep(3)
print""

# explain question section
print "I will ask you what neighborhood you want to go to"
sleep(3)
print "what type of cuisine you're in the mood for"
sleep(3)
print "and what intensity of activity you're up for"
sleep(3)
print""

# ask the user for permission to continue
user_input = raw_input("Sound good? Type 'yes' or 'no': ")
sleep(2)
if user_input == 'yes':
    print("Great!") 
else:
    print("aww too bad, we're doing this anyways")
sleep(2)
print""

neighborhoods = ["uws", "west village", "dumbo", "park slope"]

# begin question section
neighborhood = raw_input("What neighborhood do you want to go to? (type uws, west village, dumbo, or park slope): ")
sleep(2)
print "Hmm, so you want to go to %s. Got it." % neighborhood
sleep(2)
print""

cuisine = raw_input("What type of cuisine do you want for dinner? (enter thai, japanese, american, or veggie): ")
sleep(2)
print "Okay, great! %s it is. I can handle that." % cuisine
sleep(2)
print""

intensity = raw_input("What intensity level are you feeling tonight? (enter high, medium, low, or 'abort' to just head home): ")
sleep(2)
if intensity == 'abort':
    print "Ok! Let's head home!"
    exit()
else:
    print "Alrighty then! %r intensity sounds good to me too." % intensity
sleep(2)
print""

# recap user inputs
print "So let's recap"
sleep(2)
print "You want to go to %s, eat some %s food, and do something %s intensity." % (neighborhood, cuisine, intensity)
sleep(2)
print""

print "Let me find some options"
print""
sleep(2)
print "Thinking"
sleep(1)
print "Thinking."
sleep(1)
print "Thinking.."
sleep(1)
print "Thinking..."
sleep(1)
print""
print "Got it!"
print""
sleep(1)

# restaurant variables
uws_thai = "Land Thai"
uws_jap = "Miyako Sushi"
uws_amer = "Jacob's Pickles / Maison"
uws_veg = "Blossom on Columbus"

wv_thai = "Pinto Garden"
wv_jap = "Omakase Room"
wv_amer = "Hudson Clearwater"
wv_veg = "Westville Hudson"

d_thai = "Thai Sidewalk"
d_jap = "Sugarcane"
d_amer = "Vinegar Hill House"
d_veg = "Westville Dumbo"

ps_thai = "Nourish Thai"
ps_jap = "Mori NYC"
ps_amer = "Stone Park Cafe"
ps_veg = "Luanne's Wild Ginger"

# activity variables
uws_high = "catch a show at Smoke Jazz Club"
uws_med = "get a craft cocktail at Nobody Told Me"
uws_low = "play a board game at Hex & Company"

wv_high = "catch a show at the Village Vanguard" 
wv_med = "play some games at Fatcat"
wv_low = "play a board game at The Uncommons"

d_high = "try some VR at vrbar"
d_med = "shop at the Empire Stores"
d_low = "hang out at the Powerhouse Arena"

ps_high = "check out a show at Union Hall"
ps_med = "grab a craft beer at Threes Brewing"
ps_low = "find a book at Community Bookstore"

## print Date Night recommendation ##

# upper west recommendations
if neighborhood == 'uws' and cuisine == 'thai' and intensity == 'high':
    print "We'll eat at %s in the Upper West Side and %s" % (uws_thai, uws_high)
elif neighborhood == 'uws' and cuisine == 'thai' and intensity == 'medium':
    print "We'll eat at %s in the Upper West Side and %s" % (uws_thai, uws_med)
elif neighborhood == 'uws' and cuisine == 'thai' and intensity == 'low':
    print "We'll eat at %s in the Upper West Side and %s" % (uws_thai, uws_low)

elif neighborhood == 'uws' and cuisine == 'japanese' and intensity == 'high':
    print "We'll eat at %s in the Upper West Side and %s" % (uws_jap, uws_high)
elif neighborhood == 'uws' and cuisine == 'japanese' and intensity == 'medium':
    print "We'll eat at %s in the Upper West Side and %s" % (uws_jap, uws_med)
elif neighborhood == 'uws' and cuisine == 'japanese' and intensity == 'low':
    print "We'll eat at %s in the Upper West Side and %s" % (uws_jap, uws_low)

elif neighborhood == 'uws' and cuisine == 'american' and intensity == 'high':
    print "We'll eat at %s in the Upper West Side and %s" % (uws_amer, uws_high)
elif neighborhood == 'uws' and cuisine == 'american' and intensity == 'medium':
    print "We'll eat at %s in the Upper West Side and %s" % (uws_amer, uws_med)
elif neighborhood == 'uws' and cuisine == 'american' and intensity == 'low':
    print "We'll eat at %s in the Upper West Side and %s" % (uws_amer, uws_low)

elif neighborhood == 'uws' and cuisine == 'veggie' and intensity == 'high':
    print "We'll eat at %s in the Upper West Side and %s" % (uws_veg, uws_high)
elif neighborhood == 'uws' and cuisine == 'veggie' and intensity == 'medium':
    print "We'll eat at %s in the Upper West Side and %s" % (uws_veg, uws_med)
elif neighborhood == 'uws' and cuisine == 'veggie' and intensity == 'low':
    print "We'll eat at %s in the Upper West Side and %s" % (uws_veg, uws_low)
# west village recommendations
elif neighborhood == 'west village' and cuisine == 'thai' and intensity == 'high':
    print "We'll eat at %s in the West Village and %s" % (wv_thai, wv_high)
elif neighborhood == 'west village' and cuisine == 'thai' and intensity == 'medium':
    print "We'll eat at %s in the West Village and %s" % (wv_thai, wv_med)
elif neighborhood == 'west village' and cuisine == 'thai' and intensity == 'low':
    print "We'll eat at %s in the West Village and %s" % (wv_thai, wv_low)

elif neighborhood == 'west village' and cuisine == 'japanese' and intensity == 'high':
    print "We'll eat at %s in the West Village and %s" % (wv_jap, wv_high)
elif neighborhood == 'west village' and cuisine == 'japanese' and intensity == 'medium':
    print "We'll eat at %s in the West Village and %s" % (wv_jap, wv_med)
elif neighborhood == 'west village' and cuisine == 'japanese' and intensity == 'low':
    print "We'll eat at %s in the West Village and %s" % (wv_jap, wv_low)

elif neighborhood == 'west village' and cuisine == 'american' and intensity == 'high':
    print "We'll eat at %s in the West Village and %s" % (wv_amer, wv_high)
elif neighborhood == 'west village' and cuisine == 'american' and intensity == 'medium':
    print "We'll eat at %s in the West Village and %s" % (wv_amer, wv_med)
elif neighborhood == 'west village' and cuisine == 'american' and intensity == 'low':
    print "We'll eat at %s in the West Village and %s" % (wv_amer, wv_low)

elif neighborhood == 'west village' and cuisine == 'veggie' and intensity == 'high':
    print "We'll eat at %s in the West Village and %s" % (wv_veg, wv_high)
elif neighborhood == 'west village' and cuisine == 'veggie' and intensity == 'medium':
    print "We'll eat at %s in the West Village and %s" % (wv_veg, wv_med)
elif neighborhood == 'west village' and cuisine == 'veggie' and intensity == 'low':
    print "We'll eat at %s in the West Village and %s" % (wv_veg, wv_low)
# dumbo recommendations
elif neighborhood == 'dumbo' and cuisine == 'thai' and intensity == 'high':
    print "We'll eat at %s in Dumbo and %s" % (d_thai, d_high)
elif neighborhood == 'dumbo' and cuisine == 'thai' and intensity == 'medium':
    print "We'll eat at %s in Dumbo and %s" % (d_thai, d_med)
elif neighborhood == 'dumbo' and cuisine == 'thai' and intensity == 'low':
    print "We'll eat at %s in Dumbo and %s" % (d_thai, d_low)

elif neighborhood == 'dumbo' and cuisine == 'japanese' and intensity == 'high':
    print "We'll eat at %s in Dumbo and %s" % (d_jap, d_high)
elif neighborhood == 'dumbo' and cuisine == 'japanese' and intensity == 'medium':
    print "We'll eat at %s in Dumbo and %s" % (d_jap, d_med)
elif neighborhood == 'dumbo' and cuisine == 'japanese' and intensity == 'low':
    print "We'll eat at %s in Dumbo and %s" % (d_jap, d_low)

elif neighborhood == 'dumbo' and cuisine == 'american' and intensity == 'high':
    print "We'll eat at %s in Dumbo and %s" % (d_amer, d_high)
elif neighborhood == 'dumbo' and cuisine == 'american' and intensity == 'medium':
    print "We'll eat at %s in Dumbo and %s" % (d_amer, d_med)
elif neighborhood == 'dumbo' and cuisine == 'american' and intensity == 'low':
    print "We'll eat at %s in Dumbo and %s" % (d_amer, d_low)

elif neighborhood == 'dumbo' and cuisine == 'veggie' and intensity == 'high':
    print "We'll eat at %s in Dumnbo and %s" % (d_veg, d_high)
elif neighborhood == 'dumbo' and cuisine == 'veggie' and intensity == 'medium':
    print "We'll eat at %s in Dumbo and %s" % (d_veg, d_med)
elif neighborhood == 'dumbo' and cuisine == 'veggie' and intensity == 'low':
    print "We'll eat at %s in Dumbo and %s" % (d_veg, d_low)
# park slope recommendations
elif neighborhood == 'park slope' and cuisine == 'thai' and intensity == 'high':
    print "We'll eat at %s in Park Slope and %s" % (ps_thai, ps_high)
elif neighborhood == 'park slope' and cuisine == 'thai' and intensity == 'medium':
    print "We'll eat at %s in Park Slope and %s" % (ps_thai, ps_med)
elif neighborhood == 'park slope' and cuisine == 'thai' and intensity == 'low':
    print "We'll eat at %s in Park Slope and %s" % (ps_thai, ps_low)

elif neighborhood == 'park slope' and cuisine == 'japanese' and intensity == 'high':
    print "We'll eat at %s in Park Slope and %s" % (ps_jap, ps_high)
elif neighborhood == 'park slope' and cuisine == 'japanese' and intensity == 'medium':
    print "We'll eat at %s in Park Slope and %s" % (ps_jap, ps_med)
elif neighborhood == 'park slope' and cuisine == 'japanese' and intensity == 'low':
    print "We'll eat at %s in Park Slope and %s" % (ps_jap, ps_low)

elif neighborhood == 'park slope' and cuisine == 'american' and intensity == 'high':
    print "We'll eat at %s in Park Slope and %s" % (ps_amer, ps_high)
elif neighborhood == 'park slope' and cuisine == 'american' and intensity == 'medium':
    print "We'll eat at %s in Park Slope and %s" % (ps_amer, ps_med)
elif neighborhood == 'park slope' and cuisine == 'american' and intensity == 'low':
    print "We'll eat at %s in Park Slope and %s" % (ps_amer, ps_low)

elif neighborhood == 'park slope' and cuisine == 'veggie' and intensity == 'high':
    print "We'll eat at %s in Park Slope and %s" % (ps_veg, ps_high)
elif neighborhood == 'park slope' and cuisine == 'veggie' and intensity == 'medium':
    print "We'll eat at %s in Park Slope and %s" % (ps_veg, ps_med)
elif neighborhood == 'park slope' and cuisine == 'veggie' and intensity == 'low':
    print "We'll eat at %s in Park Slope and %s" % (ps_veg, ps_low)

else:
    print "Uh oh! I must have parsed your response incorrectly"
    print "You said %r, %r, %r ... right?" % (neighborhood, cuisine, intensity)
    print "Your spouse may need to help interpret, I am just a robot after all..."
print""
sleep(1)
print "Enjoy your night <3"
sleep(1)
print""