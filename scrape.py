from pddiktipy import api
import time

a = api()

list_all_univ = a.dump_all_univ()

list_all_univ_name = []
list_to_write_to_f = []
list_to_write_to_f_2 = []
for univ in list_all_univ:
    nama_pt = univ['nama_pt']
    try:  
        pt = a.detail_data_univ_by_name(nama_pt)  
        if "email" in pt and pt["email"] is not None and pt["email"] != "" and pt["email"] != " ":
            email_pt = pt['email']
        else :
            email_pt = 'none'
        list_to_write_to_f.append(pt["id_sp"] + " ---- " + email_pt + " ---- " + nama_pt +"\n")
    except:
        list_to_write_to_f_2.append(nama_pt +"\n")

f = open("list_email.txt", "a")
f.write("\n".join(list_to_write_to_f))
f.close()
f_2 = open("list_kampus_error.txt","a")
f_2.write("\n".join(list_to_write_to_f_2))
f_2.close()


# list_pt_hash = []
# for univ in list_all_univ_name:
#     pt = a.search_pt(univ)
#     list_pt_hash.append(pt[0]["website-link"])

# list_email_pt = []
# for link in list_pt_hash:
#     new_link = link.replace("/data_pt/","")
#     list_email_pt.append(a.get_kampus_detail_by_hash(new_link)["email"])


