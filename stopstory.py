stop_file = input("Enter stop words filename: ")
story_file = input("Enter story filename: ")
out_file = input("Enter output filename: ")

stop_words = set(open(stop_file).read().lower().split())
story = open(story_file).read().split()

result = [word for word in story if word.lower() not in stop_words]

open(out_file, "w").write(" ".join(result))

print("Stop words removed! Output saved in", out_file)
