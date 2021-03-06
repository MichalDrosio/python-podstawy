# John keeps a backup of his old personal phone book as a text file.
# On each line of the file he can find the phone number
# (formated as +X-abc-def-ghij where X stands for one or two digits),
# the corresponding name between < and > and the address.
#
# Unfortunately everything is mixed, things are not always in the same order;
# parts of lines are cluttered with non-alpha-numeric characters (except inside phone number and name).
#
# Examples of John's phone book lines:
#
# "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n"
#
# " 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"
#
# "<Anastasia> +48-421-674-8974 Via Quirinal Roma\n"
#
# Could you help John with a program that, given the lines of his phone book and a phone number num returns
# a string for this number : "Phone => num, Name => name, Address => adress"
from re import sub


def phone(txt, num):
    if txt.count("+" + num) == 0:
        return "Error => Not found: " + num

    if txt.count("+" + num) > 1:
        return "Error => Too many people: " + num

    for line in txt.splitlines():
        if "+" + num in line:
            name = sub(".*<(.*)>.*", "\g<1>", line)
            line = sub("<" + name + ">|\+" + num, "", line)
            address = " ".join(sub("[^a-zA-Z0-9\.-]", " ", line).split())
            return "Phone => %s, Name => %s, Address => %s" % (num, name, address)






txt = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"
print(phone(txt,'1-541-754-3010'))
