# ---------- General Functions (Not File Specific) ----------
def vowel_check(string):
	vowel_list = ['A','E','I','O','U']
	if string[0].upper() in vowel_list:
		return True
	else:
		return False