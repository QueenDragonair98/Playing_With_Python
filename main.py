def decode(message_file):
    open_file = open(message_file, "r")
    file_contents = open_file.read()
    
    #Get all the numbers in the file
    nums_array = [int(i) for i in file_contents.split() if i.isdigit()]
    nums_array.sort()

    #Use those numbers to create a pyramid
    step = 1
    pyramid = []
    while len(nums_array) != 0:
        if len(nums_array) >= step:
            pyramid.append(nums_array[0:step])
            nums_array = nums_array[step:]
            step += 1
        else:
            return False
    

    #Use the pyramid to find the numbers for the secret message
    secret_numbers = []
    if(pyramid):
       for i in pyramid:
          secret_numbers.append(i[-1])

    #Build the secret message
    secret_message = ""
    file_contents_list = file_contents.split()

    for num in secret_numbers:
        for i in range(len(file_contents_list)):
            if file_contents_list[i] == str(num):
                secret_message = secret_message + file_contents_list[i + 1] + " "
            
    return secret_message

message = decode('./testFile.txt')
print(message)