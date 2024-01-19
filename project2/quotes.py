import requests
import json

# class here for practice 
class FavQuotesInterpreter:
    def __init__(self):
        # api site and token
        self.url = 'https://favqs.com/api/' 
        self.auth = 'Token token="b35a811f370be0add8fb856670c711fa"'
    
    def get_qotd(self): # quote of the day 
        response = requests.get(self.url+'qotd', headers={'Authorization': self.auth})
        return response.json() 

    def get_quote_by_keyword(self, page_num, keyword):
        response = requests.get(self.url+'quotes', 
        headers={'Authorization': self.auth},
        params={
            'page': page_num,
            'filter': keyword
        })

        return response.json() 

    def print_response(self, data, resp_type):  # the 2 responses have different JSON structures so need resp_type
        output = []
        if resp_type == 'qotd': 
            output.append(f'\n\t"{data["quote"]["body"]}"\n\t\t--{data["quote"]["author"]}\n') # if qotd format quote and return
        elif resp_type == 'keyword_search':
            for quote in data["quotes"]:
                output.append(f'\n\t"{quote["body"]}"\n\t\t--{quote["author"]}\n') # if search, format then append to output list
        return output 
    
    def search_prompt(self):
        keyword = input('What keyword are you searching by?: ')
        pg_num = 1 # start on the first page of results
        pg_turn = ''

        while True: 
            pg_data = self.get_quote_by_keyword(pg_num, keyword)  # make the query 
            class_resp = self.print_response(pg_data, 'keyword_search') # format 
            for i in range(len(class_resp)):
                print(str(class_resp[i])) # convert to string

            # here we change what we print out for all use cases to make it more intuitive to navigate and prevent user input error
            if pg_data['last_page'] == False and pg_num > 1: # any middle page
                print(f'You are on page {pg_num}')
                pg_turn = input(r'Enter "next", "prev", or "exit" to navigate: ')
            elif pg_data['last_page'] == False and pg_num == 1: # the First page
                print(f'You are on page {pg_num}')
                pg_turn = input(r'Enter "next" or "exit" to navigate: ')
            elif pg_data['last_page'] == True and pg_num == 1: # the First AND Last Page
                print(f'You are on the only page with results')
                pg_turn = input(r'Enter "exit" to exit to main menu: ')
            elif pg_data['last_page'] == True: # The Last page
                print(f'You are on page {pg_num} of {pg_num}')
                pg_turn = input(r'Enter "prev" or "exit" to navigate: ')
                
            pg_turn = str(pg_turn)
            pg_turn.lower()

            if pg_turn == 'next': # if user wants next page
                if pg_data['last_page'] == True: # AND its the last page
                    print('invalid input') # it's invalid
                else: # NOT the last page
                    pg_num += 1 # go to next page
                    continue 
            elif pg_turn == 'prev': # if the user wants to go back
                if pg_num == 1: # AND user on 1st page
                    print('invalid input') # invalid
                else: # AND its past page 1
                    pg_num -= 1 # move back a page
                    continue 
            elif pg_turn == 'exit': # If user wants to exit
                break 
            else: # Catchall invalid inputs
                print('invalid input')

def main():
    quotes = FavQuotesInterpreter() # Create local version of class

    # loop for input
    while True:
        # Specifiy user's choice and format their response into a string
        user_choice = input(r'Enter "qotd" for the quote of the day, "search" to search via keyword, or "exit" for exiting the app: ') 
        user_choice = str(user_choice)
        user_choice.lower()

        if user_choice == 'qotd': # IF they want the quote of the day
            class_resp = quotes.print_response(quotes.get_qotd(), 'qotd') # get quote and print
            print(str(class_resp[0])) # Format response 
        elif user_choice == 'search': # IF they want to search 
            quotes.search_prompt() # run the search prompt
            continue 
        elif user_choice == 'exit': # IF they want to exit
            print('Goodbye!') # Say Adios!
            break
        else: # Catchall for any other invalid input
            print('invalid input')

if __name__ == "__main__":
    main()
