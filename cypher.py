# Quick explanation what the program does
print("This program uses a cyper to encode any message you give it.\n")

# Prompting message that user wants to encode
message = input("Please enter the message to encode:\t")



#Defining encode_message function with a single parameter message, which represents the message to be encoded.

def encode_message(message):
    encoded_message = ""  #The variable encoded_message which will store the encoded message is initialized as an empty string. 
    
    #The for loop to iterate over each character char in the input
    
    for char in message:
        if char.isalpha():  # Checking if the character is a letter / if not it moves to the else block
            ascii_val = ord(char)  # Geting the ASCII value of the character; it will be stored in ascii_val string
            if 'a' <= char <= 'z':  # Inner if statement is checking if the character is a lowercase letter /if not it moves to the inner else block
                
                # Variable encoded_ascii_val will store our encoded ASCII value
                # The difference between ascii_val and the ASCII value of 'a' (ord('a')) is calculated
                # to get the relative position of the character within the lowercase alphabet.
                # 15 is added to shift the letter by 15 positions in lowercase alphabet
                # Modulus operator % is used with 26 to handle the cyclical nature of the alphabet.
                # The result is added to the ASCII value of 'a' to obtain the encoded ASCII value.
                
                encoded_ascii_val = (ascii_val - ord('a') + 15) % 26 + ord('a')
            else:
                # taking the same steps from previous if statement but within uppercase alphabet 
                encoded_ascii_val = (ascii_val - ord('A') + 15) % 26 + ord('A') 
            encoded_char = chr(encoded_ascii_val)  # Converting the ASCII value back to a character
            
            # Adding encoded characters to our encoded message character by character
            encoded_message += encoded_char
        else:
            encoded_message += char  # Adding non-letter characters without any change to them
    return encoded_message



encoded_message = encode_message(message)

# Printing out encoded message
print("\nEncoded message:\t", encoded_message)