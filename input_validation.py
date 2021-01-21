def get_valid_float(input_message, error_message):
  valid_number_entered = False
  while not valid_number_entered:
    user_value = input(input_message)
    try: 
      float(user_value)
      valid_number_entered = True
    except:
      print(error_message)
  return float(user_value)

def get_valid_int(input_message, error_message):
  valid_number_entered = False
  while not valid_number_entered:
    user_value = input(input_message)
    try: 
      int(user_value)
      valid_number_entered = True
    except:
      print(error_message)
  return int(user_value)
