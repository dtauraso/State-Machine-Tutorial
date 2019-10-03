import sys
sys.path.insert(1, '/Users/David/Documents/github/hierarchial_context_sensitive_state_machine')
import hierarchial_context_sensitive_state_machine as hcssm

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

def isWord(node, var_store):


	i = var_store['i']
	input_ = var_store['input']
	if i >= len(input_):
		return False
	letter = ''
	if (input_[i] != '(' and input_[i] != ')'):
		#print(input_[i])
		# this will determine a letter
		while i < len(input_) and ((input_[i] >= 'A' and input_[i] <= 'Z') or (input_[i] >= 'a' and input_[i] <= 'z') or input_[i] == '_' ):

			letter += input_[i]
			i += 1
			#print(input_[i])
		if len(letter) > 0:
			print(letter)

			var_store['i'] = i
			return True
	return False

def isNumber(node, var_store):

	i = var_store['i']
	input_ = var_store['input']
	if i >= len(input_):
		return False
	collected_digit = ''
	if (input_[i] != '(' and input_[i] != ')'):



		if i < len(input_) and (input_[i] >= '0' and input_[i] <= '9'):

			collected_digit += input_[i]
			i += 1
		if len(collected_digit) > 0:
			print(collected_digit)

			var_store['i'] = i
			return True
	return False

def isCharacter(node, var_store, character):
	i = var_store['i']
	input_ = var_store['input']
	if i >= len(input_):
		return False
	return input_[i] == character

def notWordNotNumber(node, var_store):
	return not isWord(node, var_store) and not isNumber(node, var_store)





vars = {
	'input' : '(Im_a_word55)',
	'i' : 0,


	# this control graph uses string for the state names
	'node_graph2' : [



		#text template:

		#['first_name', [
		#	['next', [['second_name', [ <next state would be here> ]]]],
		#	['children',  [['second_name', [ <child would be here> ]]]],
		#	['functions', [['second_name', returnTrue ]]],
		# 	['parents',   [['second_name', [ <child would be here> ]]]]
		#   ]]],
		# <child would look like this> = [ 'child_state_first_name', 'child_state_second_name']
		# <next state would look like this> = [ 'next_state_first_name', 'next_state_second_name']

		# the style of choosing which next (state, case) to run is done using the if elif else style
		# if
		# elif
		# elif
		# else

		# here is an example of next states with a first name and a second name
		# ['(','0'], [')','0'], ['error', '0']


		['(' , [
			['next', [['0', [ ['letters_and_digits', '0'] ]]]],
			['children',  [['0', [  ]]]],
			['functions', [['0', isLeftParenthesis ]]],
			['parents', [['0', [ ]  ] ]]
			]],

		['letters_and_digits', [
			['next', [['0', [ [')','0'] ]]]],
			['children',  [['0', [ ['letters', '0'], ['digit', '0'], ['No letters and no digits', '0'] ]]]],
			['functions', [['0', returnTrue ]]],
			['parents', [['0', [ ]  ] ]]
			]],

			# the indent from letters_and_digits to letters means we are inside a lower level
			['letters', [
				['next', [['0', [ ['digit', '1'] ]], ['1', [ ['digit', '3']  ]]]],
				['children',  [['0', [  ]], ['1', []] ]],
				['functions', [['0', isWord ], ['1', isWord]]],
				['parents', [['0', [ ['letters_and_digits', '0'] ]  ], ['1', []] ]]
				]],
			['digit', [
				['next', [['0', [ ['letters', '1'] ]],    ['1', [ ['digit', '2']  ]], ['2', [ ]], ['3', [ ]] ]],
				['children',  [['0', [  ]], ['1', []], ['2', []], ['3', []] ]],
				['functions', [['0', isNumber ], ['1', isNumber], ['2', isNumber], ['3', isNumber] ]],
				['parents', [['0', [ ['letters_and_digits', '0'] ]  ], ['1', []], ['2', []], ['3', []] ]]
				]],

			# this is an end state cause there are no next states
			['No letters and no digits', [
				['next', [['0', [   ]]]],
				['children',  [['0', [  ]]]],
				['functions', [['0', notWordNotNumber ]]],
				['parents', [['0', [ ['letters_and_digits', '0'] ]  ] ]]
				]],


		[')' , [
			['next', [['0', [ ['end','0'] ]]]],
			['children',  [['0', []]]],
			['functions', [['0', isRightParenthesis ]]],
			['parents', [['0', [ ]  ] ]]
			]],

			# this is an end state cause there are no next states
		['end', [
			['next', [['0', []]]],
			['children',  [['0', []]]],
			['functions', [['0', returnTrue ]]],
			['parents', [['0', [ ]  ] ]]
			]]


		]
	}

'''
example of planning out the states before you actually add them in
'''

#hcssm.visit(['(', '0'], vars, 0, True)
#
'''
(word##)
(#word#)
()

(Im_a_word5)
(Im_a_word56)
(4Im_a_word5)
()
'''
fails_list = ['(Im_a_word5)', '(Im_a_word)', '(Im8_a_word)', ')Im8_a_word(']
print("fails")
for test in fails_list:
	vars['input'] = test
	vars['i'] = 0
	print("start")
	hcssm.visit(['(', '0'], vars, 0, True)
	print("end")
	print()

pass_list = ['(Im_a_word56)', '(4Im_a_word5)', '()']
print("passes")
for test in pass_list:
	vars['input'] = test
	vars['i'] = 0
	print("start")
	hcssm.visit(['(', '0'], vars, 0, True)
	print("end")
	print()
print('done w machine')
