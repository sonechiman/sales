#!coding: utf-8
import facebook
import os
import secret


def get_friends():
	graph = facebook.GraphAPI(secret.access_token)
	args = {'fields' : 'birthday,name,work,education'}
	friends = graph.get_object("me/friends",**args)
	return friends

def arrange_dic(friends_dic):
	result = "name,birthday,graduate,companys\n"
	for f in friends_dic["data"]:
		result += "%s,"%f["name"]
		if "birthday" in f:
			result += "%s," %f["birthday"]
		else: 
			result += ","
		if "education" in f:
			y = 0
			for s in f["education"]:
				if "year" in s:
					t = int(s["year"]["name"])
					if t > y :
						y = t
			result += "%s," %y
		else:
			result += "None,"
		if "work" in f:
			for w in f["work"]:
				result += "%s," %w["employer"]["name"]
		result += "\n"

	return result

def make_csv(result,filename):
	dirpath = os.path.dirname(os.path.abspath(__file__))
	result_dirpath = dirpath + "/result/"
	csvfile = open(result_dirpath + filename + ".csv", 'w')
	csvfile.write(result.encode("utf-8"))
	csvfile.close()


def main():
	friends_dic = get_friends()
	result = arrange_dic(friends_dic)
	make_csv(result,"friend_list")


if __name__ == "__main__":
	main()