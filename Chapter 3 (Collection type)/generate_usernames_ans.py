import sys
import collections

ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)
User = collections.namedtuple("User", "username forename middlename surname id")

def generate_username(fields, usernames):
    username = ((fields[FORENAME][0]+fields[MIDDLENAME][:1] + fields[SURNAME]).replace("-", "").replace("'", ""))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1
    usernames.add(username)
    return username

def process_line(line, usernames):
    fields = line.split(":")
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME], fields[SURNAME], fields[ID])
    return user

def print_users(users):
    namewidth = 17
    usernamewidth = 9
    pair = 0
    two_user = [None, None]

    for key in sorted(users):
        if(pair%128==0):
            print("{0:<{nw}} {1:^6} {2:{uw}}   {0:<{nw}} {1:^6} {2:{uw}}".format("Name", "ID", "Username", nw=namewidth, uw=usernamewidth))
            print("{0:-<{nw}} {0:-<6} {0:-<{uw}}   {0:-<{nw}} {0:-<6} {0:-<{uw}}".format("", nw=namewidth, uw=usernamewidth))


        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
        name = "{0.surname}, {0.forename}{1}".format(user, initial)
        two_user[pair%2] = {"name": name,
                            "user": user}
        pair += 1

        if(two_user[0] != None and two_user[1] != None):
            print("{0:.<{nw}} ({1.id:4}) {1.username:{uw}}   {2:.{nw}} ({3.id:4}) {3.username:{uw}}".format(
                two_user[0]["name"],  two_user[0]["user"], two_user[1]["name"],  two_user[1]["user"],
                nw=namewidth, uw=usernamewidth))
            two_user = [None, None]

    if (two_user[0] != None):
        print("{0:.{nw}} ({1.id:4}) {1.username:{uw}}".format(two_user[0]["name"], two_user[0]["user"], nw=namewidth, uw=usernamewidth))

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]]".format(sys.argv[0]))
        sys.exit()

    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        for line in open(filename, encoding="utf8"):
            line = line.rstrip()
            if line:
                user = process_line(line, usernames)
                users[(user.surname.lower(), user.forename.lower(), user.id)] = user
    print_users(users)

main()