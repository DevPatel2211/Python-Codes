# Convert number 0 to 19 to its equivalent words. E.g. 0 --> zero, 19 --> nineteen.

def words():
    num = int(input("Enter the number(0-19) :"))
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
             'eleven', 'twelve', 'thirteen', 'forteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    print(words[num])


words()
