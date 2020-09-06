# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure



def main():
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)
my_num = 
their_num = 
    for i in range(count_lines()):
        line = script.readline().rstrip('\n').split(" ")
        for word in line:
            try:
                message = client.messages \
                .create(
                     body=word,
                     from_=my_num,
                     to=their_num
                time.sleep(delay)
            except:
                print("You've hit a block.")
                 )

def count_lines(file='no_line_script.txt'):
    with open(file, 'r') as file:
        for index, line in enumerate(file):
            pass
    file.close()
    return index + 1

def remove_lines(original='mormon.txt', empty='no_line_script.txt'):
    script = open(original, 'r')
    empty_script = open(empty, 'w')
    script_length = count_lines(original)
    for i in range(script_length):
        line = script.readline()
        if line.replace(" ","") not in ['\n','\r\n']:
            empty_script.write(line)

if __name__ == '__main__':
    remove_lines()
    main()
 
