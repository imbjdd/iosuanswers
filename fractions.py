# fractions (input hardcoded) 

f = open("out2.txt", "a")

def foo(inp):
	res = []
	for i in range(inp+1, 2*inp+2):
		if (i*inp % (i-inp))==0:
			res.append((i, int(1/(1/inp - 1/i))))
	for val in res:
	 	f.write('1/' + str(inp) + ' = 1/' + str(val[1]) + ' + 1/' + str(val[0]))
	 	f.write('\n')


L=[78123,72466,43925,53361,52579,47285,54676,11419,91917,21915,32196,85586,48429,24116,79526,97366,13594,62206,78396,11626,86940,20931,38156,91682,85560,67303,61546,4031,23939,24633,4404,96636,45929,28047,81045,17713,20350,124,4222,66424,29780,18960,13856,20342,93878,27357,77915,58010,96415,21568,83181,7827,71431,10144,35834,94086,64292,31959,61857,89696,8128,77839,28821,27447,85428,74642,95975,93118,38020,88218,7747,82662,55354,37930,38439,79922,4682,47579,64869,36408,59921,96341,56554,22996,55822,88369,91871,95030,58315,17623,39134,49854,39227,55162,89423,98082,52512,8965,84460,33269,70902,66763,71076,81353,44537,27395,50723,85929,59918,46152,91345,14476,34764,92778,82222,79218,23987,26904,23088,24285,76086,70888,34878,89056,95116,28324,77912,24781,21423,87394,24454,95051,96679,18868,59481,15129,4402,54096,97799,17403,46318,16892,38264,51573,20803,72401,2789,59913,39755,94442,8694,21606,88562,62684,41072,97196,96722,7511,72583,3965,44890,30895,99620,50876,79916,23117,40040,59379,67689,71875,10455,24431,77402,5432,83823,95320,36115,7056,77636,21678,59820,30253,99572,71972,81477,88086,29360,48040,51736,11812,51401,14355,19994,78694,81195,48307,58029,97099,90791,96994,88097,3042,90012,51881,1593,68726,90973,46608,90931,66213,17188,15640,621,27874,80038,15992,13218,90222,18958,26566,4671,35773,296,42026,70283,41388,29674,93884,48229,39212,68452,5195,75174,61065,69449,31740,12196,42061,68518,16575,13895,70334,46682,45863,49395,65569,74327,26427,23943,92559,51573,15101,33971,14605,66862,35708,74453,20518,26025,98399,35113,97863,92791,17506,54271,73450,29899,77018,49628,6028,8797,49096,77627,24541,20779,27334,49163,14695,89971,57939,69902,82383,87764,99335,34064,22655,39312,73736,63418,20275,12200,95748,86347,8602,97431,31633,96248,65914,95871,78442,30618,75110,108,15925,20297,14124,64481,42090,59795,85208,88863,341,42971,12199,69868,30745,14300,10039,52729,2240,18843,5250,66030,38190,59023,63953,6063,97522,56567,45456,39938,69749,30193,47918,46966,44127,14801,58570,14338,68190,95699,83305,13085,87445,53516,98203,91649,83302,16730,16680,15786,38104,24377,69110,41989,37922,12998,6545,50611,67026,25987,55994,3374,46150,32844,44933,4662,97405,46903,92991,51841,12633,41423,78513,7344,2366,83570,13637,36483,32626,35885,70315,52340,77987,66979,96903,88915,85629,23512,21654,36181,55893,67243,69895,38921,91028,89343,38207,69027,27621,11932,28429,40659,93376,73020,60988,66037,19313,14698,89007,15734,32734,45848,4899,73264,83546,63037,13453,34582,54506,94612,29660,84098,50208,2093,79384,32417,84781,80482,44650,97074,43841,90474,58333,52183,79833,31585,89394,13500,77510,20918,22172,75105,27545,1606,54673,65351,89276,76869,14787,46173,55843,65315,10356,10222,62540,71305,87069,3836,24518,81022,96185,93633,27046,98677,65645,7025,44417,25456,91456,572,56064,10143,62832,51354,91398,83293,72592,42383,72521,4484,75171,24151,1071,52674,43003,96615,94343,9045,32884,76910,37001,42800,97296,22620,80839,50397,70648,95699,37357,60920,58280,5612,54621,25533,89762,56786,39366,36063,66836,53366,53663,56356,82038,84642,63575,90957,65198,91597,43111,10682,50397,94209,90360,12091,61921,7256,95350,49258,52679,74923,35958,92622,98850,91791,90117,57228,47981,63888,40919,9476,4271,25439,91537,67722,78369,62503,47742,9444,24299,16746,59307,83550,83460,73244,60953,99818,32841,55842,4035,40184,76362,33764,22291,7082,34054,11853,40657,39432,12563,70898,60772,48169,81714,47510,99893,17304,81162,30153,78359,16137,31941,98682,12628,80798,82973,22041,50252,60440,95740,17030,52804,45582,55475,51868,20424,10038,70318,63410,14788,42055,60706,10508,60413,72592,68209,44105,97893,29651,87483,29506,15878,67061,92213,22646,41194,95882,33053,36808,52565,30913,26735,78337,62207,83754,16378,35035,94389,32943,95227,85648,64674,9578,22609,59880,42574,66845,80969,232,38796,64408,66444,76146,49572,8614,22668,17257,29966,64646,38511,22222,50891,5408,29986,73753,61489,81209,16158,49340,21993,19104,65691,85066,30368,86318,5550,86911,56199,13001,36393,35276,16947,22736,19455,31697,16056,54306,51663,48764,96052,69536,38772,79412,32437,71121,97664,8820,68549,11533,28366,28230,86827,10318,52223,66217,91858,7052,71028,72630,62488,74019,23922,28810,87521,45672,44110,4506,47601,96193,63718,26791,89674,18227,87699,63104,6477,61711,90213,3108,47723,96814,20256,49456,38922,15405,32406,6313,85310,21032,73944,77056,62735,69714,4964,2442,35830,74255,45743,38445,35830,6290,91864,38985,90560,24977,35466,12686,15787,51617,98325,62419,30819,48693,17315,68807,27237,1941,20388,81732,19043,26619,37134,69710,98712,90512,75347,55383,29780,30581,11008,35796,30626,19030,33738,67133,65689,79572,92224,87205,91547,15580,14098,90058,52619,56164,62059,88512,61007,47799,1408,34933,55450,11228,50197,22584,22322,97665,12328,79873,87356,80,68125,15274,23256,60240,59313,46153,63554,10661,47444,44913,17814,96867,14353,11191,99162,55986,66425,97951]
for val in L:
	foo(val)
f.close()
