import random

main_ticket = []
count = 0

while count < 12:
    ticket = random.randint(0, 100)
    if ticket not in main_ticket:
        main_ticket.append(ticket)
        count += 1

# Print the main_ticket list all 12 unique numbers
for number in main_ticket:
    print(number, end=" ")
