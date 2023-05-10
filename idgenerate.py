import random
import string

# Arrays can be used to make sure the same id/user isn't used twice

used_class_ids = []
used_teacher_ids = []
used_student_ids = []
used_users = []

# The words in these arrays will later be randomised to make usernames for students. More can be added later.

user_list_adj = ["Absolute", "Acrobatic", "Admirable", "Adored", "Adventurous", "Afraid", "Agile", "Amazing", "Amusing", "Ancient", "Angry", "Animated", "Anxious", "Artistic", "Athletic"]
user_list_noun = ["Actor", "Anchor", "Antagonist", "Apple", "Angel", "Army", "Astronaut"]

'''
def generate_class_id():
    chars = "".join((string.ascii_letters, string.digits))
    class_prefix = "cl"
    class_id = "".join(random.choice(chars) for _ in range(4))
    final_id = class_prefix + class_id
    while final_id in used_class_ids:
        class_id = "".join(random.choice(chars) for _ in range(4))
        final_id = class_prefix + class_id
    if final_id not in used_class_ids:
        used_class_ids.append(final_id)
    return final_id

def generate_teacher_id():
    chars = "".join((string.ascii_letters, string.digits))
    teacher_prefix = "tc"
    teacher_id = "".join(random.choice(chars) for _ in range(4))
    final_id = teacher_prefix + teacher_id
    while final_id in used_teacher_ids:
        teacher_id = "".join(random.choice(chars) for _ in range(4))
        final_id = teacher_prefix + teacher_id
    if final_id not in used_teacher_ids:
        used_teacher_ids.append(final_id)
    return final_id

def generate_student_id():
    chars = "".join((string.ascii_letters, string.digits))
    student_prefix = "st"
    student_id = "".join(random.choice(chars) for _ in range(4))
    final_id = student_prefix + student_id
    while final_id in used_student_ids:
        student_id = "".join(random.choice(chars) for _ in range(4))
        final_id = student_prefix + student_id
    if final_id not in used_student_ids:
        used_student_ids.append(final_id)
    return final_id
'''

'''Above I created three different functions to generate teacher, student and class ids. They need no parameters
and the respective function is simply called. However by introducing a new value called id_key, they can be
done with one function, as done below. In teacher accounts, id_key would be t and in student accounts it would be s.
Both approaches work fine however and can be used if this presents inconvenience.'''

def generate_any_id(id_key):
    chars = "".join((string.ascii_letters, string.digits))
    if id_key == "c":
        class_prefix = "cl"
        class_id = "".join(random.choice(chars) for _ in range(4))
        final_id = class_prefix + class_id
        while final_id in used_class_ids:
            class_id = "".join(random.choice(chars) for _ in range(4))
            final_id = class_prefix + class_id
        if final_id not in used_class_ids:
            used_class_ids.append(final_id)
        return final_id
    elif id_key == "t":
        teacher_prefix = "tc"
        teacher_id = "".join(random.choice(chars) for _ in range(4))
        final_id = teacher_prefix + teacher_id
        while final_id in used_teacher_ids:
            teacher_id = "".join(random.choice(chars) for _ in range(4))
            final_id = teacher_prefix + teacher_id
        if final_id not in used_teacher_ids:
            used_teacher_ids.append(final_id)
        return final_id
    elif id_key == "s":
        student_prefix = "st"
        student_id = "".join(random.choice(chars) for _ in range(4))
        final_id = student_prefix + student_id
        while final_id in used_student_ids:
            student_id = "".join(random.choice(chars) for _ in range(4))
            final_id = student_prefix + student_id
        if final_id not in used_student_ids:
            used_student_ids.append(final_id)
        return final_id


# This uses the random module to randomise selection from each word list then concatenates into a username.

def generate_user():
    final_user = random.choice(user_list_adj) + random.choice(user_list_noun)
    while final_user in used_users:
        final_user = random.choice(user_list_adj) + random.choice(user_list_noun)
    if final_user not in used_users:
        used_users.append(final_user)
    final_user = final_user
    return final_user

# This uses the teachers name and adds a number at the end if it's taken.

def generate_teacher_user(username, id):
    final_user = username[0:1]
    suffix_value = 1
    while final_user in used_users:
        final_user = username[0:1] + str(suffix_value)
        suffix_value = suffix_value + 1
    if final_user not in used_users:
        used_users.append(final_user)
    final_user = [id, final_user]
    return final_user

# The way we verify teachers is by checking the first two values of their id number.
# The generate_any_id function will have prefixed the tc onto the id number if id_key = t

def verify_teacher(id):
    if id[0:2] == "tc":
        return True
    else:
        return False
