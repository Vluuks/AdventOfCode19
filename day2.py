from copy import deepcopy

def parse_intlist(ints):
  i = 0
  # iter over in steps of 4
  while True:
    opcode = ints[i]
    if opcode == 99:
      print("termination 99")
      break

    print('opcode ' + str(opcode))

    val1 = ints[ints[i+1]]
    val2 = ints[ints[i+2]]

    

    print(val1, val2)
    print("index" + str(ints[i+3]))

    if opcode == 1:
      ints[ints[i+3]] = val1 + val2
    elif opcode == 2:
      ints[ints[i+3]] = val1 * val2
    
    else:
      print("you fucked up")
      break 
    
    i += 4
    print(ints[i])

  print(i)
  print(ints)

def parse_intlist_reverse_engineering(ints):

  ints_initial = deepcopy(ints)

  # keep going until the output is the desired value
  for a in range(0, 100):
    for b in range(0, 100):

      print("combo {} {}".format(a, b))
      ints[1] = a
      ints[2] = b

      print(ints)

      # PARSE THE LIST
      i = 0
      while True:
        
        # get instruction
        opcode = ints[i]
        print('opcode ' + str(opcode))

        if opcode == 99:
          print("termination 99")
          break

        # get the values to parse
        val1 = ints[ints[i+1]]
        val2 = ints[ints[i+2]]

        print(val1, val2)
        print("index" + str(ints[i+3]))

        if opcode == 1:
          ints[ints[i+3]] = val1 + val2
        elif opcode == 2:
          ints[ints[i+3]] = val1 * val2
        
        # opcode is not 1, 2 or 99
        else:
          print("can never reach end of program")
          break 
        
        i += 4

      # every time we parsed a list, check if it mees requirement  
      if(ints[0] == 19690720):
        return (a, b)
      else:
        ints = deepcopy(ints_initial)
        print("SHOULD BE RESET")
        print(ints)

ints = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,1,23,13,27,2,6,27,31,1,5,31,35,2,10,35,39,1,6,39,43,1,13,43,47,2,47,6,51,1,51,5,55,1,55,6,59,2,59,10,63,1,63,6,67,2,67,10,71,1,71,9,75,2,75,10,79,1,79,5,83,2,10,83,87,1,87,6,91,2,9,91,95,1,95,5,99,1,5,99,103,1,103,10,107,1,9,107,111,1,6,111,115,1,115,5,119,1,10,119,123,2,6,123,127,2,127,6,131,1,131,2,135,1,10,135,0,99,2,0,14,0
]

arr_size = len(ints)
print(arr_size)

# parse_intlist(ints)

success = parse_intlist_reverse_engineering(ints)
print("WE ARE DONE FINALLY")
print(success)


