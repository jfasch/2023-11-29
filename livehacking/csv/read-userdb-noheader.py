import sys
import user_csv

if len(sys.argv) != 2:
    print('Usage:', sys.argv[0], 'FILENAME.csv')
    sys.exit(1)

for user in user_csv.read_csv_noheader(sys.argv[1]):
    user_csv.print_user(user)
