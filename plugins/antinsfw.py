nsfw_keywords = {
    "general": [
        "se1x", "nud1e", "nake1d", "boo1bs", "ti1ts", "puss1y", "d1ick", "co1ck", "a1ss",
        "fu1ck", "blowjo1b", "c1um", "or1gasm", "she1male", "ero1tic", "mastur1bate", "ana1l",
        "hardc1ore", "bd1sm", "feti1sh", "l1inge1rie", "mi1lf", "ga1y", "les1bian",
        "three1some", "squir1ting", "bu1tt plu1g", "dil1do", "vibrat1or", "esc1ort", "hand1job",
        "stri1ptease", "ki1nky", "s1ex ta1pe", "sp1ank", "swi1nger", "tab1oo", "cumsh1ot",
        "deept1hroat", "domin1ation", "submi1ssion", "hand1cuffs", "or1gy", "roqlep1lay", "se1x to1y",
        "voye1ur", "cos1p1lay", "cul1ture", "p1orn1hwa",
        "netor1are", "ne1tori", "net1orase", "eroma1nga", "in1cest", "st1ep1mo1m", "s1tep1dad",
        "ste1psis1ter", "ste1pbr1other", "st1ep1son", "st1ep1daug1hter", "nt1r", "ga1ng1b1ang",
        "fac1ial", "gol1den sho1wer", "peg1gin1g", "ri1mmi1ng", "ro1ugh s1ex", "di1rty t1a1lk",
        "s1ex ch1at", "nu1de p1ic", "le1wd", "tit1ty", "twe1rk", "bre1asts", "pen1is", "va1gi1na",
        "cli1tor1is", "ge1nit1als", "se1x1ual", "kam1asut1ra", "inc1est", "pe1do", "ra1pe", "bon1d1age",
        "cu1m insi1de", "cre1am1pie", "se1x sla1ve", "se1x do1ll", "s1ex mac1hine", "lat1ex", "or1al s1ex",
        "bu1tt", "sl1ut", "wh1ore", "tra1mp", "ska1nk", "cum1dump1ster", "cul1tur1ed", "ecc1hi", "dou1jin",
        "hen1tai", "sm1ut", "lew1d", "wai1fu", "futa1nari", "tent1acle"
    ],
    "hentai": [
        "hen1tai", "douj1inshi", "ecc1hi", "y1aoi", "sho1ta", "lo1li", "tent1acle", "futa1nari",
        "bish1oujo", "bisho1unen", "mec2ha hen1tai", "hen1tai ma1ng1a", "hen1tai anime", "sm1ut",
        "erog1e", "visu1al nov1el", "hma1nga", "h1nime", "1+ ani1me", "1+ ma1nga",
        "le1wd ani1me", "lew1d man1ga", "anim1ated porn", "anim1ated sex", "hen1tai ga1me", "hen1tai ar1t",
        "hent1ai draw1ing", "hen1tai dou1jin", "yao1i hentai", "hen1tai com1ic",
        "hen1tai pic1ture", "hent1ai sce1ne", "hen1tai story", "hen1tai vid2eo", "hen1tai mov1ie",
        "hen1tai epis1ode", "hent1ai ser1ies"
    ],
    "abbreviations": [
        "s3x1", "n00d1", "1fck", "bj1", "hj1", "l1t", "h3nt1ai", "hn1tai", "pn1wh",
        "p0r1nh1wa", "l33ts1k", "l31d", "cult1d", "s3xu1al"
    ],
    "offensive_slang": [
        "sl1ut", "who1re", "tra1mp", "ska1nk", "cumdu1mpster", "gan1gba1ng", "fac1ial", "gol1den sh1o1wer",
        "pegg1ing", "rim1ming", "ro1ugh se1x", "dir1ty ta1lk", "se1x c1hat", "nu1de p1ic", "le1wd", "ti1tty",
        "twe1rk", "brea1sts", "pen1is", "vag1ina", "clito1ris", "genit1als", "sex1ual", "ka1mas1utra",
        "ince1st", "pe1do", "ra1pe", "s1ex sla1ve", "bond1age", "cre1ampie", "c1um ins1ide", "se1x do1l1l",
        "se1x mach1ine", "lat1ex", "or1al se1x", "cum1sh1ot", "deep1thro1at", "dom1ination", "submi1ssion",
        "handc1uffs", "or1gy", "role1play", "se1x to1y", "voy1eur", "cosp1lay", "cul1ture",
        "ana1l", "er2otic", "mastu1rbate", "hard1core", "bd1sm", "feti1sh", "ling1erie", "mi1lf", "tab1oo"
    ]
}

exception_keywords = ["nxi1vm", "class1room", "assass1ination", "gea1ss"]

async def check_anti_nsfw(new_name, message):
    lower_name = new_name.lower()
    for keyword in exception_keywords:
        if keyword.lower() in lower_name:
            return False  # Allow the filename if it contains an exception keyword
    
    for category, keywords in nsfw_keywords.items():
        for keyword in keywords:
            if keyword.lower() in lower_name:
                await message.reply_text("You can't rename files with NSFW content.")
                return True
    return False 
