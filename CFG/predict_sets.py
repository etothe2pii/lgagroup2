import follow_set


#pass in the relevant grammar rule, the entire list.
def predict_set(cfg, nt, n_term, term, prev_t = []):

        pre_set = []
        is_lambda = True
        index = 1
        while is_lambda and index < len(nt):
            pre_set += follow_set.first_set(cfg, nt[index], n_term, term, [])
            is_lambda = follow_set.to_lambda(cfg, nt[index], n_term, term,[])
            index += 1

        if index == len(nt) and is_lambda:
            pre_set += follow_set.follow_set(cfg, nt[0], n_term, term,[])

        return(list(set(pre_set)))


def pairwise_disjoint(cfg, nt, n_term, term, prev_t = []):

    disjoint = True
    failed_cases = []
    for c in cfg:
        for f in cfg:
            if c[0] == f[0] and not c[0] in failed_cases and not c == f:
                tmp_1 = predict_set(cfg,c,n_term,term)
                tmp_2 = predict_set(cfg,f,n_term,term)

                for t in tmp_1:
                    for m in tmp_2:
                        if t == m:
                            disjoint =False
                            failed_cases.append(c[0])

    return disjoint, failed_cases

