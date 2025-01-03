from pathlib import Path
from sys import argv
import json

# this script converts area coord used in the previous HTML map version of this
# project to latlng coords usable by leaflet js

# for Shanai
# area_coords = {
#    "lyreth": "1139,983,887,745",
#    "graev": "594,1090,859,1327",
#    "silk-port": "1404,792,1828,997",
#    "umberfhel": "2922,28,3351,224",
#    "winter-sea": "1968,489,2881,680",
#    "endless-sea": "54,1537,221,2469",
#    "zerqan": "1348,1509,1614,1719",
#    "qyiax": "1642,1532,1870,1770",
#    "shai-yn": "985,2063,1297,2292",
#    "tubul": "789,2348,1013,2543",
#    "yllan": "976,2571,1264,2692",
#    "usol": "943,2958,1153,3153",
#    "soule": "1176,3014,1386,3209",
#    "kwaixl": "1665,2338,2065,2525",
#    "suntouched-sea": "1544,3358,2648,3535",
#    "veithaar": "2336,2366,2708,2520",
#    "ithaar": "2610,2017,2936,2171",
#    "kepe": "3165,2888,3365,3097",
#    "silent-sea": "3202,2087,4031,2296",
#    "sleet": "3649,3149,3859,3335",
#    "tenzu": "4049,3247,4371,3428",
#    "port-tivar": "4455,2525,4920,2678",
#    "yoros": "4613,1933,4874,2119",
#    "sedhar": "2764,1341,3048,1621",
#    "hadria": "4017,1458,4315,1626",
#    "mercaia": "3751,1290,4082,1458",
#    "seleria": "4175,880,4455,1109",
#    "darun": "4590,1318,4869,1500",
#    "efretes": "5018,1644,5218,2408",
# }


# MAP_HEIGHT = 3880
# MAP_WIDTH = 5272

# x1, y1, x2, y2
area_coords = {
    "trig": "48,158,213,306",
    "belfrost": "398,244,585,368",
    "fo": "653,33,750,172",
    "maul": "834,163,987,273",
    "annis": "1698,77,1858,200",
    "alldark": "1634,264,1861,361",
    "di-loth": "869,451,1124,552",
    "westfall": "1251,438,1478,592",
    "tusk": "0,590,121,1063",
    "aro": "295,676,728,825",
    "teth": "812,612,974,731",
    "lyka": "1467,621,1702,717",
    "baldurkeep": "550,900,300,1139",
    "anethyr": "669,990,915,1155",
    "faelaen": "1214,805,1447,885",
    "bahz": "1454,904,1641,990",
    "karathuhm": "130,1307,378,1437",
    "mystra-academy": "431,1193,631,1393",
    "duin": "600,1408,726,1516",
    "saltcliff": "757,1479,1009,1582",
    "port-amyr": "1047,1149,1331,1305",
    "Fane": "1801,1532,1993,1620",
    "valynor": "317,1851,556,1959",
    "demlin-sea": "1785,1288,1300,1739",

"Anchorage Vista": "2875,3519,2905,3549",
"Ardesia": "1724,3825,1754,3855",
"Claw Harbour": "2493,4056,2523,4086",
"Cochrane River": "1762,3531,1792,3561",
"Mithril Lake": "2207,3148,2237,3178",
"Montistum": "1646,3308,1676,3338",
"Rasa": "2569,3150,2599,3180",
"Sabul Pass": "2639,3455,2669,3485",
"Tarsal Desert": "2338,2972,2774,3420",
"The Hold": "2377,3737,2427,3787",
"Vermillis": "2559,2872,2589,2902",
"WillowGlade": "2064,3807,2094,3837",
"Aztarok": "5112,842,5142,872",
"Gaj Gedad": "5050,1607,5080,1637",
"Gedad": "5350,1364,5380,1394",
"Jusomaas": "6000,1546,6050,1596",
"Od-Nenga": "5935,1327,5965,1357",
"Zut'Kitot": "4125,1778,4155,1808",
"Aerduluk": "1880,1986,2931,2984",
"Anduril": "1975,2422,2061,2470",
"Barlenghir": "1954,2249,2082,2305",
"Kadrehl": "1669,2292,1761,2341",
"Korhelihr": "1688,3173,1785,3224",
"Lordakihr": "2094,3014,2216,3063",
"Torruhn": "1312,1412,2376,2419",
"Varkuhldir": "2073,2772,2200,2822",
"Vel-Gendar": "2296,2645,2491,2752",
"Ironscar Hill": "6683,4154,6713,4184",
"Neverport": "6619,4524,6649,4554",
"Repository of Records": "6551,3905,6601,3955",
"Rockfort Ridge": "5859,3612,5949,3665",
"Slag's Reach": "6180,4081,6210,4111",
"Soratin": "5868,3722,5898,3752",
"Tabrise": "6322,4321,6352,4351",
"Trigg's Landing": "5929,3877,5959,3907",
"Borderton": "4996,2640,5026,2670",
"Boscus Pass": "4283,2606,4313,2636",
"Bright Stone": "2846,2189,2876,2219",
"Coval": "4672,2604,4702,2634",
"Elder Point": "3142,2142,3172,2172",
"Elvene": "2981,2380,3011,2410",
"Fernn": "3742,3544,3772,3574",
"Fort Arteron": "2640,2589,2670,2619",
"Groggwood": "4845,2177,4875,2207",
"Korthal": "3248,2127,3298,2177",
"Lunalem": "3719,2443,3749,2473",
"Lyric": "2903,2859,2933,2889",
"Mattermont": "3184,2725,3214,2755",
"Riverhold": "3580,3206,3610,3236",
"Starguard": "3616,2189,3646,2219",
"WakeField": "2648,2397,2678,2427",
"Yellow Ridge": "4294,2907,4324,2937",
"Royal Mines of Morheim": "3695,2047,3923,2152",
"University": "2906,3102,3040,3174",
"Angelfer Island": "6680,3476,6710,3506",
"Aquatas": "6763,3110,6883,3230",
"Ardenport": "5568,2496,5598,2526",
"Carran": "6087,3514,6117,3544",
"Cindergulch": "6995,3707,7025,3737",
"Drymoor": "6331,3778,6361,3808",
"Far Water": "6297,3537,6327,3567",
"Flurham": "5691,2119,5721,2149",
"Meera": "5704,3160,5754,3210",
"MesaPort": "6514,3672,6544,3702",
"Nightshale": "6065,2151,6095,2181",
"Pikecliff": "5428,3084,5458,3114",
"Pikeville": "5316,3116,5346,3146",
"Pirates Sanctum": "6936,2668,6966,2698",
"Port Mid": "6374,2337,6404,2367",
"Port Passer": "5817,3547,5847,3577",
"Port Sheerstone": "6648,2285,6678,2315",
"Retria": "6343,2449,6373,2479",
"Ruslet": "6405,2654,6435,2684",
"Sheerstone Island": "6731,2333,6761,2363",
"Smit": "5614,2765,5644,2795",
"Smuggler's Cove": "5446,2143,5476,2173",
"Tebiton": "7078,3476,7108,3506",
"Usterduum": "5992,2900,6022,2930",
"Uadir": "5876,5286,5906,5316",
"Aphachaigia Isl.": "4932,5162,5174,5321",
"Azureinn Isl.": "4437,5030,4663,5267",
"Broken Earth Isl.": "5119,5505,5357,5600",
"Ichor Landing": "5625,5494,5776,5567",
"Laogai": "5373,5010,5608,5199",
"Mytra": "5825,4953,5825,4953",
"Oman": "5815,4776,5815,4776",
"Frostling Stronghold": "839,2262,869,2292",
"Elantis": "2053,1419,2103,1469",
"Rea Xandor": "2273,1734,2323,1784",
"Rhun": "6585,1293,6635,1343",
"Ty Rythel": "875,1425,905,1455",
"Val'Alora": "2941,1646,2971,1676",
"The Watch House": "528,1996,625,2047",
"Andale Port": "738,2784,768,2814",
"Cindere": "1094,3197,1124,3227",
"Druin": "944,3165,974,3195",
"Elafi Field": "820,3043,850,3073",
"Esperia": "1285,3419,1315,3449",
"Far Point": "1200,4578,1230,4608",
"Freeton": "1246,4186,1276,4216",
"Hearth": "1255,3792,1285,3822",
"KingsPort": "685,3485,715,3515",
"Mistvalley Keep": "1019,3394,1069,3444",
"Oberon Ports": "684,4117,714,4147",
"Red Rock": "1318,3062,1348,3092",
"Revari": "1510,3227,1540,3257",
"Sledge": "1144,2351,1174,2381",
"Somarden": "1004,3560,1034,3590",
"Stillcreek": "1500,3559,1530,3589",
"Usuall": "1251,2938,1281,2968",
"West Warden": "379,3739,409,3769",
"Zirconia": "896,4444,926,4474",
"Hold of Civilization": "3731,4077,3781,4127",
"Sutherland Keep": "3622,4429,3672,4479",
"Underdark Guard Post": "4133,3580,4163,3610",
"Barsellaq": "4298,4206,4328,4236",
"Fallmoer": "4778,3882,4808,3912",
"Katsu-Tal": "4036,3823,4066,3853",
"Mire'Seil": "5060,3388,5110,3438",
"Ousoul-Droth": "4413,3989,4443,4019",
"Tineihm": "4933,3634,4963,3664",
"Vassalqar": "4534,3783,4564,3813",
"Yuntas": "4146,4310,4196,4360",
"The Dead Lake": "3901,3940,3941,3980",
"Lake Vari": "1562,3246,1592,3276",
"Lake Harmony": "1435,2522,1435,2522",
"Loch Redwater": "1310,2992,1350,3032",
"The Great Mountain Lake": "1594,2637,1894,2937",
"Lake Mithril": "2202,3074,2310,3151",
"Lake Arcane": "2992,2869,3192,3069",
"Lake Ene": "2116,2507,2216,2607",
"Tortle Lake": "3933,2742,4213,3022",
"Lake Centhe": "5852,2235,5942,2325",
"Orc Hunt Waters": "6359,1824,6449,1914",
"Patola Lake": "5282,1843,5400,1950",
"Firbolg Shallows": "5735,1156,5836,1215",
"Atlashire Cove": "4733,1258,4835,1312",
"Casrath Lagoon": "4906,866,5029,926",
"Tribal Depths": "5457,1415,5582,1464",
"Carato Marshlands": "5490,966,5771,1146",
"Willow Basin": "2060,3557,2153,3620",
"Lake Shimmer": "3049,673,3282,723",
"Lurker's Vale": "2509,607,2729,633",
"Domain of the Gods": "4951,479,5345,719",
"Hand of The Gods": "5544,805,5803,910",
"Carato Mountains": "5151,902,5317,1029",
"Ekhis Hills": "4719,1038,4874,1150",
"Border Stones": "5625,1326,5837,1364",
"Mt. Mer'Ehl": "6070,1271,6220,1322",
"The Lonely Peak": "5328,1502,5446,1551",
"Jusomaas Border Hills": "6105,1585,6161,1838",
"Mt. Hellion": "5212,1654,5345,1724",
"Twillight Gates": "6125,1907,6392,1983",
"Guardian Mountains": "5636,2025,5957,2077",
"Patola Mountain Range": "4895,1905,5185,1959",
"Stormcrest Mountains": "5957,2370,6145,2627",
"Mt. Blackfuse": "3687,1892,3845,1973",
"Morheim Border Hills": "4180,2000,4557,2156",
"Capital Mountain Range": "2981,1982,3512,2083",
"Attium Hills": "3948,3382,4116,3446",
"Auril Peak": "2262,1282,2366,1447",
"Elantis Faehills": "1995,1497,2180,1680",
"Xandor Faehills": "2431,1639,2687,1665",
"Hyrsasm Peaks": "1808,1804,1908,1882",
"Omega Peak": "1727,2420,1849,2513",
"Smoulder Mountans": "2302,2575,2592,2605",
"Mt. Feyr": "2456,2018,2608,2163",
"Blunder hills": "1036,2685,1146,2767",
"Mourning Walls": "540,1842,828,1892",
"Mourning Mountains": "1064,2041,1315,2292",
"Mt. Harmony": "1394,2432,1502,2502",
"Mt. Winvern": "1079,3480,1146,3529",
"Mt. Esper": "1190,3689,1340,3734",
"Rage Mountain": "1761,3912,1870,3982",
"Claw of the World": "2003,4016,2413,4183",
"Dagger Peaks": "1138,3836,1312,3983",
"Onyx Mountain": "1896,4375,1984,4456",
"Sickle Mountains": "3821,4170,4001,4267",
"The Shard Mountains": "3573,4250,3978,4385",
"The Wildland Cliffs": "6414,4797,6621,4902",
"Arcarath Mountains": "6710,3985,6879,4471",
"Adon's Rest": "2352,2266,2551,2306",
"The Anvil of Stone": "5279,2219,5395,2278",
"The Great Stone Road": "3958,2597,4168,2646",
"The Great Stone Road": "4649,2637,4860,2677",
"The Great Stone Road": "5235,2668,5558,2724",
"The Twin Hills (GreatGaunt + Arden)": "5203,2399,5453,2649",
"The Trail of Bridges": "1482,3370,1533,3486",
"Korthal Forest": "3790,2337,3920,2467",
"The Endless Forest": "4233,2235,4533,2535",
"Hellcrawl Forest": "4820,2700,4940,2820",
"Aris Woods": "3771,2793,3851,2873",
"Astral Woodss": "3210,3018,3280,3088",
"Velvin Thicket": "3045,3160,3215,3330",
"Rage Hollow": "4685,3091,4825,3231",
"Arteron Woods": "2740,2420,3000,2680",
"Feyrian Woods": "1681,1957,2054,2065",
"Ancient Woodlands of Xandor": "1964,1767,2883,1962",
"The Thicket": "1852,3304,2033,3595",
"Dire Forest": "2076,3378,2282,3496",
"Dreamseap Forests": "2499,3692,2603,3855",
"Sycamores Hunt Grounds": "2454,3928,2529,4027",
"Stillwind Forest": "1524,3609,1641,3897",
"Esperian Woods": "1111,3557,1363,3654",
"Old Growth of Elmonn": "802,3701,951,3944",
"Hammercrag Growth": "813,4061,1043,4217",
"Winter Woods": "818,2495,1049,2707",
"Deadgrowth Forest": "3761,3709,3980,3816",
"Grogwood wilds": "4648,2058,4844,2155",
"Patola Woods": "4991,2038,5316,2148",
"Damned Forest": "4898,1564,5036,1714",
"Misty Bog": "4593,1629,4821,1912",
"The Deep Woodlands": "5486,1542,5968,1889",
"Witch King Woodlands": "5350,897,5444,1164",
"Tawere Forest": "6231,1108,6421,1284",
"Tiny Wood": "5986,1172,6178,1215",
"The Covert": "6231,1593,6451,1769",
"Eprerre Woods": "6614,1646,6780,1832",
"Evennfall Woods": "6519,1969,6757,2139",
"Firelight Forest": "6136,2092,6464,2235",
"Angel's Growth": "7009,3560,7224,3710",
"Ikidian Jungle": "6937,3799,7271,4128",
"The Wildlands": "6778,5002,7200,5349",
"Joultou Grove": "3912,2656,4077,2732",
"The Dead Coast": "5874,4006,6126,4271",
"The Guarded Coast": "2714,3790,2834,3910",
"Serpent's Pass": "3369,2587,3469,2687",
"Capital Inlet": "3485,2277,3670,3069",
"Citizen's Path": "3060,2413,3200,2553",
"Capital Channel": "4398,3260,4692,3370",
"Cemetery of the Forgotten": "6208,2731,6408,2931",
"Shimmerian Coast": "5497,2860,5810,2952",
"The Andalin Coast": "519,3269,679,3429",
"The Shores of Zirconia": "627,4194,907,4474",
"The Yuntas Coast": "4259,4249,4568,4346",
"The Free Coast": "4970,3510,5036,3799",
"The Forgotten Shores": "2223,5266,2804,5556",
"White Bay": "3654,3596,3744,3686",
"Dreamshard Depths": "2855,3847,3371,4469",
"Yuntas Sea": "4802,3957,5702,4857",
"The Meerilian Ocean": "6285,2943,6685,3343",
"The Meerilian Islands": "7052,2512,7632,3092",
"Nancy's Reef": "6926,1075,7232,1811",
"Reef of Captain Leadhand": "5691,308,6463,812",
"Tortlewall Reef": "6244,5332,6878,5656",
"Realm's Reach (South)": "63,5856,8105,6075",
"Spirit Bay": "1222,1721,1705,2035",
"Aurillian Ocean": "1123,843,1923,1735",
"Oberon Reef": "437,4176,662,4438",
"Domain of the Lurker": "2774,1246,3380,1490",
"The Sea of the Gods": "3977,88,4641,1239",
"Atlashire Inlet (Cove)": "4540,1406,4683,1544",
"Angel's Route": "6491,3493,6670,3529",
"Tremmor Falls": "4331,3461,4361,3491",
"The Great Falls of Azam": "5129,1972,5169,2012",
"Esper Falls": "1237,3769,1257,3789",
"The Everfalls": "5012,2148,5032,2168",
"The Tarsal Desert": "2338,2972,2774,3420",
"The Azure Fields": "648,2018,920,2194",
"The Fejur Badlands": "3660,1423,4160,1923",
"The Scalded Outlands": "3334,3551,3614,3831",
"The Hammerstone Wastes": "3373,3941,3673,4241",
"Atrium Nooklands": "3925,3421,4065,3561",
"Selum-Tor Sol": "5984,3843,6257,4034",
"Nir-Uhlin Sol": "6379,4164,6747,4476",
"Nehr-Fehlen Er-Losar": "6210,4706,6496,4890",
"Relinquished Holds of Underrun": "1228,4666,2058,4881",
"Silvercourt Valley": "1602,4181,1867,4436",
"Nightstar Fields": "737,3183,976,3457",
"Direshade Valley": "1172,2651,1488,2775",
"Blunder Slopes": "1449,2783,1587,2956",
"The Crystal Tundra": "743,1500,889,1780",
"The Sabul Stones": "2674,3257,2949,3427",
"Short Hill Valley": "5708,2387,5938,2603",
"Saffron Fields": "6589,3779,6823,3835",

       
}

MAP_HEIGHT = 6144
MAP_WIDTH = 8192

if len(argv) != 2:
    raise Exception("Must include a content file")

target_file = argv[1]

path = Path(argv[1])
f = open(path)

places_dict = json.load(f)

for place, info in places_dict.items():
    [x1, y1, x2, y2] = area_coords[place].split(",")

    # flip y coords - leaflet considers 0 bottom whereas html area considers 0
    # the top of the image
    y1 = MAP_HEIGHT - int(y1)
    y2 = MAP_HEIGHT - int(y2)

    # leaflet latlng wants y first
    coords = [[y1, int(x1)], [y2, int(x2)]]
    places_dict[place]["coords"] = coords

content_file = open(path.parent / "places.json", "w")
json.dump(places_dict, content_file)
