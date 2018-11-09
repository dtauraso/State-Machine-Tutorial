import hierarchial_context_sensitive_state_machine.hierarchial_context_sensitive_state_machine as hcssm

from collections import OrderedDict as od




def returnTrue(node, var_store):
	return True
def isLeftParenthesis(node, var_store):

	if isCharacter(node, var_store, '('):
		var_store['i'] += 1
		return True
	return False

def isRightParenthesis(node, var_store):


	if isCharacter(node, var_store, ')'):
		var_store['i'] += 1
		return True
	return False

def isNumber(node, var_store):

	i = var_store['i']
	input_ = var_store['input']
	if i >= len(input_):
		return False
	collected_digit = ''
	if (input_[i] != '(' and input_[i] != ')'):



		while i < len(input_) and (input_[i] >= '0' and input_[i] <= '9'):
			#print(input_[i])
			collected_digit += input_[i]
			i += 1
			#print(input_[i])

		if len(collected_digit) <= 0:
			return False
			#print(collected_digit)
		else:
			var_store['number'] = collected_digit

		var_store['i'] = i
		return True
	return False

def notWordNotNumber(node, var_store):
	return not isWord(node, var_store) and not isNumber(node, var_store)

def isCharacter(node, var_store, character):
	i = var_store['i']
	input_ = var_store['input']
	if i >= len(input_):
		return False
	return input_[i] == character

def printIthInputValue(node, var_store):
	i = var_store['i']
	input_ = var_store['input']
	print(input_[i])
def isAsterisk(node, var_store):

	#printIthInputValue(node, var_store)
	if isCharacter(node, var_store, '*'):
		var_store['i'] += 1
		return True

	return False

def isAmpersand(node, var_store):
	#printIthInputValue(node, var_store)

	if isCharacter(node, var_store, '&'):
		var_store['i'] += 1
		return True
	return False

def findSumOfDigitsInNumber(node, var_store):

	number = var_store['number']

	sum = 0
	for i in number:
		sum += int(i)

	print(sum)
	return True
parents = {

	# only the parent

	'(' : {'0':{}},
	')' : {'0':{}},
	'stuff' : {'0':{}},

	'*' : {'0':{'stuff': '0'},'1':{}},
	'#' : {'0':{}},
	'&' : {'0':{}},

	'sum_of_digits_in_number' : {'0':{}}
}


# sequences: ( * # & * ); where # is any integer
vars = {
	# update input
	# make a testing loop
	'input' : '(*3456&*)', # '(Im_a_word56)'
	'i' : 0,

	'number' : '',

	'parents' : parents,

	# this control graph uses string for states and cases
	'node_graph2' : [


		# current state -> [current_context [list of (next_state, next_context)]]

		#text template:

		#[	'name', [
		#	['next', [['0', [ <next state would be here> ]]]],
		#	['children',  [['0', [ <child would be here> ]]]],
		#	['functions', [['0', returnTrue ]]]]],
		# <child case would be here> = [ 'child_string_1', 'child_string_2']
		# <next state would be here> = [ 'next_state_string_1', 'next_state_string_2']

		# the style of choosing which next (state, case) to run is done using the if elif else style
		# if
		# elif
		# elif
		# else

		# next states are these ['(','0'], [')','0'], ['error', '0']


		['(' , [
			['next', [['0', [ ['stuff', '0'] ]]]],
			['children',  [['0', [  ]]]],
			['functions', [['0', isLeftParenthesis ]]]]],

		['stuff', [
			['next', [['0', [ [')','0'] ]]]],
			['children',  [['0', [ ['*', '0'] ]]]],
			['functions', [['0', returnTrue ]]]]],

			['*', [
				['next', [['0', [ ['#', '0'] ]], ['1', [  ]]]],
				['children',  [['0', [  ] ], ['1', []] ]],
				['functions', [['0', isAsterisk ], ['1', isAsterisk]]]]],
			['#', [
				['next', [['0', [ ['&', '0'] ]] ]],
				['children',  [['0', [  ]] ]],
				['functions', [['0', isNumber ] ]]]],

			['&', [
				['next', [['0', [ ['*', '1'] ]]]],
				['children',  [['0', [  ]]]],
				['functions', [['0', isAmpersand ]]]]],

		[')' , [
			['next', [['0', [ ['sum_of_digits_in_number','0'] ]]]],
			['children',  [['0', []]]],
			['functions', [['0', isRightParenthesis ]]]]],

		['sum_of_digits_in_number', [
			['next', [['0', []]]],
			['children',  [['0', []]]],
			['functions', [['0', findSumOfDigitsInNumber ]]]]]


		]
	}

hcssm.visit(['(', '0'], vars, 0, True)
# these are things you can do with state machines with some things you may have seen from ravi's class
# a^nb^n where n >= 1
# using this make one that looks like this a^nb^nc^n where n >= 1
# see if you can extend this to a^n....
# need a primary counter and a secondary counter that you can reset each round

print('done w machine')
