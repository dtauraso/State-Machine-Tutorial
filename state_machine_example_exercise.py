import sys
sys.path.insert(1, '/Users/David/Documents/github/contextual-state-chart')
import contextual_state_chart as csc

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
	'input' : '',
	'i' : 0,


	# this control graph uses string for the state names
	'node_graph2' : [


		# current state -> [current_context [list of (next_state, next_context)]]

		#text template:

		#[	'name', [
		#	['next', [['0', [ <next state would be here> ]]]],
		#	['children',  [['0', [ <child would be here> ]]]],
		#	['functions', [['0', returnTrue ]]]]],
		# <child case would be here> = [ 'child_state', 'child_case']
		# <next state would be here> = [ 'next_state', 'next_state_case']

		# the style of choosing which next (state, case) to run is done using the if elif else style
		# if
		# elif
		# elif
		# else

		# next states are these ['(','0'], [')','0'], ['error', '0']

		# start state
		['(' , [
			['next', [['0', [ [ ] ]]]],
			['children',  [['0', [  ]]]],
			['functions', [['0', isLeftParenthesis ]]],
			['parents', [['0', [] ]]]

			]],

		['letters_and_digits', [
			['next', [['0', [ [ ] ]]]],
			['children',  [['0', [ [ ], [ ], [ ] ]]]],
			['functions', [['0', returnTrue ]]],
			['parents', [['0', [ ] ]]]

			]],


			['letters', [
				['next', [['0', [ [ ] ]], ['1', [ [ ]  ]], ['2', []]]],
				['children',  [['0', [  ]], ['1', []], ['2', []] ]],
				['functions', [['0', isWord ], ['1', isWord], ['2', isWord]]],
				['parents', [['0', [] ], ['1', [['letters_and_digits', '0']]], ['2', []] ]]
				]],
			['digit', [
				['next', [['0', [ [ ] ]],    ['1', [ [ ]  ]], ['2', [ ]], ['3', [[ ] ]], ['4', [[ ]]] ]],
				['children',  [['0', [  ]], ['1', []], ['2', []], ['3', []], ['4', []] ]],
				['functions', [['0', isNumber ], ['1', isNumber], ['2', isNumber], ['3', isNumber], ['4', isNumber] ]],
				['parents', [['0', [['letters_and_digits', '0']] ], ['1', []], ['2', []], ['3', []], ['4', []] ]] # the ones with empty lists these aren't in the dict
				]],

			['No letters and no digits', [
				['next', [['0', [   ]]]],
				['children',  [['0', [  ]]]],
				['functions', [['0', notWordNotNumber ]]],
				['parents', [['0', [['letters_and_digits', '0' ]] ]]]
				]],


		[')' , [
			['next', [['0', [ [ ] ]]]],
			['children',  [['0', []]]],
			['functions', [['0', isRightParenthesis ]]],
			['parents', [['0', [ ] ]]]
			]],

		# end state
		['end', [
			['next', [['0', []]]],
			['children',  [['0', []]]],
			['functions', [['0', returnTrue ]]],
			['parents', [['0', [ ] ]]]
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
	csc.visit(['(', '0'], vars, 0, True)
	print("end")
	print()

pass_list = ['(Im_a_word56more_letters)', '(4Im_a_word56)', '()']
print("passes")
for test in pass_list:
	vars['input'] = test
	vars['i'] = 0
	print(test)

	print("start")
	csc.visit(['(', '0'], vars, 0, True)
	print("end")
	print()
print('done w machine')
