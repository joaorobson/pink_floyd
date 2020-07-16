import os
import json

NOT_FOUND_SONGS = [
    {
        "title": "Marooned",
        "album": "The Division Bell",
        "year": "1994-03-28",
        "lyrics": "",
    },
    {
        "title": "Terminal Frost",
        "album": "A Momentary Lapse of Reason",
        "year": "1987-09-07",
        "lyrics": ""
    },
    {
        "title": "It’s What We Do",
        "album": "The Endless River",
        "year": "2014-11-07",
        "lyrics": "",
    },
    {"title": "Sum", "album": "The Endless River", "year": "2014-11-07", "lyrics": ""},
    {
        "title": "Skins",
        "album": "The Endless River",
        "year": "2014-11-07",
        "lyrics": "",
    },
    {
        "title": "Unsung",
        "album": "The Endless River",
        "year": "2014-11-07",
        "lyrics": "",
    },
    {
        "title": "Anisina",
        "album": "The Endless River",
        "year": "2014-11-07",
        "lyrics": "",
    },
    {
        "title": "The Lost Art of Conversation",
        "album": "The Endless River",
        "year": "2014-11-07",
        "lyrics": "",
    },
    {
        "title": "On Noodle Street",
        "album": "The Endless River",
        "year": "2014-11-07",
        "lyrics": "",
    },
    {
        "title": "Night Light",
        "album": "The Endless River",
    "year": "2014-11-07",
    "lyrics": "",
},
{
    "title": "Allons-y (1)",
    "album": "The Endless River",
    "year": "2014-11-07",
    "lyrics": "",
},
{
    "title": "Autumn ’68",
    "album": "The Endless River",
    "year": "2014-11-07",
    "lyrics": "",
},
{
    "title": "Allons-y (2)",
    "album": "The Endless River",
    "year": "2014-11-07",
    "lyrics": "",
},
{
    "title": "Talkin’ Hawkin’",
    "album": "The Endless River",
    "year": "2014-11-07",
    "lyrics": "Speech has allowed the communication of ideas, enabling human beings to work together to build the impossible\nMankind's greatest achievements have come about by talking\nOur greatest hopes could become reality in the future, with the technology at our disposal, the possibilities are unbounded\n\nAll we need to do is make sure we keep talking\n",
},
{
    "title": "Calling",
    "album": "The Endless River",
    "year": "2014-11-07",
    "lyrics": "",
},
{
    "title": "Eyes to Pearls",
    "album": "The Endless River",
    "year": "2014-11-07",
    "lyrics": "",
},
{
    "title": "Surfacing",
    "album": "The Endless River",
    "year": "2014-11-07",
    "lyrics": "",
},
{"title": "TBS9", "album": "The Endless River", "year": "2014-11-07", "lyrics": ""},
{
    "title": "TBS14",
    "album": "The Endless River",
    "year": "2014-11-07",
    "lyrics": "",
},
{
    "title": "Nervana",
    "album": "The Endless River",
    "year": "2014-11-07",
    "lyrics": "",
},
{
    "title": "When You’re In",
    "album": "Obscured By Clouds",
    "year": "1972-06-02",
    "lyrics": "",
},
{
    "title": "Wot’s... Uh the Deal?",
    "album": "Obscured By Clouds",
    "year": "1972-06-02",
    "lyrics": """
Heaven sent the promised land\n
Looks alright from where I stand\n
'Cause I’m the man on the outside looking in\n
Waiting on the first step\n
Show me where the key is kept\n
Point me down the right line because it’s time\n\n
To let me in from the cold\n
Turn my lead into gold\n
'Cause there’s a chill wind blowing in my soul\n
And I think I’m growing old\n\n
Flash the readies\n
Wot’s… uh-the deal?\n
Got to make it to the next meal\n
Try to keep up with the turning of the wheel\n
Mile after mile\n
Stone after stone\n
Turn to speak but you’re alone\n
Million miles from home, you’re on your own\n\n
So let me in from the cold\n
Turn my lead into gold\n
Cause there’s a chill wind blowing in my soul\n
And I think I’m growing old\n\n
Fire bright by candlelight\n
And her by my side\n
And if she prefers we will never stir again\n
Someone sent the promised land\n
And I grabbed it with both hands\n
Now I'm the man on the inside looking out\n\n
Hear me shout \"Come on in!\"\n
\"What’s the news and where've you been?\"\n
Cause there’s no wind left in my soul\n
And I’ve grown old\n""",
    },
    {
        "title": "Mudmen",
        "album": "Obscured By Clouds",
        "year": "1972-06-02",
        "lyrics": "",
    },
    {
        "title": "Childhood’s End",
        "album": "Obscured By Clouds",
        "year": "1972-06-02",
        "lyrics": """
You shout in your sleep\n
Perhaps the price is just too steep\n
Is your conscience at rest\n
If once put to the test?\n
You awake with a start\n
To just the beating of your heart\n
Just one man beneath the sky\n
Just two ears, just two eyes\n\n
You set sail across the sea\n
Of long past thoughts and memories\n
Childhood’s end, your fantasies\n
Merge with harsh realities\n
And then as the sail is hoist\n
You find your eyes are growing moist\n
All the fears never voiced\n
Say you have to make your final choice\n\n
Who are you and who am I\n
To say we know the reason why?\n
Some are born; some men die\n
Beneath one infinite sky\n
There’ll be war, there’ll be peace\n
But everything one day will cease\n
All the iron turned to rust;\n
All the proud men turned to dust\n
And so all things, time will mend\n
So this song will end\n""",
    },
    {
        "title": "Absolutely Curtains",
        "album": "Obscured By Clouds",
        "year": "1972-06-02",
        "lyrics": "",
    },
    {
        "title": "Don’t Leave Me Now",
        "album": "The Wall",
        "year": "1979-11-30",
        "lyrics": """
Ooh, babe, don't leave me now\n\n
Don't say it's the end of the road\n
Remember the flowers I sent\n
I need you, babe\n
To put through the shredder in front of my friends\n\n
Oh, babe, don't leave me now\n\n
How could you go?\n
When you know how I need you\n
(Need you, need you, need you, need you, need you, need you)\n
To beat to a pulp on a Saturday night\n\n
Oh, babe, don't leave me now\n\n
How can you treat me this way?\n
Running away\n
Ooh, babe, why are you running away?\n\n
Ooh, babe\n
Ooh, babe\n
Ooh, babe\n
Ooh, ooh\n
Argh!\n""",
    },
    {
        "title": "Atom Heart Mother",
        "album": "Atom Heart Mother",
        "year": "1970-10-02",
        "lyrics": '"Here is a loud announcement"\n\n"Silence in the studio!'
    },
    {
        "title": "Summer ’68",
        "album": "Atom Heart Mother",
        "year": "1970-10-02",
        "lyrics": """
Would you like to say something before you leave?\n
Perhaps you'd care to state exactly how you feel\n
We say goodbye before we've said hello\n
I hardly even like you, I shouldn't care at all\n
We met just six hours ago, the music was too loud\n
From your bed I gained a day and lost a bloody year\n\n
And I would like to know:\n
How do you feel?\n
How do you feel? Oh\n
How do you feel?\n
How do you feel? Oh\n\n
Paaaaaa pa-pap paaaaaaa\n
Pa-pa paaaa pa-pa pap pa paaaaa\n
Pa pap pa paaaa\n\n
Not a single word was said, the night still hid our fears\n
Occasionally you showed a smile but what was the need\n
I felt the cold far too soon in a room of 95\n
My friends are lying in the sun, I wish that I was there\n
Tomorrow brings another town another girl like you\n
Have you time before you leave to greet another man?\n\n
Just you let me know:\n
How do you feel?\n
How do you feel? Oh\n
How do you feel?\n
How do you feel? Oh\n\n
Paaaaaa pa paaaaaaa\n
Pa-pa paaaa pa-pa pa pa pa-pa pa-pa pap paaaaa\n
Pap pa pa-pap paaaa\n\n
Goodbye to you\n
Charlotte Pringle's due\n
I've had enough\n
For one day\n""",
    },
    {
        "title": "Alan’s Psychedelic Breakfast",
        "album": "Atom Heart Mother",
        "year": "1970-10-02",
        "lyrics": """
    Oh, uh, me flakes, then uh, scrambled eggs, bacon, sausages, tomatoes... toast, coffee... marmalade, I like marmalade. Yes, porridge is nice. Any cereal, I like all cereals... oh God. Kickoff is 10am\n\n
    Breakfast in Los Angeles, macrobiotic stuff\n\n
    I don't mind a barrack where I can bury my stuff in\n
    I got a terrible back. When I work, it hurts me\n
    ... it's ready for the gig\n
    I don't know\n
    This electrical stuff I can't bother with it so...\n
    All my head's a blank\n
    """,
    },
    {
        "title": "The Grand Vizier’s Garden Party",
        "album": "Ummagumma",
        "year": "1969-10-25",
        "lyrics": "",
    },
    {
        "title": "Party Sequence",
        "album": "More (Original Film Soundtrack)",
        "year": "1969-06-13",
        "lyrics": "",
    },
    {
        "title": "Main Theme",
        "album": "More (Original Film Soundtrack)",
        "year": "1969-06-13",
        "lyrics": "",
    },
    {
        "title": "More Blues",
        "album": "More (Original Film Soundtrack)",
        "year": "1969-06-13",
        "lyrics": "",
    },
    {
        "title": "Quicksilver",
        "album": "More (Original Film Soundtrack)",
        "year": "1969-06-13",
        "lyrics": "",
    },
    {
        "title": "Dramatic Theme",
        "album": "More (Original Film Soundtrack)",
        "year": "1969-06-13",
        "lyrics": "",
    },
]


#JSON_NAMES = os.listdir("lyrics")
JSON_NAMES = ["The-Endless-River.json"]
print(JSON_NAMES)
INTEREST_FEATURES = ["title", "lyrics", "album", "year"]
lyrics =  [i for i in NOT_FOUND_SONGS if i['album'].find("River") >= 0]
for filename in JSON_NAMES:
    lyrics_json = json.load(open("lyrics/{}".format(filename), "r"))

    print(filename, len(lyrics_json["songs"]))
    for song in lyrics_json["songs"]:
        lyrics.append({'title': song['title'], 'album': song['album'], 'year': song['year'], 'lyrics':song['lyrics']})
        print(song["title"])
print(lyrics)
