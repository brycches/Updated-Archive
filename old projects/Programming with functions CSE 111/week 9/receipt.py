import csv
print("Inkom Emporium")
import random
import datetime
from datetime import datetime

current_date_and_time = datetime.now()
current_day = current_date_and_time.weekday()
current_time = current_date_and_time.time()
eleven_am = datetime.strptime("11:15:00", "%H:%M:%S").time()

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
    filename: the name of the CSV file to read.
    key_column_index: the index of the column
    to use as the keys in the dictionary.
    Return: a compound dictionary that contains
    the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader, None)

        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
    return dictionary

def get_coupon():
    try:
        products_dict = read_dictionary("products.csv", 0)
    except FileNotFoundError as not_found_error:
        print(f"error, products.csv not found", not_found_error)
    except PermissionError as permission_error:
        print("permission error", permission_error)
    except Exception as error:
        print(f"there was an error", error)
    list_reader = []
    try:
        with open("request.csv", "rt") as csv_file:

                reader = csv.reader(csv_file)

                next(reader, None)
                for line in reader:
                    list_reader.append(line)
                length = len(list_reader)
                random_thing = random.randint(0, length-1)
                line = list_reader[random_thing]
                coupon = line[0]
                line2 = products_dict[coupon]
                product = line2[1]
                return f"Congradulations, you have recieved a coupon for 10% off {product} on your next visit!"
    except FileNotFoundError as not_found_error:
        print(f"error, request.csv not found", not_found_error)
    except PermissionError as permission_error:
        print("permission error", permission_error)
    except Exception as error:
        print(f"there was an error", error)





def main():
    try:
        total_items = 0
        subtotal = 0
        try:
            products_dict = read_dictionary("products.csv", 0)
        except FileNotFoundError as not_found_error:
            print(f"error, products.csv not found", not_found_error)
        except PermissionError as permission_error:
            print("permission error", permission_error)
        except Exception as error:
            print(f"there was an error", error)
        

        print(products_dict)
        
        with open("request.csv", "rt") as csv_file:

            reader = csv.reader(csv_file)

            next(reader, None)

            print("Your order: ")
            for line in reader:
                wanted = line[0]
                quantity = int(line[1])
                row = products_dict[wanted]
                print(f'{row[1]}: {quantity} @ {float(row[2]):.2f} = {(float(row[2])*quantity):.2f}')
                total_items += quantity
                subtotal += float(row[2])*quantity

            print(f"total items: {total_items}")
            print(f'subtotal {subtotal:.2f}')
            tax = subtotal * .06
            print(f"tax: {tax:.2f}")
            if current_day == 1 or current_day == 2 or current_time < eleven_am:
                discount = .1
                total = subtotal * 1.06 * discount
            else:
                total = subtotal * 1.06
            print(f"total: {total:.2f}")
            print("Thank you for shopping at the Inkom Emporium.")
            print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")
            print(f"Please enjoy this coupon for your next purchase:\n{get_coupon()}")
            print(f"Please take some time to fill out our online survey found at InkomEmporium.com\nYour unique customer ID is {random.randint(0, 9999999)}")

    except KeyError as key_error:
        print(f"You have an item that doesn't exist in your cart, we are unable to determine what {wanted} is", key_error)
    except FileNotFoundError as not_found_error:
        print(f"error, request.csv not found", not_found_error)
    except PermissionError as permission_error:
        print("permission error", permission_error)
    except Exception as error:
        print(f"there was an error", error)


if __name__ == "__main__":
    main()