from pddiktipy import api

a = api()

list_all_univ = a.dump_all_univ()
list_all_univ_name = []
for univ in list_all_univ:
    list_all_univ_name.append(univ['nama_pt'])

list_pt_hash = []
for univ in list_all_univ_name:
    pt = a.search_pt(univ)
    list_pt_hash.append(pt[0]["website-link"])

list_email_pt = []
for link in list_pt_hash:
    new_link = link.replace("/data_pt/","")
    list_email_pt.append(a.get_kampus_detail_by_hash(new_link)["email"])

try:
    f = open("list_email.txt", "a")
    f.write(list_email_pt)
    f.close()
    print("DONE!")
except Exception as e:
    print("Error : "+e)
