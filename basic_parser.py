import os


def get_local_user_id(user_id_dict, num_users, user):
    res = user_id_dict.get(user, None)
    if res is None:
        user_id_dict[user] = num_users[0]
        num_users[0] += 1
        return num_users[0] - 1
    return res


def parse(fname, num_users=None, user_id_dict=None):
    if num_users is None:
        num_users = [0] #in a list so that it is mutable
    if user_id_dict is None:
        user_id_dict = {}
        
    utc_lis = []
    users_lis = []
    with open(fname, 'r') as F:
        for line in F:
            utc, users = line.strip("\n").split(", ", 1) #without the "\n"
            utc = float(utc)
            users = users.split(", ")
            if users[0] == '':
                users = tuple()
            else:
                users = tuple(get_local_user_id(user_id_dict, num_users, user)
                              for user in users)

            utc_lis.append(utc)
            users_lis.append(users)
        
    return user_id_dict, utc_lis, users_lis


def parse_all(directory='/data', relative_path=True):
    """
    returns user_id_dict, and a list of
    (fname, utc_lis, users_lis)
    for all files in a directory.
    IDs are local numbers and aren't related to discord usernames or discord IDs
    
    if relative_path == True, assume the directory is
    (current_directory) + directory.
    The defauls arguments work fine if the script is in the same dir as main.py.
    """
    num_users = [0]
    user_id_dict = {}
    
    if relative_path:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        directory = dir_path + directory

    res_lis = []
    for file in os.listdir(directory):
        if file[-4:] == '.txt':
            res_lis.append(
                (file[:-4],) + 
                 parse(directory + "/" + file,
                       num_users,
                       user_id_dict)[1:]
            )
    return user_id_dict, res_lis
