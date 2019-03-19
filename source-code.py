from decimal import *

# set desired precision
# 1000 is chosen
getcontext().prec = 1000

# the actual value of pi
# obtained from http://www.math.com/tables/constants/pi.htm
actual_pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989'


# the formula of pi by F. Bellard
# obtained from https://bellard.org/pi/
# this is only the expression inside the sigma notation
# and the constant, rearranged based on the identity
# of a summation

pi_bellard = lambda n: (
# the constant
    (
        Decimal(1)
      / (
            Decimal(2) ** Decimal(6)
        )
    ) 
    *
# the expression inside the sigma notation
    (
        (Decimal(-1) ** Decimal(n))
      / (Decimal( 2) ** Decimal(Decimal(10) * Decimal(n)))
    )
    *
    (0
      - (
            (Decimal(2) ** Decimal(5))
          / (Decimal(4) * Decimal(n) + Decimal(1))
        )
      - (
            (Decimal(1))
          / (Decimal(4) * Decimal(n) + Decimal(3))
        )
      + (
            (Decimal(2) ** Decimal(8))
          / (Decimal(10) * Decimal(n) + Decimal(1))
        )
      - (
            (Decimal(2) ** Decimal(6))
          / (Decimal(10) * Decimal(n) + Decimal(3))
        )
      - (
            (Decimal(2) ** Decimal(2))
          / (Decimal(10) * Decimal(n) + Decimal(5))
        )
      - (
            (Decimal(2) ** Decimal(2))
          / (Decimal(10) * Decimal(n) + Decimal(7))
        )
      + (
            (Decimal(1))
          / (Decimal(10) * Decimal(n) + Decimal(9))
        )
    )
)

# n_range is the range of n for the summation
# through trial and error, you can find the
# threshold where the higher the value will
# not increase the precision of the
# calculation anymore. usually the number of
# precision set from getcontext.prec is 
# enough to get the value passing the
# threshold
n_range = range(1000)

# perform a summation and conversion to string
# so that we can compare character by character
# between the actual pi and the calculated pi
calculated_pi = str(sum([pi_bellard(n) for n in n_range]))

# a simple function to do the comparison
def find_mismatch(str_1, str_2):
    # choose shorter length of string to perform the comparison
    length = len(str_1) if len(str_1) < len(str_2) else len(str_2)
    
    # perform comparison character by character
    for i in range(length):
        # if there is a mismatch of character, indicate the index
        if(str_1[i] != str_2[i]):
            return 'Mismatch at ' + str(i)
    #if there is no mismatch, indicate the first number of characters where they are similar
    return 'Two strings are matching for the first ' + str(length) + ' characters'

print(find_mismatch(actual_pi, calculated_pi))
