from flask import jsonify
def pagination(num_of_record, count, page):
    per_page = num_of_record
    previous_btn = True
    next_btn = True
    first_btn = True
    last_btn = True
    start = page * per_page
    cur_page = page
    cur_page = int(cur_page)
    msg = ""

    no_of_paginations = count // per_page

    if (count > 0):
        if(cur_page >= 7):
            start_loop = cur_page - 3
            if (no_of_paginations > cur_page + 3):
                end_loop = cur_page + 3
            elif cur_page <= no_of_paginations and cur_page > no_of_paginations - 6:
                start_loop = no_of_paginations - 6
                end_loop = no_of_paginations
            else:
                end_loop = no_of_paginations
        else:
            start_loop = 1
            if(no_of_paginations > 7):
                end_loop = 7
            else:
                end_loop = no_of_paginations
        msg += "<div class='pagination'><ul class='list-inline'>"
        if(first_btn and cur_page > 1):
            pre = cur_page - 1
            pre = str(pre)
            msg += "<li p='"+pre+"' class='active' onclick='Pagination("+pre+")'>Previous</li>"
        elif(previous_btn):
            msg += "<li class='inactive'>Previous</li>"
        for i in range(start_loop, end_loop+1):
            if(cur_page == i):
                i = str(i)
                msg += "<li p='"+i+"' class='active current-page'>"+i+"</li>"
            else:
                i = str(i)
                msg += "<li p='"+i+"' class='active' onclick='Pagination("+i+")'>"+i+"</li>"
        if(next_btn and cur_page < no_of_paginations):
            nex = cur_page + 1
            nex = str(nex)
            msg += "<li p='"+nex+"' class='active' onclick='Pagination("+nex+")'>Next</li>"
        elif next_btn:
            msg += "<li class='inactive'>Next</li>"
        if(last_btn and cur_page < no_of_paginations):
            no_of_paginations = str(no_of_paginations)
            msg += "<li p='"+no_of_paginations+"' class='active' onclick='Pagination("+no_of_paginations+")'>Last</li>"
        elif(last_btn):
            no_of_paginations = str(no_of_paginations)
            msg += "<li p='"+no_of_paginations+"' class='inactive'>Last</li>"
        goto = "<input type='text' style='display:none;' class='goto' size='1' style='margin-top:-1px;margin-left:60px;'/><input type='button' id='go_btn' class='go_button' value='Go' style='display:none;'/>"
        no_of_paginations = str(no_of_paginations)
        cur_page = str(cur_page)
        total_string = "<span class='total' a='"+no_of_paginations+"'>(page<b>" + cur_page + "</b> of <b>"+no_of_paginations+"</b> )</span>"
        msg = msg + "</ul>" + goto + total_string + "</div>"    
    else:
        msg += '<div class="col-md-12 text-center" style="color:red"><strong>No Record Found</strong></div>'
    return msg
