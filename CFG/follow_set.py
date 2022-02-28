import sys

#cfg is the entire context free grammar, nt is the non-terminal that the follow set is being calculated for
#n_term is the list of non-terminals, and term is the list of terminals. Takes these arguments and
#returns an array that represents the follow set.
def follow_set(cfg, nt, n_term, term, prev_t = []):
    prev_t.append(nt)
    set = []

    for c in cfg:
        if nt in c and c.index(nt) != 0:
            index = c.index(nt) + 1
            if index == len(c) and not c[0] in  prev_t:
                set = set + follow_set(cfg, c[0], n_term, term, prev_t)

            derived_lam = True
            while (derived_lam and index < len(c)):
                if not c[index] in prev_t:
                    set = set + first_set(cfg, c[index], n_term, term, [])

                if to_lambda(cfg, c[index], n_term, term):
                    index += 1
                    if index == len(c) and not c[0] in prev_t:
                        set = set + follow_set(cfg, c[0], n_term, term, prev_t)
                else:
                    derived_lam = False
    return set




def first_set(cfg, nt, n_term, term, prev_Terms = []):
    prev_Terms.append(nt)
    if (nt in term or nt == "$") and not nt == "lambda":
        return [nt]

    set = []

    for c in cfg:
        if(c[0] == nt):
            derived_lam = True
            index = 1
            while(derived_lam):
                if not c[index] in prev_Terms:
                    set = set + first_set(cfg,c[index], n_term, term, prev_Terms)

                if to_lambda(cfg,c[index], n_term, term) and index < len(c[0]):
                    index += 1
                else:
                    derived_lam = False
    return set


def to_lambda(cfg, nt, n_term, term, prev_terms = []):
    prev_terms.append(nt)
    if nt == "lambda":
        return True
    if not nt in n_term:
        return False
    to_lam_major = False
    for c in cfg:

        if(c[0] == nt):
            if(len(c) == 2 and c[1] == "lambda"):
                return True
            else:
                to_lam = True
                for f in c:
                    if f in n_term:
                        to_lam = False
                    elif f in n_term and not f in prev_terms:
                        to_lam = to_lam and to_lambda(cfg, f, n_term, term, prev_terms)
            to_lam_major = to_lam_major or to_lam


    return to_lam_major




