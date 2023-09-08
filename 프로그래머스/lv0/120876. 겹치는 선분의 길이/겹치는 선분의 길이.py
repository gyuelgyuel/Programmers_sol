def solution(lines):
    line1, line2, line3 = lines
    ovl1 = ovl([line1, line2])
    ovl2 = ovl([line1, line3])
    ovl3 = ovl([line2, line3])
    ovl_len = 0
    if ovl1 and ovl2 and ovl3:
        oovl = ovl([ovl1,ovl2])
        oovl_len = oovl[1]-oovl[0]
        ovl_len = ovl1[1] - ovl1[0] + ovl2[1] - ovl2[0] + ovl3[1] - ovl3[0] - 2*oovl_len
    else:
        for ovl_line in [ovl1,ovl2,ovl3]:
            if ovl_line:
                ovl_len += (ovl_line[1] - ovl_line[0])
        
    return ovl_len

def ovl(lines):
    if lines[0][0] > lines[1][0]:
        line2, line1 = lines
    else:
        line1, line2 = lines
    if line1[1] > line2[0]:
        return [line2[0], min(line1[1], line2[1])]
    else:
        return False