def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def vowel_checker(name,i,code,prev_code,soundex):
   if ((name[i-1].upper() in ['A','E','I','O','U']) and code == prev_code):
        return True
   return False

def adjacent_checker(name,i,code,prev_code,soundex):
   if (code != '0' and code != prev_code):
      return True
   return False

def code_checker(name,i,code,prev_code,soundex):
    if ((vowel_checker(name,i,code,prev_code,soundex) == True) or (adjacent_checker(name,i,code,prev_code,soundex) == True)):
        soundex += code
        prev_code = code
    return soundex,prev_code

def soundex_generate(name):
    # Start with the first letter (capitalized)
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)

    i = 1
    while ((i < len(name)) and len(soundex)<4):
      code = get_soundex_code(name[i])
      soundex, prev_code = code_checker(name,i,code,prev_code,soundex)

      i+=1

    soundex = soundex.ljust(4, '0')

    return soundex

def generate_soundex(name=None):
    if (not name) or (name == None):
        return ""
    
    soundex = soundex_generate(name)

    return soundex
