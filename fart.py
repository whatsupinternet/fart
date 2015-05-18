print 'hello world'
import random

outFart = open('outFart', 'w')

farts = ['brrt', 'braaah', 'THPPTPHTPHPHHPH', 'phhhhhhrt', 'PPPPPPPPPPPPPPPPPPPPPPPPPPP', 'pff', 'prtrtrtrgurtrufnasutututut', 'prrrt', 'PFFT!', 'PHHhhhh...', 'SPLPLPLLLP', 'WHOooooffff', 'poot', 'prrrrrrrvt', 'scraeft', 'ppppppwwarrrrppppp', 'pllllllllllllllllllllllllloooooooooooaaa...', 'RRRRRRRIIIIIIIIIIIIIIIIIIIIIIIIIPPPPP', 'fuuuuuuuuuuuurrrrrrrt', 'hhhppbbbb', 'verrrrrrrrrnnnnnntttttt', 'hooooooooooooooooooooooooonk', 'pbpbpbpbp', 'frr frr frrrrrr rampooooooooo ag', 'pppppppptttttttttttttttttttttttt', 'flurpppppppppppppppppppppppppppppppppppp', 'poot', 'Pprrpffrrppfff', 'Plappppt', 'Pthbbbbt', 'Thzzdt', 'Flarpt', 'Fwint', 'Plunt', 'ffffppbbttbbbt']

counter = 10000
while counter > 0:
	thisFart = ""
	thisFart += random.choice(['b','t','p','p','f','f','f','w']) * random.choice([1,1,1,1,2,2,2,3,5,7])
	thisFart += random.choice(['a','a','u','o','','','','']) * random.choice([1,1,1,2,2,2,2,2,4])
	thisFart += random.choice(['r','p','h','l']) * random.choice([1,1,1,1,2,2,2,2,3,4,5])
	thisFart += random.choice(farts)
	thisFart += random.choice(['r','p','h','l']) * random.choice([1,1,1,1,1,2,2,2,3,3,4,5])
	thisFart += random.choice(['a','a','u','o','','','','']) * random.choice([1,1,1,1,1,2,2,2,3,4])
	thisFart += random.choice(['b','t','p','p','f','f','f','w']) * random.choice([2,3,5,7])

	outFart.write(thisFart)
	if counter != 1:
		outFart.write('\n')
	print thisFart
	counter = counter - 1