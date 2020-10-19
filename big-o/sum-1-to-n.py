import argparse
from timeit import default_timer as timer
import sys


def parse_my_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--num', required=True, type=int, help="Enter 'n' to find the sum of n natural numbers")
	parser.add_argument('--rec',default=False, type=str2bool, help="Enter True to use a recursive algorithm")
	args = parser.parse_args()
	return args


def str2bool(value):
	if value.lower() == "true":
		return True
	elif value.lower()== "false":
		return False
	else:
		raise argparse.ArgumentTypeError('Enter a valid boolean for \'rec\' arg')

def sum_1_to_n(n, rec=False, cnt=0):
	if rec:
		if n==0:
			print('Num times recursed:',cnt)
			return 0
		else:
			# cnt += 1
			# print('Curr n is {} and cnt is {}'.format(n,cnt))
			# print(cnt)
			return n + sum_1_to_n(n-1,rec=True)
	else:
		return n*(n+1)/2

def validate_n(n):
	if n<0:
		raise argparse.ArgumentTypeError("Enter a positive integer (natural number)")

def main():
	args = parse_my_args()
	start = timer()
	validate_n(args.num)
	args.rec = bool(args.rec)
	print(args.rec)
	# print('REc arg:',type(args.rec), args.rec, args.rec==True)
	prev_rec_limit=sys.getrecursionlimit()
	print('Prev rec limit:',prev_rec_limit)
	if(args.num>prev_rec_limit):
		sys.setrecursionlimit(args.num*10)
		print('New rec limit:',sys.getrecursionlimit())
	print('The sum is ',sum_1_to_n(args.num, args.rec))
	sys.setrecursionlimit(prev_rec_limit)
	end = timer()

	print('Used {} algorithm'.format('Recursive' if args.rec==True else 'Non-Recursive'))
	print('Took {} seconds... '.format(end-start))


if __name__=="__main__":
	main()