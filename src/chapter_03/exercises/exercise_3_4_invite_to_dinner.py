# Created Time: 2026/07/09
# Author: sunshinesDL (sunshinesDL@163.com)

"""Send out invitations for dinner to individuals listed."""


invitation_list = ["Mom", "Dad", "Teacher Lou"]

def send_invitations(personnel_list: list[str]) -> None:
    for person in personnel_list:
        print(f"{person}, I'd like to invite you for dinner. ")


send_invitations(invitation_list)
print('-' * 20)

print("However, Teacher Lou can't come.")
invitation_list[-1] = "Teacher Lu"
send_invitations(invitation_list)

