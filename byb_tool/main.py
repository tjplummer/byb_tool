import gzip, sys, os, argparse
from enum import Enum


class BatThrow(Enum):
   BothRight = "AB"
   BothLeft = "AC"
   BatBothThrowLeft = "AD"
   BatRightThrowLeft = "AG"
   BatLeftThrowRight = "AI"
   BatBothThrowRight = "AM"

   def __str__(self):
       return str(self.value)

class Endurance(Enum):
    Least = "AB"
    Infinite = "JG"

    def __str__(self):
        return str(self.value)

class Appearance(Enum):
    MWhiteRound = "AB"
    MWhiteFlat = "AC"
    MBlackRound = "AD"
    MBlackFlat = "AE"
    MBrownRound = "AF"
    MBrownFlat = "AG"
    WWhitePigTail = "AH"
    WWhiteLong = "AI"
    WBlackPigTail = "AJ"
    WBlackLong = "AK"
    WBrownPigTail = "AL"
    WBrownLong = "AM"

    def __str__(self):
        return str(self.value)

class Stadium(Enum):
    DirtYards = 0
    PlaygroundCommons = 1
    CementGardens = 2
    EckmanAcres = 3
    BigCityStadium = 4
    SuperColossalDome = 5
    SteeleStadium = 6
    TinCanAlley = 7
    ParksDepartmentFieldNo2 = 8
    SandyFlats = 9

    def __str__(self):
        return str(self.value)

class Innings(Enum):
    six = 12
    nine = 18

class AlphaNum:
    CA = " "
    CB = "!"
    CC = "\""
    CD = "#"
    CE = "$"
    CF = "%"
    CG = "&"
    CH = "'"
    CI = "("
    CJ = ")"
    CK = "*"
    CL = "+"
    CM = ","
    CN = "-"
    CO = "."
    CP = "/"
    DA = 0
    DB = 1
    DC = 2
    DD = 3
    DE = 4
    DF = 5
    DG = 6
    DH = 7
    DI = 8
    DJ = 9
    DK = " ="
    DL = ";"
    DM = "<"
    DN = "="
    DO = ">"
    DP = "?"
    EA = "@"
    EB = "A"
    EC = "B"
    ED = "C"
    EE = "D"
    EF = "E"
    EG = "F"
    EH = "G"
    EI = "H"
    EJ = "I"
    EK = "J"
    EL = "K"
    EM = "L"
    EN = "M"
    EO = "N"
    EP = "O"
    FA = "P"
    FB = "Q"
    FC = "R"
    FD = "S"
    FE = "T"
    FF = "U"
    FG = "V"
    FH = "W"
    FI = "X"
    FJ = "Y"
    FK = "Z"
    FL = "["
    FM = "\\"
    FN = "]"
    FO = "^"
    FP = "_"
    GA = "~"

    @staticmethod
    def get_key_by_val(val: str):
        h = vars(AlphaNum)
        for item in h:
            if h[item] == val:
                return item

    @staticmethod
    def rename(val: str):
        nn = ""

        for n in val.upper():
            c = AlphaNum.get_key_by_val(n)
            nn = nn + c

        if len(nn) < 42:
            for i in range(42 - len(nn)):
                nn = nn + "A"

        return nn

class StatRatings:
    AA = 0
    AB = 1
    AC = 2
    AD = 3
    AE = 4
    AF = 5
    AG = 6
    AH = 7
    AI = 8
    AJ = 9
    AK = 10
    AL = 11
    AM = 12
    AN = 13
    AO = 14
    AP = 15
    BA = 16
    BB = 17
    BC = 18
    BD = 19
    BE = 20
    BF = 21
    BG = 22
    BH = 23
    BI = 24
    BJ = 25
    BK = 26
    BL = 27
    BM = 28
    BN = 29
    BO = 30
    BP = 31
    CA = 32
    CB = 33
    CC = 34
    CD = 35
    CE = 36
    CF = 37
    CG = 38
    CH = 39
    CI = 40
    CJ = 41
    CK = 42
    CL = 43
    CM = 44
    CN = 45
    CO = 46
    CP = 47
    DA = 48
    DB = 49
    DC = 50
    DD = 51
    DE = 52
    DF = 53
    DG = 54
    DH = 55
    DI = 56
    DJ = 57
    DK = 58
    DL = 59
    DM = 60
    DN = 61
    DO = 62
    DP = 63
    EA = 64
    EB = 65
    EC = 66
    ED = 67
    EE = 68
    EF = 69
    EG = 70
    EH = 71
    EI = 72
    EJ = 73
    EK = 74
    EL = 75
    EM = 76
    EN = 77
    EO = 78
    EP = 79
    FA = 80
    FB = 81
    FC = 82
    FD = 83
    FE = 84
    FF = 85
    FG = 86
    FH = 87
    FI = 88
    FJ = 89
    FK = 90
    FL = 91
    FM = 92
    FN = 93
    FO = 94
    FP = 95
    GA = 96
    GB = 97
    GC = 98
    GD = 99
    GE = 100
    GF = 101
    GG = 102
    GH = 103
    GI = 104
    GJ = 105
    GK = 106
    GL = 107
    GM = 108
    GN = 109
    GO = 110
    GP = 111
    HA = 112
    HB = 113
    HC = 114
    HD = 115
    HE = 116
    HF = 117
    HG = 118
    HH = 119
    HI = 120
    HJ = 121
    HK = 122
    HL = 123
    HM = 124
    HN = 125
    HO = 126
    HP = 127
    IA = 128
    IB = 129
    IC = 130
    ID = 131
    IE = 132
    IF = 133
    IG = 134
    IH = 135
    II = 136
    IJ = 137
    IK = 138
    IL = 139
    IM = 140
    IN = 141
    IO = 142
    IP = 143
    JA = 144
    JB = 145
    JC = 146
    JD = 147
    JE = 148
    JF = 149
    JG = 150
    JH = 151
    JI = 152
    JJ = 153
    JK = 154
    JL = 155
    JM = 156
    JN = 157
    JO = 158
    JP = 159

    @staticmethod
    def get_key_by_val(val: int):
        h = vars(StatRatings)
        for item in h:
            if h[item] == val:
                return item

class StatCategories:
    #DONOTCHANGE
    P1 = str
    #STAMINA
    P2 = str
    #THROW RELIABILITY
    P3 = str
    #REACTION
    P4 = str
    #SPEED
    P5 = str
    #THROWPOWER
    P6 = str
    #THROWACCURACY
    P7 = str
    #BATTINGPOWER
    P8 = str
    #BATTINGCONTACT
    P9 = str
    #BALLTRACKING
    P10 = str
    #UNKNOWN
    P11 = str
    #Appearance
    P12 = str
    #UNKNOWN
    P13 = str
    #BATS/THROWS
    P14 = str
    #FASTBALL
    P15 = str
    #SLOWBALL
    P16 = str
    #LEFTHOOK
    P17 = str
    #RIGHTHOOK
    P18 = str
    #SCREWBALL
    P19 = str
    #ZIGZAG
    P20 = str
    #BIGFREEZE
    P21 = str
    #FIREBALL
    P22 = str
    #SPITBALL
    P23 = str
    #CRAZYBALL
    P24 = str
    #SLOMO
    P25 = str
    #ELEVATOR
    P26 = str
    #BATTINGSTANCE
    P27 = str
    #HEIGHT
    #NOTE: THIS BASICALLY TELLS THE GAME HOW TALL THE STRIKE ZONE SHOULD BE AND HOW HIGH THE CAN REACH WITH THEIR GLOVE
    P28 = str
    #GENDER
    P29 = str
    #BIRTHDAYMONTH
    P30 = str
    #BIRTHDAYDAY
    P31 = str
    #BLOCK FOR UNKNOWN
    P32 = str
    P33 = str
    P34 = str
    P35 = str
    P36 = str
    #NICKNAME
    P37 = str

    def load_stats(self, d):
        val = d['custom']['backupstats0']
        x = 1
        for i in range(0, len(val), 2):
            chunk = val[i:i+2]
            setattr(self, f"P{x}", getattr(StatRatings, chunk))
            x += 1

    @staticmethod
    def save_stats(d, val):
        d['custom']['backupstats0'] = val

    def juggernaut(self):
        nochange = [1, 2, 12, 14, 11, 12, 13, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]

        for i in range(1, 37):
            if i not in nochange:
                setattr(self, f"P{i}", StatRatings.JP)

        self.max_endurance()

    def max_endurance(self):
        self.P2 = Endurance.Infinite.value

    def max_throwing(self):
        arr = [3, 6, 7 , 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

        for i in arr:
            setattr(self, f"P{arr[i]}", StatRatings.JP)

    def max_speed(self):
        self.P5 = StatRatings.JP

    def max_batting(self):
        self.P8 = StatRatings.JP
        self.P9 = StatRatings.JP
        self.P10 = StatRatings.JP

    def max_fielding(self):
        self.P4 = StatRatings.JP
        self.P10 = StatRatings.JP

    def switch_arms(self):
        if self.P14 == StatRatings.AB:
            self.P14 = StatRatings.AG
        elif self.P14 == StatRatings.AC:
            self.P14 = StatRatings.AI
        elif self.P14 == StatRatings.AD:
            self.P14 = StatRatings.AM
        elif self.P14 == StatRatings.AG:
            self.P14 = StatRatings.AB
        elif self.P14 == StatRatings.AI:
            self.P14 = StatRatings.AC
        else:
            self.P14 = StatRatings.AD

    def switch_sides(self):
        if self.P14 not in [StatRatings.AM, StatRatings.AD]:
            if self.P14 == StatRatings.AB:
                self.P14 = StatRatings.AI
            elif self.P14 == StatRatings.AC:
                self.P14 = StatRatings.AG
            elif self.P14 == StatRatings.AG:
                self.P14 = StatRatings.AC
            elif self.P14 == StatRatings.AI:
                self.P14 = StatRatings.AB

    def switch_hitter(self):
        if self.P14 not in [StatRatings.AM, StatRatings.AD]:
            if self.P14 in [StatRatings.AB, StatRatings.AI]:
                self.P14 = StatRatings.AM
            else:
                self.P14 = StatRatings.AD

    def compile(self):
        sb = ""
        h = vars(self)
        for item in h:
            var = StatRatings.get_key_by_val(h[item])
            if var is not None:
                sb += var
        return sb


def append_line(sb, val):
    return sb + val + "\n"

def import_file(file):
    f = gzip.open(file, mode="rb")
    uncompress = f.readlines()
    f.close()

    di = {}

    for line in uncompress:
        decode = line.decode()
        if decode[0] == "[":
            key = decode[1:-2]
            di[key] = {}
        else:
            lk = list(di)[-1]
            kv = decode.split("=")
            if len(kv) < 2:
                kv.append("")
            di[lk][kv[0]] = kv[1].strip()

    return di

def save_file(d, file):
    dp = os.path.dirname(file)
    fn = os.path.splitext(os.path.basename(file))[0]
    ext = os.path.splitext(os.path.basename(file))[1]
    os.rename(file, f"{dp}/{fn}.bak{ext}")

    sb = ""

    for k in d.keys():
        sb = append_line(sb, f"[{k}]")
        for v in d[k].keys():
            sb = append_line(sb, f"{v}={d[k][v]}")

    f = gzip.open(file, "wb")
    f.write(sb.encode())
    f.close()

def get_name(di):
    og_name = di['custom']['names0']
    translated = ""
    for i in range(0, len(og_name), 2):
        chunk = og_name[i:i+2]
        if chunk != 'AA':
            char = getattr(AlphaNum(), og_name[i:i+2])
            translated = translated + char

    return translated

def is_gz_file(filepath):
    with open(filepath, 'rb') as test_f:
        return test_f.read(2) == b'\x1f\x8b'

def add_parse_arguments():
    parse = argparse.ArgumentParser(description="This is a program to edit Backyard Baseball 2001 save files. By default, this backs up current save file")

    parse.add_argument("--f", dest="file", metavar="file", required=True, type=str, help="path to valid c0# file created for team saves")
    parse.add_argument("--j", action="store_true", help="make custom player maxed out")
    parse.add_argument("--sh", action="store_true", help="make custom player a switch hitter")
    parse.add_argument("--sb", action="store_true", help="make custom player throw with the other arm")
    parse.add_argument("--st", action="store_true", help="make custom player throw with the other arm")
    parse.add_argument("--msp", action="store_true", help="max customer players speed")
    parse.add_argument("--mb", action="store_true", help="max customer players batting")
    parse.add_argument("--mt", action="store_true", help="max customer players throwing")
    parse.add_argument("--mf", action="store_true", help="max customer players fielding")
    parse.add_argument("--dbo", action="store_true", help="change default batting stance to open")
    parse.add_argument("--dbc", action="store_true", help="change default batting stance to closed")
    parse.add_argument("--dbs", action="store_true", help="change default batting stance to square")
    parse.add_argument("--cn", dest="name", metavar="name", type=str, help="change name for custom player. MAX of 21 characters COUNTING whitespace")

    return parse.parse_args()


def main():
    args = add_parse_arguments()
    sc = StatCategories()

    if not os.path.isfile(args.file):
        sys.exit("Not a valid filepath given.. Exiting!")

    if not is_gz_file(args.file):
        sys.exit("{fp} - This file is not gzip compressed or saved uncompressed in general. Use a fresh file.. Exiting!")

    if args.name is not None:
        if len(args.name) > 21:
            sys.exit("Change name - too many characters. It must be 21 or less characters including whitespace.. Exiting!")

    #rename to something that means something
    d = import_file(args.file)

    sc.load_stats(d)

    if args.j is not None:
        sc.juggernaut()

    if args.j is None and args.msp is not None:
        sc.max_speed()

    if args.j is None and args.mb is not None:
        sc.max_batting()

    if args.j is None and args.mt is not None:
        sc.max_throwing()

    if args.j is None and args.mf is not None:
        sc.max_fielding()

    if args.st is not None:
        sc.switch_arms()

    if args.sb is not None:
        sc.switch_sides()

    if args.sh is not None:
        sc.switch_hitter()

    if args.name is not None:
        d['custom']['names0'] = AlphaNum.rename(args.name)

    sc.save_stats(d, sc.compile())

    save_file(d, args.file)


if __name__ == "__main__":
    main()