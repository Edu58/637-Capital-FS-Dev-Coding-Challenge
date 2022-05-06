# Total balance of every individual
BALANCE = {'Wanjiru': 0.00, "Linda": 0.00, "Juma": 0.00}

# Opens the transactions.txt file and read the data
with open('transactions.txt', 'r') as transactions:
    read_data = transactions.readlines()

    # A list of lists of individual transactions.
    all_transactions_splitted = []

    # Loops through the data read from the txt file, converts each transaction
    # into a list and pushes it to the all_transactions list
    for transaction in read_data:
        one_transaction = transaction.split(":")
        all_transactions_splitted.append(one_transaction)

    # Loops through each transaction in the all_transactions_splitted list and takes actions
    # depending on the transaction type and individual
    for each in all_transactions_splitted:
        if each[0] == "DEPOSIT":
            if each[1] in BALANCE:
                total = float(BALANCE[each[1]]) + float(each[2])
                BALANCE[each[1]] = total
            else:
                pass

        elif each[0] == "WITHDRAW" and each[1] in BALANCE:
            # First checks if the amount is enough to withdraw. It prevents over-withdrawal
            if float(BALANCE[each[1]]) - float(each[2]) >= 0:
                total = float(BALANCE[each[1]]) - float(each[2])
                BALANCE[each[1]] = total
            else:
                pass

        elif each[0] == "TRANSFER":
            if each[1] in BALANCE and each[2] in BALANCE:
                # Checks if the balance of the person transferring the money is more
                # than the amount being transferred to avoid  over-withdrawal
                if float(BALANCE[each[1]]) - float(each[3]) >= 0:
                    BALANCE[each[1]] += float(BALANCE[each[1]]) - float(each[3])
                    BALANCE[each[2]] += float(BALANCE[each[2]]) + float(each[3])
            else:
                pass

    print(BALANCE)
