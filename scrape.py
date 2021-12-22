from pddiktipy import api

a = api()

list_all_univ = a.dump_all_univ()

f = open("list_email.txt", "a")
list_all_univ_name = []
for univ in list_all_univ:
    nama_pt = univ['nama_pt']
    pt = a.detail_data_univ_by_name(nama_pt)
    if "email" in pt and pt["email"] is not None and pt["email"] != "" and pt["email"] != " ":
        email_pt = pt['email']
    else :
        email_pt = 'none'
    f.write(email_pt + " ---- " +nama_pt +"\n")
f.close()



# list_pt_hash = []
# for univ in list_all_univ_name:
#     pt = a.search_pt(univ)
#     list_pt_hash.append(pt[0]["website-link"])

# list_email_pt = []
# for link in list_pt_hash:
#     new_link = link.replace("/data_pt/","")
#     list_email_pt.append(a.get_kampus_detail_by_hash(new_link)["email"])


